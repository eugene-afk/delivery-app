import instance from './instance'
import ordersModule from './orders'
import shopsModule from './shops'

export default {
    orders: ordersModule(instance),
    shops: shopsModule(instance),
}