from pydantic import Field, BaseModel


class Equipment(BaseModel):
    """设备类
    """

    device_serialnumber: str = Field(..., title="设备序列号")

    mainboard_serialnumber: str = Field(..., title="主板序列号")

    device_type: str = Field(..., title="Device类型")

    controller_type: str = Field(..., title="Controller型号")

    wifi_version: str = Field(..., title="wifi模块程序版本号")

    software_function: str

    create_time: str

    update_time: str
