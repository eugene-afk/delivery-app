export default function(instance){
    return{
        getOrders(args){
            return instance.get('orders/', {params: args})
        },
        sendOrder(payload){
            return instance.post('orders/', payload)
        },
    }
}