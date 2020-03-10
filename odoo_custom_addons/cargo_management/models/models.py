# -*- coding: utf-8 -*-

from odoo.models import Model
from odoo.fields import (Char, Many2one, Binary,
                         Datetime, Integer, Text,
                         Boolean, Selection, Float,
                         One2many, Html)
from odoo.api import (model, depends)


class Shift(Model):
    _name = 'cargo.shifts'
    _description = 'Turnos de reservacion'

    name = Char(
        size=30,
        string='Turno',
        translate=True
    )


class BurdenType(Model):
    _name = 'cargo.type_of_burden'
    _description = 'Tipo de carga'

    name = Char(
        size=30,
        string='Tipo de Carga',
        translate=True
    )


class ConfigBoxCar(Model):
    _name = 'cargo.configuration_of_box_car'
    _description = 'Configuracion de furgon'

    config = Char(
        size=30,
        string='Configuracion Furgon'
    )

    image = Binary(
        string='Imagen',
        store=True,
        attachment=False
    )

    # @model
    # @depends('image_url')
    # def _compute_image(self):
    #     for record in self:
    #         image = None
    #         if record.image_url:
    #             image = self.fetch_image_from_url(record.image_url)
    #         record.update({'image': image, })


class PackagingType(Model):
    _name = 'cargo.type_of_package'
    _description = 'Tipo de embalaje'

    name = Char(
        size=15,
        string='Tipo de embalaje',
        translate=True
    )


# class IncidentType(Model):
#     _name = 'cargo.type_of_incidents'
#     _description = 'Tipo de incidencias'
#     name = Many2one(
#         'request.type',
#         string='Incidentes'
#     )


class Journey(Model):
    _name = 'cargo.journeys'
    _description = 'Viajes'
    identifier = Char(
        string="Identificador de Viaje",
        required=True
    )
    driver_name = Char(
        size=30,
        string='Nombre del Piloto',
        required=True,
    )
    truck = Many2one(
        'fleet.vehicle',
        string='Camion',
        required=True
    )
    shift = Many2one(
        'cargo.shifts',
        string='Turno del viaje',
        required=True
    )
    datetime_planned_source = Datetime(
        string='Salida'
    )
    datetime_planned_return = Datetime(
        string='Regreso'
    )
    datetime_real_source = Datetime(
        string='Salida'
    )
    datetime_real_return = Datetime(
        string='Regreso'
    )
    quantity_journey_stop = Integer(
        string='Cantidad de Paradas'
    )

    # @depends('quantity_journey_stop')
    # def amount_journey_stop(self):
    #     if self.quantity_journey_stop:
    #         print(self.quantity_journey_stop, "CANTIDAD DE PARADAS INGRESADAS Y CON EL DEPENDS PUDE HACER ESTO, ESTA GUAY, VERDAD?")
    #         if self.quantity_journey_stop <= self.quantity_journey_stop_include:
    #             self.quantity_journey_stop.create()

    quantity_journey_stop_include = Integer(
        size='5',
        string='Cantidad de Paradas incluidas'
    )
    journeys_stop = One2many(
        "cargo.journey_stop",
        "journey",
        string='Paradas'
    )
    burdens = One2many(
        "cargo.burden",
        "journey",
        string='Cargas'
    )
    incidents = One2many(
        "cargo.incidents",
        "journey",
        string='Incidencias'
    )
    stay = Boolean('Estadia')
    assistants = Boolean('Personal Auxiliar')
    insurance = Boolean('Seguro')

    config_boxcar = Many2one(
        'cargo.configuration_of_box_car',
        string='Configuracion Furgon'
    )
    partners_help = One2many(
        "cargo.partner_help",
        "name",
        string='Personal'
    )


class Burden(Model):
    _name = "cargo.burden"
    _description = 'Carga'
    journey = Many2one(
        "cargo.journeys",
        string="Viaje"
    )
    description = Text(
        string="Descripcion"
    )
    notes = Html(
        string="Notas"
    )
    bulk = Char(
        size=30,
        string="Volumen"
    )
    range_temperature = Char(
        size=20,
        string="Rango de Temperatura"
    )
    range_humidity = Char(
        size=20,
        string="Rango de Humedad"
    )
    packaging = Many2one(
        "cargo.type_of_package",
        string="Embalaje",
        required=True
    )
    burden_cost = Float(
        string="Costo de Carga"
    )
    compartment = Text(
        size=100,
        string="Compartimiento"
    )
    load_stop = Integer(
        size=30,
        string="Parada de Carga"
    )
    download_stop = Integer(
        size=30,
        string="Parada de Descarga"
    )


class JourneyStop(Model):
    _name = 'cargo.journey_stop'
    _description = 'Paradas'
    order = Char(
        string="Orden"
    )
    location = Char(
        size=30,
        string='Ubicacion'
    )
    journey = Many2one(
        "cargo.journeys",
        string="Viaje"
    )
    instructions = Text(
        size=35,
        string='Instrucciones'
    )
    type_of_journey_stop = Selection(
        [
            ('load', 'Carga'),
            ('download', 'Descarga')
        ],
        string="Tipo"
    )
    hour_journey_stop = Float(string='Hora')

    # @depends('agreed_appointment')
    # def journey_stop(self):
    #     if self.agreed_appointment:
    #         print(self.agreed_appointment, "ES CITA  NO ES CITA DEPENDE SI EL CHECKBOX ESTA SELCCIONADO O NO.")
    #         self.hour_journey_stop.create()

    agreed_appointment = Boolean(string='Cita')
    contact_name = Char(
        size=50,
        string="Nombre Contacto"
    )
    counterpart_signature = Char(
        string="Firma Contraparte"
    )
    status = Selection(
        [
            ('CF', 'Confirmado'),
            ('CC', 'Cancelado'),
            ('HC', 'Hecho'),
            ('RPG', 'Reprogramado'),
            ('PRD', 'Perdido')
        ],
        string="Estado"
    )


class PartnerHelp(Model):
    _name = "cargo.partner_help"
    _description = "Personal Auxiliar"
    name = Char(
        size=30,
        string="Nombre"
    )
    dpi = Integer(
        size=11,
        string="Documento de Identificacion"
    )
    job = Char(
        size=30,
        string="Puesto"
    )


class Incident(Model):
    _name = "cargo.incidents"
    _description = "Incidencias"
    journey = Many2one(
        "cargo.journeys",
        string="Viaje"
    )
    journeys_stop = Many2one(
        "cargo.journey_stop",
        string='Paradas'
    )
    items = Many2one(
        "cargo.burden",
        string='Cargas'
    )
    description = Char(
        size=30,
        string="Descripcion"
    )
    incident_type = Many2one(
        'request.type',
        string='Incidentes'
    )
    responsible = Selection(
        [
            ("INT", "Interno"),
            ("TRC", "Tercero"),
            ("CLI", "Cliente")
        ],
        string="Responsable del Incidente"
    )
    name_responsible = Char(
        size=30,
        string="Nombre de Responsable"
    )
    contact = Char(
        size=30,
        string="Nombre de Contacto"
    )
    resolution = Text(
        string="Resolucion"
    )
    economic_impact = Float(
        string="Impacto Economico"
    )
    extra_charge = Boolean('Aplica Cargo Extra')
    assistant = Boolean('Aplica Seguro')
