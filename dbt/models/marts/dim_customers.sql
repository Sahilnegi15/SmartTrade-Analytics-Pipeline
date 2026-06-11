select distinct
  customer_id,
  'anonymous' as customer_name
from {{ ref('stg_orders') }}