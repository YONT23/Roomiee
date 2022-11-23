<template>
    <h1 class="pull-right">
        <div class="row">
            <div class="col-4"></div>
            <div class="col-4">
                <h3>Listado de Consultas</h3>
            </div>
            <div class="col-4">
            </div>
        </div>
    </h1>
    <div text-align:center class="d-grid gap-2">
        <div class="col-2"></div>
        <div class="row">
            <div class="col-3"></div>
            <div class="alert alert-dismissible alert-info">
                <p>Mostrar todos los Servicios, Clientes y Propietarios en un rango de fecha
                    determinada, es decir fecha inicial y fecha final.</p>
                <a href="/consulta1" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 5px;">Consulta 1</a>
            </div>
            <div class="alert alert-dismissible alert-info">
                <p>Mostrar la cantidad de servicios disponibles en un rango de fecha determinada.</p>
                <a href="/consulta2" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 5px;">Consulta 2</a>
            </div>
            <div class="alert alert-dismissible alert-info">
                <p>Mostrar la cantidad de servicios disponibles discriminados por clientes en un rango de fecha determinada.
                </p>
                <a href="/consulta3" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 5px;">Consulta 3</a>
            </div>
        </div>
    </div>
</template>

<script  lang="ts">
export default {}
</script>

<style scoped lang="css">

</style>