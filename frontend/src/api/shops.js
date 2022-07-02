export default function(instance){
    return{
        getShops(){
            return instance.get('shops/')
        },
    }
}