<template>
<v-card>
    <v-row>
        <v-col cols=12 lg=6>

            <v-card-header>
                <v-card-header-text>
                    <v-card-title>
                        Personal information
                    </v-card-title>
                    <v-card-subtitle>
                        Order # {{ item.id }}
                    </v-card-subtitle>
                </v-card-header-text>
            </v-card-header>

            <v-card-text>
                <div>
                    Customer name: 
                    <span class="font-weight-bold">
                        {{ item.name }}
                    </span>
                </div>
                <div>
                    Customer phone: 
                    <span class="font-weight-bold">
                        {{ item.phone }}
                    </span>
                </div>
                <div>
                    Delivery address: 
                    <span class="font-weight-bold">
                        {{ item.address }}
                    </span>
                </div>
                <div class="mt-2">
                    Amount: 
                    <span class="font-weight-bold">
                        ${{ item.amount }}
                    </span>
                </div>
                <div class="mt-2">
                    Status: 
                    <span class="font-weight-bold">
                        {{ decodedStatus }}
                    </span>
                </div>
            </v-card-text>

        </v-col>
        <v-col cols=12 lg=6>

            <v-card-header>
                <v-card-header-text>
                    <v-card-title>
                        Products
                    </v-card-title>                    
                </v-card-header-text>
            </v-card-header>

            <v-card-text>
                <v-table>
                    <thead>
                    <tr>
                        <th class="text-left">
                        
                        </th>
                        <th class="text-left">
                            Name
                        </th>
                        <th class="text-left">
                            Qty
                        </th>
                    </tr>
                    </thead>
                    <tbody>
                        <tr v-for="i in item.products" :key="i.id">
                            <td>
                                <img :src="`${mediaUrl}${i.product.photo}`" height="44" width="44" />
                            </td>
                            <td>{{ i.product.name }}</td>
                            <td>{{ i.qty }}</td>
                        </tr>
                    </tbody>
                </v-table>
            </v-card-text>

        </v-col>
    </v-row>
</v-card>
</template>

<script>
export default {
    name: "HistoryOrderCardComponent",
    inject: ["mediaUrl",],
    setup() {
        
    },

    computed: {
        decodedStatus(){
            switch(this.item.status[0]){
                case 1:
                    return "Pending"
                default:
                    return "Pending"
            }
        }
    },

    props: {
        item: {
            //TODO: remove object
            type: Object,
            required: true,
        }
    }
}
</script>