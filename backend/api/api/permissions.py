from rest_framework import permissions
from bilan_radio.models import BilanRadiologique
from bilan_bio.models import BilanBiologique
class HasRolePermission:
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    def __call__(self):
        class RoleBasedPermission(permissions.BasePermission):
            allowed_roles = self.allowed_roles
            def has_permission(self, request, view):
                # Check if user has required role and authenticated
                return bool(
                    request.user and
                    request.user.is_authenticated and
                    request.user.role in self.allowed_roles
                )
            

        return RoleBasedPermission
class HasBilanAssignment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj,BilanRadiologique):
            return bool(request.user and request.user.is_authenticated and obj.radiologe == request.user)
        if isinstance(obj,BilanBiologique):
            return bool(request.user and request.user.is_authenticated and obj.laborantient == request.user)
class HasDPIAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_authenticated and request.user.id == obj.id)
#  permission classes for each role
IsPatient = HasRolePermission(['patient'])
IsMedecin = HasRolePermission(['medecin'])
IsInfirmier = HasRolePermission(['infirmier'])
IsLaborantin = HasRolePermission(['laborantin'])
IsRadiologue = HasRolePermission(['radiologue'])
IsAdmin = HasRolePermission(['admin'])
IsMedicalStaff = HasRolePermission(['medecin','infirmier','laborantin','radiologue'])