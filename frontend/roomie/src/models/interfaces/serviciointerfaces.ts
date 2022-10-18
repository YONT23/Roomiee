export interface IDisponibilidad {
    id?: number;
    disp_disponible: string;
    disp_precio: number;
  }

export interface IServicio {
    id?: number;
    serv_internet: string;
    serv_cocina: string;
    serv_patio: string;
    serv_ubicacion: string;
    habitacion: any;
    huesped: any;
    baño: any;
    disponibilidad: any;
  }