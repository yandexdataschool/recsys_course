import polars as pl


def check_semantic_ids(df, num_levels=3, codebook_size=512, item_col="item_id"):
    sid_cols = [f"sid_{i}" for i in range(num_levels)]
    required = [item_col, *sid_cols]

    assert all(c in df.columns for c in required)
    assert df[item_col].n_unique() == df.height

    for c in sid_cols:
        assert df[c].null_count() == 0
        assert df[c].min() >= 0
        assert df[c].max() < codebook_size

    full = (
        df.group_by(sid_cols)
        .agg(pl.len().alias("cnt"))
        .sort("cnt", descending=True)
    )

    n_items = df.height
    n_unique = full.height
    n_extra_collisions = n_items - n_unique
    max_collision = full["cnt"].max()

    print("items:", n_items)
    print("unique semantic ids:", n_unique)
    print("extra collisions:", n_extra_collisions)
    print("max full collision:", max_collision)

    return full


def check_collision_resolving_sid(
    old_df: pl.DataFrame,
    new_df: pl.DataFrame,
    item_col: str = "item_id",
):
    old_sid_cols = sorted(
        [c for c in old_df.columns if c.startswith("sid_")],
        key=lambda x: int(x.split("_")[1]),
    )

    new_sid_cols = sorted(
        [c for c in new_df.columns if c.startswith("sid_")],
        key=lambda x: int(x.split("_")[1]),
    )

    added_cols = [c for c in new_sid_cols if c not in old_sid_cols]

    assert len(added_cols) == 1
    new_col = added_cols[0]

    assert new_df.height == old_df.height
    assert new_df[item_col].n_unique() == old_df[item_col].n_unique()
    assert new_df[item_col].n_unique() == new_df.height

    for c in old_sid_cols:
        left = old_df.select([item_col, c])
        right = new_df.select([item_col, c])
        assert left.join(right, on=[item_col, c], how="inner").height == old_df.height

    assert new_df[new_col].null_count() == 0
    assert new_df[new_col].min() == 0

    old_group_sizes = (
        old_df
        .group_by(old_sid_cols)
        .agg(pl.len().alias("old_cnt"))
    )

    new_max_sid = (
        new_df
        .group_by(old_sid_cols)
        .agg(pl.col(new_col).max().alias("max_new_sid"))
    )

    check = old_group_sizes.join(new_max_sid, on=old_sid_cols)

    bad = check.filter(pl.col("max_new_sid") != pl.col("old_cnt") - 1)
    assert bad.height == 0

    full_unique = new_df.select(new_sid_cols).unique().height
    assert full_unique == new_df.height

    print("OK")
    print("old unique semantic ids:", old_df.select(old_sid_cols).unique().height)
    print("new unique semantic ids:", new_df.select(new_sid_cols).unique().height)
    print("items:", new_df.height)
    print("new column:", new_col)
    print("max resolving sid:", new_df[new_col].max())
