
<template>
    <h1>Consulta 3</h1>
    <div class="container">
        <div class="row">
            <div class="col-3"></div>
            <div class="col-5">
                <form method="post">
                    <div  text-align="center;" class="form-group">
                        <input type="date" class="form-control my-3" placeholder="Fecha 1" name="fecha1">
                    </div>
                    <div class="form-group">
                        <input type="date" class="form-control my-3" placeholder="Fecha 2" name="fecha2">
                    </div>
                    <button type="submit" class="btn btn-primary my-3">Consultar</button>
                    {{ ' ' }}
                    <button type="button" class="btn btn-primary my-3" onclick="history.back()">Volver</button>
                </form>
            </div>
            <div class="col-2"></div>
            <div class="col-9"></div>
                <h1>Mostrando Consulta</h1>
                <div class="alert alert-success" role="alert">
                    <p>Mostrar todos los Servicios, Clientes y Propietarios en un rango de fecha
                        determinada, es decir fecha inicial y fecha final.</p>
                    <strong></strong> y <strong></strong>
                </div>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Usuario</th>
                            <th scope="col">Fecha Pres</th>
                            <th scope="col">Fecha Dev</th>
                            <th scope="col">Ejemplar</th>
    
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="table-light">
                            <td></td>
                            <td></td>
                            <td></td>
                            <td></td>
                        </tr>
                    </tbody>
                </table>
            <div class="alert alert-dismissible alert-info" role="alert">
                Debe agregar fechas validas.
            </div>
            </div>
            <div class="col-1"></div>
        </div>
</template>


<script  lang="ts">
export default {}
</script>

<style scoped lang="css">

</style>