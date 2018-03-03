from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'SUB000  ._SN',
        MapName             = 'a',
        Location            = 'a.x',
        MapIndex            = 0,
        MapDefaultBGM       = "ed60000",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_153",          # 03, 3
        "Function_4_154",          # 04, 4
        "Function_5_155",          # 05, 5
        "Function_6_156",          # 06, 6
        "Function_7_157",          # 07, 7
        "Function_8_1B0",          # 08, 8
        "Function_9_1FC",          # 09, 9
        "Function_10_259",         # 0A, 10
        "Function_11_2BD",         # 0B, 11
        "Function_12_321",         # 0C, 12
        "Function_13_380",         # 0D, 13
        "Function_14_3DF",         # 0E, 14
        "Function_15_443",         # 0F, 15
        "Function_16_4A2",         # 10, 16
        "Function_17_4F7",         # 11, 17
        "Function_18_551",         # 12, 18
        "Function_19_5B0",         # 13, 19
        "Function_20_5FE",         # 14, 20
        "Function_21_65D",         # 15, 21
        "Function_22_6B7",         # 16, 22
        "Function_23_71B",         # 17, 23
        "Function_24_77F",         # 18, 24
        "Function_25_A6D",         # 19, 25
        "Function_26_AA0",         # 1A, 26
        "Function_27_BD1",         # 1B, 27
        "Function_28_D79",         # 1C, 28
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    RunExpression(0x65, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x65), scpexpr(EXPR_END)),
        (0, "loc_DD"),
        (1, "loc_E9"),
        (2, "loc_F5"),
        (3, "loc_101"),
        (4, "loc_10D"),
        (5, "loc_119"),
        (6, "loc_125"),
        (SWITCH_DEFAULT, "loc_131"),
    )


    label("loc_DD")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_13D")

    label("loc_E9")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_13D")

    label("loc_F5")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_13D")

    label("loc_101")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_13D")

    label("loc_10D")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_13D")

    label("loc_119")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_13D")

    label("loc_125")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_13D")

    label("loc_131")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_13D")

    label("loc_13D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_152")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_13D")

    label("loc_152")

    Return()

    # Function_2_AC end

    def Function_3_153(): pass

    label("Function_3_153")

    Return()

    # Function_3_153 end

    def Function_4_154(): pass

    label("Function_4_154")

    Return()

    # Function_4_154 end

    def Function_5_155(): pass

    label("Function_5_155")

    Return()

    # Function_5_155 end

    def Function_6_156(): pass

    label("Function_6_156")

    Return()

    # Function_6_156 end

    def Function_7_157(): pass

    label("Function_7_157")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_7_157 end

    def Function_8_1B0(): pass

    label("Function_8_1B0")

    OP_31(0x8, 0x0, 0x5A)
    OP_31(0x8, 0xFE, 0x0)
    OP_41(0x8, 0x551, 0xFF)
    OP_41(0x8, 0x60E, 0xFF)
    OP_41(0x8, 0x64, 0xFF)
    OP_35(0x8, 0x0)
    OP_BB(0x8, 0x6, 0x10E)
    OP_37(0x8, 0x7F, 0x2)
    OP_41(0x8, 0x2A6, 0x0)
    OP_41(0x8, 0x296, 0x1)
    OP_41(0x8, 0x294, 0x2)
    OP_41(0x8, 0x29C, 0x3)
    OP_41(0x8, 0x29A, 0x4)
    OP_41(0x8, 0x291, 0x5)
    OP_41(0x8, 0x2C7, 0x6)
    Return()

    # Function_8_1B0 end

    def Function_9_1FC(): pass

    label("Function_9_1FC")

    OP_31(0xE, 0x0, 0x5A)
    OP_31(0xE, 0xFE, 0x0)
    OP_41(0xE, 0x5AB, 0xFF)
    OP_41(0xE, 0x60E, 0xFF)
    OP_41(0xE, 0x64, 0xFF)
    OP_35(0xE, 0x0)
    OP_37(0xE, 0x80, 0x2)
    OP_37(0xE, 0x81, 0x2)
    OP_37(0xE, 0x82, 0x2)
    OP_37(0xE, 0x83, 0x1)
    OP_37(0xE, 0x84, 0x1)
    OP_37(0xE, 0x85, 0x2)
    OP_37(0xE, 0x86, 0x2)
    OP_41(0xE, 0x2D2, 0x0)
    OP_41(0xE, 0x260, 0x1)
    OP_41(0xE, 0x25A, 0x2)
    OP_41(0xE, 0x266, 0x3)
    OP_41(0xE, 0x269, 0x4)
    OP_41(0xE, 0x274, 0x5)
    OP_41(0xE, 0x26F, 0x6)
    Return()

    # Function_9_1FC end

    def Function_10_259(): pass

    label("Function_10_259")

    OP_31(0x0, 0x0, 0x71)
    OP_31(0x0, 0xFE, 0x0)
    OP_41(0x0, 0x3E9, 0xFF)
    OP_41(0x0, 0x613, 0xFF)
    OP_41(0x0, 0x6A, 0xFF)
    OP_35(0x0, 0x0)
    OP_BB(0x0, 0x6, 0xE8)
    OP_37(0x0, 0x80, 0x2)
    OP_37(0x0, 0x81, 0x2)
    OP_37(0x0, 0x82, 0x2)
    OP_37(0x0, 0x83, 0x2)
    OP_37(0x0, 0x84, 0x2)
    OP_37(0x0, 0x85, 0x2)
    OP_37(0x0, 0x86, 0x2)
    OP_41(0x0, 0x2D6, 0x0)
    OP_41(0x0, 0x298, 0x6)
    OP_41(0x0, 0x26F, 0x1)
    OP_41(0x0, 0x2CA, 0x2)
    OP_41(0x0, 0x29E, 0x3)
    OP_41(0x0, 0x294, 0x4)
    OP_41(0x0, 0x266, 0x5)
    Return()

    # Function_10_259 end

    def Function_11_2BD(): pass

    label("Function_11_2BD")

    OP_31(0x1, 0x0, 0x66)
    OP_31(0x1, 0xFE, 0x0)
    OP_41(0x1, 0x416, 0xFF)
    OP_41(0x1, 0x610, 0xFF)
    OP_41(0x1, 0x67, 0xFF)
    OP_35(0x1, 0x0)
    OP_BB(0x1, 0x6, 0xED)
    OP_37(0x1, 0x80, 0x2)
    OP_37(0x1, 0x81, 0x2)
    OP_37(0x1, 0x82, 0x2)
    OP_37(0x1, 0x83, 0x2)
    OP_37(0x1, 0x84, 0x1)
    OP_37(0x1, 0x85, 0x2)
    OP_37(0x1, 0x86, 0x1)
    OP_41(0x1, 0x274, 0x0)
    OP_41(0x1, 0x26E, 0x1)
    OP_41(0x1, 0x2C8, 0x2)
    OP_41(0x1, 0x2C6, 0x3)
    OP_41(0x1, 0x25C, 0x4)
    OP_41(0x1, 0x265, 0x5)
    OP_41(0x1, 0x25F, 0x6)
    Return()

    # Function_11_2BD end

    def Function_12_321(): pass

    label("Function_12_321")

    OP_31(0x2, 0x0, 0x6E)
    OP_31(0x2, 0xFE, 0x0)
    OP_41(0x2, 0x443, 0xFF)
    OP_41(0x2, 0x613, 0xFF)
    OP_41(0x2, 0x6A, 0xFF)
    OP_35(0x2, 0x0)
    OP_BB(0x2, 0x6, 0xF1)
    OP_37(0x2, 0x80, 0x2)
    OP_37(0x2, 0x81, 0x1)
    OP_37(0x2, 0x82, 0x1)
    OP_37(0x2, 0x83, 0x2)
    OP_37(0x2, 0x84, 0x2)
    OP_37(0x2, 0x85, 0x2)
    OP_37(0x2, 0x86, 0x2)
    OP_41(0x2, 0x2A2, 0x0)
    OP_41(0x2, 0x266, 0x1)
    OP_41(0x2, 0x25D, 0x2)
    OP_41(0x2, 0x275, 0x3)
    OP_41(0x2, 0x280, 0x4)
    OP_41(0x2, 0x260, 0x5)
    Return()

    # Function_12_321 end

    def Function_13_380(): pass

    label("Function_13_380")

    OP_31(0x3, 0x0, 0x6B)
    OP_31(0x3, 0xFE, 0x0)
    OP_41(0x3, 0x472, 0xFF)
    OP_41(0x3, 0x612, 0xFF)
    OP_41(0x3, 0x68, 0xFF)
    OP_35(0x3, 0x0)
    OP_BB(0x3, 0x6, 0xF6)
    OP_37(0x3, 0x80, 0x2)
    OP_37(0x3, 0x81, 0x2)
    OP_37(0x3, 0x82, 0x2)
    OP_37(0x3, 0x83, 0x2)
    OP_37(0x3, 0x84, 0x2)
    OP_37(0x3, 0x85, 0x2)
    OP_37(0x3, 0x86, 0x2)
    OP_41(0x3, 0x25D, 0x0)
    OP_41(0x3, 0x26C, 0x1)
    OP_41(0x3, 0x262, 0x2)
    OP_41(0x3, 0x25F, 0x3)
    OP_41(0x3, 0x26E, 0x4)
    OP_41(0x3, 0x271, 0x5)
    Return()

    # Function_13_380 end

    def Function_14_3DF(): pass

    label("Function_14_3DF")

    OP_31(0x4, 0x0, 0x68)
    OP_31(0x4, 0xFE, 0x0)
    OP_41(0x4, 0x49D, 0xFF)
    OP_41(0x4, 0x610, 0xFF)
    OP_41(0x4, 0x67, 0xFF)
    OP_35(0x4, 0x0)
    OP_BB(0x4, 0x6, 0xFA)
    OP_37(0x4, 0x80, 0x2)
    OP_37(0x4, 0x81, 0x1)
    OP_37(0x4, 0x82, 0x1)
    OP_37(0x4, 0x83, 0x2)
    OP_37(0x4, 0x84, 0x2)
    OP_37(0x4, 0x85, 0x2)
    OP_37(0x4, 0x86, 0x2)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x265, 0x1)
    OP_41(0x4, 0x25C, 0x2)
    OP_41(0x4, 0x2D4, 0x3)
    OP_41(0x4, 0x2C9, 0x4)
    OP_41(0x4, 0x268, 0x5)
    OP_41(0x4, 0x2C6, 0x6)
    Return()

    # Function_14_3DF end

    def Function_15_443(): pass

    label("Function_15_443")

    OP_31(0x5, 0x0, 0x70)
    OP_31(0x5, 0xFE, 0x0)
    OP_41(0x5, 0x4CE, 0xFF)
    OP_41(0x5, 0x613, 0xFF)
    OP_41(0x5, 0x6A, 0xFF)
    OP_35(0x5, 0x0)
    OP_BB(0x5, 0x6, 0x101)
    OP_37(0x5, 0x80, 0x2)
    OP_37(0x5, 0x81, 0x2)
    OP_37(0x5, 0x82, 0x1)
    OP_37(0x5, 0x83, 0x2)
    OP_37(0x5, 0x84, 0x1)
    OP_37(0x5, 0x85, 0x2)
    OP_37(0x5, 0x86, 0x1)
    OP_41(0x5, 0x298, 0x0)
    OP_41(0x5, 0x272, 0x1)
    OP_41(0x5, 0x269, 0x2)
    OP_41(0x5, 0x25A, 0x3)
    OP_41(0x5, 0x283, 0x5)
    OP_41(0x5, 0x262, 0x6)
    Return()

    # Function_15_443 end

    def Function_16_4A2(): pass

    label("Function_16_4A2")

    OP_31(0x6, 0x0, 0x5C)
    OP_31(0x6, 0xFE, 0x0)
    OP_41(0x6, 0x4F7, 0xFF)
    OP_41(0x6, 0x60F, 0xFF)
    OP_41(0x6, 0x65, 0xFF)
    OP_35(0x6, 0x0)
    OP_BB(0x6, 0x6, 0x105)
    OP_37(0x6, 0x80, 0x2)
    OP_37(0x6, 0x81, 0x2)
    OP_37(0x6, 0x82, 0x1)
    OP_37(0x6, 0x83, 0x1)
    OP_37(0x6, 0x84, 0x2)
    OP_37(0x6, 0x85, 0x1)
    OP_37(0x6, 0x86, 0x2)
    OP_41(0x6, 0x2C8, 0x0)
    OP_41(0x6, 0x25E, 0x2)
    OP_41(0x6, 0x2D1, 0x3)
    OP_41(0x6, 0x258, 0x4)
    Return()

    # Function_16_4A2 end

    def Function_17_4F7(): pass

    label("Function_17_4F7")

    OP_31(0x7, 0x0, 0x6B)
    OP_31(0x7, 0xFE, 0x0)
    OP_41(0x7, 0x524, 0xFF)
    OP_41(0x7, 0x612, 0xFF)
    OP_41(0x7, 0x68, 0xFF)
    OP_35(0x7, 0x0)
    OP_BB(0x7, 0x6, 0x10B)
    OP_37(0x7, 0x80, 0x2)
    OP_37(0x7, 0x81, 0x2)
    OP_37(0x7, 0x82, 0x1)
    OP_37(0x7, 0x83, 0x2)
    OP_37(0x7, 0x84, 0x2)
    OP_37(0x7, 0x85, 0x2)
    OP_37(0x7, 0x86, 0x1)
    OP_41(0x7, 0x263, 0x0)
    OP_41(0x7, 0x25A, 0x1)
    OP_41(0x7, 0x2C9, 0x2)
    OP_41(0x7, 0x281, 0x5)
    OP_41(0x7, 0x272, 0x6)
    Return()

    # Function_17_4F7 end

    def Function_18_551(): pass

    label("Function_18_551")

    OP_31(0x9, 0x0, 0x6C)
    OP_31(0x9, 0xFE, 0x0)
    OP_41(0x9, 0x57E, 0xFF)
    OP_41(0x9, 0x613, 0xFF)
    OP_41(0x9, 0x6A, 0xFF)
    OP_35(0x9, 0x0)
    OP_BB(0x9, 0x6, 0x110)
    OP_37(0x9, 0x80, 0x2)
    OP_37(0x9, 0x81, 0x2)
    OP_37(0x9, 0x82, 0x1)
    OP_37(0x9, 0x83, 0x2)
    OP_37(0x9, 0x84, 0x2)
    OP_37(0x9, 0x85, 0x1)
    OP_37(0x9, 0x86, 0x2)
    OP_41(0x9, 0x2C3, 0x0)
    OP_41(0x9, 0x2C9, 0x1)
    OP_41(0x9, 0x263, 0x2)
    OP_41(0x9, 0x272, 0x3)
    OP_41(0x9, 0x26F, 0x4)
    OP_41(0x9, 0x25A, 0x5)
    Return()

    # Function_18_551 end

    def Function_19_5B0(): pass

    label("Function_19_5B0")

    OP_31(0xA, 0x0, 0x64)
    OP_31(0xA, 0xFE, 0x0)
    OP_41(0xA, 0x470, 0xFF)
    OP_41(0xA, 0x610, 0xFF)
    OP_41(0xA, 0x67, 0xFF)
    OP_35(0xA, 0x0)
    OP_37(0xA, 0x80, 0x2)
    OP_37(0xA, 0x81, 0x1)
    OP_37(0xA, 0x82, 0x2)
    OP_37(0xA, 0x83, 0x2)
    OP_37(0xA, 0x84, 0x2)
    OP_37(0xA, 0x85, 0x1)
    OP_37(0xA, 0x86, 0x1)
    OP_41(0xA, 0x262, 0x0)
    OP_41(0xA, 0x2C9, 0x1)
    OP_41(0xA, 0x27D, 0x2)
    OP_41(0xA, 0x25F, 0x3)
    Return()

    # Function_19_5B0 end

    def Function_20_5FE(): pass

    label("Function_20_5FE")

    OP_31(0xB, 0x0, 0x75)
    OP_31(0xB, 0xFE, 0x0)
    OP_41(0xB, 0x57F, 0xFF)
    OP_41(0xB, 0x615, 0xFF)
    OP_41(0xB, 0x6B, 0xFF)
    OP_35(0xB, 0x0)
    OP_BB(0xB, 0x6, 0x114)
    OP_37(0xB, 0x80, 0x2)
    OP_37(0xB, 0x81, 0x2)
    OP_37(0xB, 0x82, 0x2)
    OP_37(0xB, 0x83, 0x2)
    OP_37(0xB, 0x84, 0x2)
    OP_37(0xB, 0x85, 0x2)
    OP_37(0xB, 0x86, 0x2)
    OP_41(0xB, 0x298, 0x0)
    OP_41(0xB, 0x2A6, 0x1)
    OP_41(0xB, 0x2CB, 0x2)
    OP_41(0xB, 0x2A0, 0x4)
    OP_41(0xB, 0x29C, 0x5)
    OP_41(0xB, 0x2A2, 0x6)
    Return()

    # Function_20_5FE end

    def Function_21_65D(): pass

    label("Function_21_65D")

    OP_31(0xC, 0x0, 0x63)
    OP_31(0xC, 0xFE, 0x0)
    OP_41(0xC, 0x4CA, 0xFF)
    OP_41(0xC, 0x610, 0xFF)
    OP_41(0xC, 0x67, 0xFF)
    OP_35(0xC, 0x0)
    OP_BB(0xC, 0x6, 0x116)
    OP_37(0xC, 0x80, 0x2)
    OP_37(0xC, 0x81, 0x2)
    OP_37(0xC, 0x82, 0x1)
    OP_37(0xC, 0x83, 0x1)
    OP_37(0xC, 0x84, 0x1)
    OP_37(0xC, 0x85, 0x2)
    OP_37(0xC, 0x86, 0x1)
    OP_41(0xC, 0x259, 0x0)
    OP_41(0xC, 0x274, 0x1)
    OP_41(0xC, 0x25F, 0x2)
    OP_41(0xC, 0x26A, 0x4)
    OP_41(0xC, 0x270, 0x5)
    Return()

    # Function_21_65D end

    def Function_22_6B7(): pass

    label("Function_22_6B7")

    OP_31(0xD, 0x0, 0x5E)
    OP_31(0xD, 0xFE, 0x0)
    OP_41(0xD, 0x49D, 0xFF)
    OP_41(0xD, 0x60F, 0xFF)
    OP_41(0xD, 0x65, 0xFF)
    OP_35(0xD, 0x0)
    OP_BB(0xD, 0x6, 0x118)
    OP_37(0xD, 0x80, 0x2)
    OP_37(0xD, 0x81, 0x2)
    OP_37(0xD, 0x82, 0x1)
    OP_37(0xD, 0x83, 0x2)
    OP_37(0xD, 0x84, 0x1)
    OP_37(0xD, 0x85, 0x1)
    OP_37(0xD, 0x86, 0x1)
    OP_41(0xD, 0x2C8, 0x0)
    OP_41(0xD, 0x273, 0x1)
    OP_41(0xD, 0x26A, 0x2)
    OP_41(0xD, 0x276, 0x3)
    OP_41(0xD, 0x270, 0x4)
    OP_41(0xD, 0x25E, 0x5)
    OP_41(0xD, 0x267, 0x6)
    Return()

    # Function_22_6B7 end

    def Function_23_71B(): pass

    label("Function_23_71B")

    OP_31(0xF, 0x0, 0x77)
    OP_31(0xF, 0xFE, 0x0)
    OP_41(0xF, 0x5D8, 0xFF)
    OP_41(0xF, 0x615, 0xFF)
    OP_41(0xF, 0x6B, 0xFF)
    OP_35(0xF, 0x0)
    OP_BB(0xF, 0x6, 0x11C)
    OP_37(0xF, 0x80, 0x3)
    OP_37(0xF, 0x81, 0x3)
    OP_37(0xF, 0x82, 0x3)
    OP_37(0xF, 0x83, 0x3)
    OP_37(0xF, 0x84, 0x3)
    OP_37(0xF, 0x85, 0x3)
    OP_37(0xF, 0x86, 0x3)
    OP_41(0xF, 0x29D, 0x0)
    OP_41(0xF, 0x29F, 0x3)
    OP_41(0xF, 0x298, 0x4)
    OP_41(0xF, 0x294, 0x5)
    OP_41(0xF, 0x2E4, 0x6)
    OP_41(0xF, 0x2D8, 0x1)
    OP_41(0xF, 0x2D5, 0x2)
    Return()

    # Function_23_71B end

    def Function_24_77F(): pass

    label("Function_24_77F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AE")
    OP_A2(0x2CF0)
    OP_3E(0x3F0, 1)

    AnonymousTalk(    #1
        "\x07\x05Found \x1F\xF0\x03\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_7AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DD")
    OP_A2(0x2CF1)
    OP_3E(0x420, 1)

    AnonymousTalk(    #2
        "\x07\x05Found \x1F\x20\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_7DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_80C")
    OP_A2(0x2CF2)
    OP_3E(0x44A, 1)

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x4A\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_80C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83B")
    OP_A2(0x2CF3)
    OP_3E(0x47A, 1)

    AnonymousTalk(    #4
        "\x07\x05Found \x1F\x7A\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_83B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86A")
    OP_A2(0x2CF4)
    OP_3E(0x4A8, 1)

    AnonymousTalk(    #5
        "\x07\x05Found \x1F\xA8\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_86A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_899")
    OP_A2(0x2CF5)
    OP_3E(0x4D4, 1)

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xD4\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_899")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C8")
    OP_A2(0x2CF6)
    OP_3E(0x502, 1)

    AnonymousTalk(    #7
        "\x07\x05Found \x1F\x02\x05\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_8C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F7")
    OP_A2(0x2CF7)
    OP_3E(0x52C, 1)

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\x2C\x05\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_8F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926")
    OP_A2(0x2CF8)
    OP_3E(0x55C, 1)

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x5C\x05\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_955")
    OP_A2(0x2CF9)
    OP_3E(0x585, 1)

    AnonymousTalk(    #10
        "\x07\x05Found \x1F\x85\x05\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_955")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_984")
    OP_A2(0x2CFA)
    OP_3E(0x47A, 1)

    AnonymousTalk(    #11
        "\x07\x05Found \x1F\x7A\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_984")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B3")
    OP_A2(0x2CFB)
    OP_3E(0x585, 1)

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\x85\x05\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_9B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E2")
    OP_A2(0x2CFC)
    OP_3E(0x4D4, 1)

    AnonymousTalk(    #13
        "\x07\x05Found \x1F\xD4\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_9E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A11")
    OP_A2(0x2CFD)
    OP_3E(0x4A8, 1)

    AnonymousTalk(    #14
        "\x07\x05Found \x1F\xA8\x04\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A40")
    OP_A2(0x2CFE)
    OP_3E(0x5B6, 1)

    AnonymousTalk(    #15
        "\x07\x05Found \x1F\xB6\x05\x07\x05.\x02",
    )

    Jump("loc_A6C")

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6C")
    OP_A2(0x2CFF)
    OP_3E(0x5DD, 1)

    AnonymousTalk(    #16
        "\x07\x05Found \x1F\xDD\x05\x07\x05.\x02",
    )


    label("loc_A6C")

    Return()

    # Function_24_77F end

    def Function_25_A6D(): pass

    label("Function_25_A6D")

    OP_BB(0x0, 0x1, 0x0)
    OP_BB(0x1, 0x1, 0x1A)
    OP_BB(0x2, 0x1, 0x19)
    OP_BB(0x4, 0x1, 0x1D)
    OP_BB(0x3, 0x1, 0x1B)
    OP_BB(0xA, 0x1, 0xA)
    OP_BB(0xB, 0x1, 0xB)
    OP_BD()
    Return()

    # Function_25_A6D end

    def Function_26_AA0(): pass

    label("Function_26_AA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x516, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACF")
    OP_A2(0x28B1)
    OP_3E(0x419, 1)

    AnonymousTalk(    #17
        "\x07\x05Found \x1F\x19\x04\x07\x05.\x02",
    )

    Jump("loc_BD0")

    label("loc_ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x516, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFE")
    OP_A2(0x28B4)
    OP_3E(0x15E, 1)

    AnonymousTalk(    #18
        "\x07\x05Found \x1F\x5E\x01\x07\x05.\x02",
    )

    Jump("loc_BD0")

    label("loc_AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x516, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D")
    OP_A2(0x28B6)
    OP_3E(0x188, 1)

    AnonymousTalk(    #19
        "\x07\x05Found \x1F\x88\x01\x07\x05.\x02",
    )

    Jump("loc_BD0")

    label("loc_B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x517, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B5C")
    OP_A2(0x28BA)
    OP_3E(0x473, 1)

    AnonymousTalk(    #20
        "\x07\x05Found \x1F\x73\x04\x07\x05.\x02",
    )

    Jump("loc_BD0")

    label("loc_B5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x517, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8B")
    OP_A2(0x28BC)
    OP_3E(0x4CE, 1)

    AnonymousTalk(    #21
        "\x07\x05Found \x1F\xCE\x04\x07\x05.\x02",
    )

    Jump("loc_BD0")

    label("loc_B8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x517, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBA")
    OP_A2(0x28BD)
    OP_3E(0x16B, 1)

    AnonymousTalk(    #22
        "\x07\x05Found \x1F\x6B\x01\x07\x05.\x02",
    )

    Jump("loc_BD0")

    label("loc_BBA")

    OP_3E(0x204, 1)

    AnonymousTalk(    #23
        "\x07\x05Found \x1F\x04\x02\x07\x05.\x02",
    )


    label("loc_BD0")

    Return()

    # Function_26_AA0 end

    def Function_27_BD1(): pass

    label("Function_27_BD1")

    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp252_04.eff")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(2000, 0)
    Sleep(1000)
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x2, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x3, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(2000)

    def lambda_D11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D11)

    def lambda_D23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_D23)

    def lambda_D35():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_D35)

    def lambda_D47():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_D47)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    OP_83(0x0, 0x2)
    OP_83(0x1, 0x2)
    OP_83(0x2, 0x2)
    OP_83(0x3, 0x2)
    Sleep(2000)
    Return()

    # Function_27_BD1 end

    def Function_28_D79(): pass

    label("Function_28_D79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA8")
    OP_A2(0x2C50)
    OP_3E(0x663, 1)

    AnonymousTalk(    #24
        "\x07\x05Found \x1F\x63\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_DA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD7")
    OP_A2(0x2C51)
    OP_3E(0x64E, 1)

    AnonymousTalk(    #25
        "\x07\x05Found \x1F\x4E\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_DD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E06")
    OP_A2(0x2C52)
    OP_3E(0xC2, 1)

    AnonymousTalk(    #26
        "\x07\x05Found \x1F\xC2\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_E06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E35")
    OP_A2(0x2C53)
    OP_3E(0xAE, 1)

    AnonymousTalk(    #27
        "\x07\x05Found \x1F\xAE\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_E35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E64")
    OP_A2(0x2C54)
    OP_3E(0xC2, 1)

    AnonymousTalk(    #28
        "\x07\x05Found \x1F\xC2\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_E64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E93")
    OP_A2(0x2C55)
    OP_3E(0x663, 1)

    AnonymousTalk(    #29
        "\x07\x05Found \x1F\x63\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_E93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC2")
    OP_A2(0x2C56)
    OP_3E(0x663, 1)

    AnonymousTalk(    #30
        "\x07\x05Found \x1F\x63\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_EC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF1")
    OP_A2(0x2C57)
    OP_3E(0x64E, 1)

    AnonymousTalk(    #31
        "\x07\x05Found \x1F\x4E\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F20")
    OP_A2(0x2C58)
    OP_3E(0xAE, 1)

    AnonymousTalk(    #32
        "\x07\x05Found \x1F\xAE\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_F20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F4F")
    OP_A2(0x2C59)
    OP_3E(0xC2, 1)

    AnonymousTalk(    #33
        "\x07\x05Found \x1F\xC2\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_F4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F7E")
    OP_A2(0x2C5A)
    OP_3E(0x663, 1)

    AnonymousTalk(    #34
        "\x07\x05Found \x1F\x63\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_F7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FAD")
    OP_A2(0x2C5B)
    OP_3E(0xAE, 1)

    AnonymousTalk(    #35
        "\x07\x05Found \x1F\xAE\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDC")
    OP_A2(0x2C5C)
    OP_3E(0x64E, 1)

    AnonymousTalk(    #36
        "\x07\x05Found \x1F\x4E\x06\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_FDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100B")
    OP_A2(0x2C5D)
    OP_3E(0xC2, 1)

    AnonymousTalk(    #37
        "\x07\x05Found \x1F\xC2\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_100B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103A")
    OP_A2(0x2C5E)
    OP_3E(0xC2, 1)

    AnonymousTalk(    #38
        "\x07\x05Found \x1F\xC2\x00\x07\x05.\x02",
    )

    Jump("loc_1066")

    label("loc_103A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1066")
    OP_A2(0x2C5F)
    OP_3E(0x663, 1)

    AnonymousTalk(    #39
        "\x07\x05Found \x1F\x63\x06\x07\x05.\x02",
    )


    label("loc_1066")

    Return()

    # Function_28_D79 end

    SaveToFile()

Try(main)
