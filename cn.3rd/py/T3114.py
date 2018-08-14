from ED63RDScenarioHelper import *

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
        "Function_2_16C",          # 02, 2
        "Function_3_170",          # 03, 3
        "Function_4_174",          # 04, 4
        "Function_5_178",          # 05, 5
        "Function_6_17C",          # 06, 6
        "Function_7_180",          # 07, 7
    )


    def Function_0_16A(): pass

    label("Function_0_16A")

    Return()

    # Function_0_16A end

    def Function_1_16B(): pass

    label("Function_1_16B")

    Return()

    # Function_1_16B end

    def Function_2_16C(): pass

    label("Function_2_16C")

    SetPlaceName(0x94)
    Return()

    # Function_2_16C end

    def Function_3_170(): pass

    label("Function_3_170")

    SetPlaceName(0x93)
    Return()

    # Function_3_170 end

    def Function_4_174(): pass

    label("Function_4_174")

    SetPlaceName(0x96)
    Return()

    # Function_4_174 end

    def Function_5_178(): pass

    label("Function_5_178")

    SetPlaceName(0x95)
    Return()

    # Function_5_178 end

    def Function_6_17C(): pass

    label("Function_6_17C")

    SetPlaceName(0x98)
    Return()

    # Function_6_17C end

    def Function_7_180(): pass

    label("Function_7_180")

    SetPlaceName(0x97)
    Return()

    # Function_7_180 end

    SaveToFile()

Try(main)
