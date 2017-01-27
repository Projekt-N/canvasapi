from pycanvas.canvas_object import CanvasObject
from pycanvas.util import combine_kwargs


class AppointmentGroup(CanvasObject):

    def delete(self):
        """
        Delete this appointment group.

        :calls: `DELETE /api/v1/appointment_groups/:id \
        <https://canvas.instructure.com/doc/api/appointment_groups.html#method.appointment_groups.destroy>`_

        :rtype: :class:`pycanvas.appointment_group.AppointmentGroup`
        """
        response = self._requester.request(
            'DELETE',
            'appointment_groups/%s' % (self.id)
        )
        return AppointmentGroup(self._requester, response.json())

    def edit(self, **kwargs):
        """
        Modify this appointment group.

        :calls: `PUT /api/v1/appointment_groups/:id \
        <https://canvas.instructure.com/doc/api/appointment_groups.html#method.appointment_groups.update>`_

        :rtype: :class:`pycanvas.appointment_group.AppointmentGroup`
        """
        response = self._requester.request(
            'PUT',
            'appointment_groups/%s' % (self.id),
            **combine_kwargs(**kwargs)
        )

        if 'title' in response.json():
            super(AppointmentGroup, self).set_attributes(response.json())

        return AppointmentGroup(self._requester, response.json())

    def __str__(self):
        return "{} ({})".format(self.title, self.id)
