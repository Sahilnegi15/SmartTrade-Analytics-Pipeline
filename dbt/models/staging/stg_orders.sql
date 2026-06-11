select
  order_id,
  customer_id,
  product_id,
  quantity,
  price,
  cast(order_ts as timestamp) as order_ts,
  cast(from_iso8601_date(substr(order_ts,1,10)) as date) as order_date
from {{ source('stap_db', 'raw_orders') }}
where order_id is not null