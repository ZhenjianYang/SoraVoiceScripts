from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3114   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3114.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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


    DeclEvent(
        X                   = -107140,
        Y                   = 0,
        Z                   = -340,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -119480,
        Y                   = 0,
        Z                   = 6960,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -107010,
        Y                   = 0,
        Z                   = 199500,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -119590,
        Y                   = 0,
        Z                   = 206950,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = -106990,
        Y                   = 0,
        Z                   = 399440,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -119440,
        Y                   = 0,
        Z                   = 406910,
        Range               = 1000,
        Unknown_10          = 0x8CA,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 7,
    )


    ScpFunction(
        "Function_0_16A",          # 00, 0
        "Function_1_16B",          # 01, 1
        "Function_2_29D",          # 02, 2
        "Function_3_2A1",          # 03, 3
        "Function_4_2A5",          # 04, 4
        "Function_5_2A9",          # 05, 5
        "Function_6_2AD",          # 06, 6
        "Function_7_2B1",          # 07, 7
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Return()

    # Function_0_16A end

    def Function_1_16B(): pass

    label("Function_1_16B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_6F(0x3, 0)
    OP_72(0x3, 0x10)
    OP_6F(0x7, 0)
    OP_72(0x7, 0x10)
    OP_6F(0xB, 0)
    OP_72(0xB, 0x10)
    OP_6F(0x0, 29)
    OP_72(0x0, 0x10)
    OP_6F(0x1, 29)
    OP_72(0x1, 0x10)
    OP_6F(0x2, 29)
    OP_72(0x2, 0x10)
    OP_6F(0x4, 29)
    OP_72(0x4, 0x10)
    OP_6F(0x5, 29)
    OP_72(0x5, 0x10)
    OP_6F(0x6, 29)
    OP_72(0x6, 0x10)
    OP_6F(0x8, 29)
    OP_72(0x8, 0x10)
    OP_6F(0x9, 29)
    OP_72(0x9, 0x10)
    OP_6F(0xA, 29)
    OP_72(0xA, 0x10)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_79(0xFF, 0x2)
    OP_7B()
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x0)
    OP_10(0xC, 0x0)

    label("loc_29C")

    Return()

    # Function_1_16B end

    def Function_2_29D(): pass

    label("Function_2_29D")

    SetPlaceName(0x94)
    Return()

    # Function_2_29D end

    def Function_3_2A1(): pass

    label("Function_3_2A1")

    SetPlaceName(0x93)
    Return()

    # Function_3_2A1 end

    def Function_4_2A5(): pass

    label("Function_4_2A5")

    SetPlaceName(0x96)
    Return()

    # Function_4_2A5 end

    def Function_5_2A9(): pass

    label("Function_5_2A9")

    SetPlaceName(0x95)
    Return()

    # Function_5_2A9 end

    def Function_6_2AD(): pass

    label("Function_6_2AD")

    SetPlaceName(0x98)
    Return()

    # Function_6_2AD end

    def Function_7_2B1(): pass

    label("Function_7_2B1")

    SetPlaceName(0x97)
    Return()

    # Function_7_2B1 end

    SaveToFile()

Try(main)
