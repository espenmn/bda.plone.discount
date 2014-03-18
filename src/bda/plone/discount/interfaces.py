from zope.interface import Interface


class IDiscountExtensionLayer(Interface):
    """Browser layer for bda.plone.discount.
    """


class IDiscountEnabled(Interface):
    """Interface for marking content having discount settings enabled.
    """


class IDiscountSettings(Interface):
    """Interface for discount settings.
    """


class ICartItemDiscountSettings(IDiscountSettings):
    """Interface for cart item discount settings.
    """


class IUserCartItemDiscountSettings(ICartItemDiscountSettings):
    """Interface for cart item user discount settings.
    """


class IGroupCartItemDiscountSettings(ICartItemDiscountSettings):
    """Interface for cart item group discount settings.
    """


class ICartDiscountSettings(IDiscountSettings):
    """Interface for cart discount settings.
    """


class IUserCartDiscountSettings(ICartDiscountSettings):
    """Interface for cart user discount settings.
    """


class IGroupCartDiscountSettings(ICartDiscountSettings):
    """Interface for cart group discount settings.
    """
