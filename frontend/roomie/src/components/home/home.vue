<template>
    <div>
        <Search />
    </div>
    <div class="d-flex flex-row flex-wrap justify-content-around my-5">
        <template v-for="ser in servicio">
            <CardServicio :i={...ser} />
        </template>
    </div>
</template>

<script lang="ts" >
import { store } from '../../context/store';
import CardServicio from '../UI/card.vue';
import Search from '../UI/search.vue';

export default {
    data() {
        return {
            servicio: [...store.state.servicio]
        }
    },
    mounted() {
        store.commit('getAllServicio', "http://127.0.0.1:8000/servicios/all/");
    },
    components: {
        Search,
        CardServicio
    },
}
</script>

<style scoped lang="scss">

</style>