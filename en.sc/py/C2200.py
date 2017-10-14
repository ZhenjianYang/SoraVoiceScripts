from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2200.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60031",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Manoria Byroad',                       # 9
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 1330,
        Z                   = -430,
        Y                   = -46450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_CA",           # 00, 0
        "Function_1_CB",           # 01, 1
        "Function_2_EC",           # 02, 2
    )


    def Function_0_CA(): pass

    label("Function_0_CA")

    Return()

    # Function_0_CA end

    def Function_1_CB(): pass

    label("Function_1_CB")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFDDD20, 0x230050)
    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x2)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_CB end

    def Function_2_EC(): pass

    label("Function_2_EC")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_2_EC end

    SaveToFile()

Try(main)
