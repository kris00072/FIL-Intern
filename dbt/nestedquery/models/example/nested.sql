with rename_column as(
    select

        contactLastName

    from
        fil.customers
)

select * from rename_columns