select
  order_id,
  customer_id,
  product_id,
  quantity,
  price,
  quantity * price as revenue,
  order_date
from {{ ref('stg_orders') }}