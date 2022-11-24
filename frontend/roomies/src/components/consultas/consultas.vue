<template>
    <h1 class="pull-right">
        <div class="row">
            <div class="col-1"></div>
            <div class="col-9">
                <center>
                    <h3>Listado de Consultas</h3>
                </center>
                <div text-align:center class="alert alert-success" role="alert">
                    <center>
                        <p class="tt">Consultas preDefinidas que te permitiran observar como se conforma un poco Roomies.</p>
                    </center>
                </div>
                <div class="col-4">
                </div>
            </div>
        </div>
    </h1>
    <div text-align:center class="d-grid gap-2">
        <div class="col-2"></div>
        <div class="row">
            <div class="col-3"></div>
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Mostrar todos los Clientes y la cantidad de hombres, como la de mujeres que hacen parte de
                        Roomies.</p>
                    <a href="/consulta1" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 5px;">Consulta
                        1</a>
                </center>
            </div>
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Mostrar Pagos por fecha de los Clientes que hacen parte de Roomies.</p>
                    <a href="/consulta2" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 5px;">Consulta
                        2</a>
                </center>
            </div>
            <div class="alert alert-dismissible alert-info">
                <center>
                    <p>Mostrar la cantidad de servicios disponibles discriminados por clientes en un rango de fecha
                        determinada.
                    </p>
                    <a href="/consulta3" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 5px;">Consulta
                        3</a>
                </center>
            </div>
        </div>
    </div>
</template>

<script  lang="ts">
export default {}
</script>

<style scoped lang="css">
.tt{
    font-size:small;
}
</style>