from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7309   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7309.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60224",
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
        '怀斯曼',                               # 9
        '洛斯托尔姆',                           # 10
        '阿斯塔尔特',                           # 11
        '基尔巴特',                             # 12
        '深渊战鬼',                             # 13
        '深渊战鬼',                             # 14
        '深渊战鬼',                             # 15
        '深渊战鬼',                             # 16
        '深渊战鬼',                             # 17
        '深渊战鬼',                             # 18
        '提妲',                                 # 19
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 20
        '穆拉',                                 # 21
        '乔丝特',                               # 22
        '约修亚',                               # 23
        '科洛丝',                               # 24
        '基库',                                 # 25
        '奥利维尔',                             # 26
        '金',                                   # 27
        '亚妮拉丝',                             # 28
        '雪拉扎德',                             # 29
        '阿加特',                               # 30
        '艾丝蒂尔',                             # 31
        '理查德',                               # 32
        '玲',                                   # 33
        '玲的大镰刀',                           # 34
        '',                                     # 35
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -6120,
        Y                   = -2000,
        Z                   = 24960,
        Range               = 5700,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x7080,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_40A",          # 00, 0
        "Function_1_41E",          # 01, 1
        "Function_2_462",          # 02, 2
        "Function_3_535",          # 03, 3
        "Function_4_658",          # 04, 4
        "Function_5_725",          # 05, 5
        "Function_6_7E4",          # 06, 6
        "Function_7_7F5",          # 07, 7
        "Function_8_38B7",         # 08, 8
        "Function_9_3905",         # 09, 9
        "Function_10_3958",        # 0A, 10
        "Function_11_5BF3",        # 0B, 11
        "Function_12_5E55",        # 0C, 12
        "Function_13_5EBF",        # 0D, 13
        "Function_14_5F2E",        # 0E, 14
        "Function_15_5FC1",        # 0F, 15
        "Function_16_61BF",        # 10, 16
        "Function_17_6213",        # 11, 17
        "Function_18_6282",        # 12, 18
        "Function_19_63B2",        # 13, 19
        "Function_20_641F",        # 14, 20
        "Function_21_648E",        # 15, 21
        "Function_22_64F6",        # 16, 22
        "Function_23_655E",        # 17, 23
        "Function_24_65C6",        # 18, 24
        "Function_25_662E",        # 19, 25
        "Function_26_684D",        # 1A, 26
        "Function_27_6A70",        # 1B, 27
        "Function_28_6C85",        # 1C, 28
        "Function_29_6EA4",        # 1D, 29
        "Function_30_6F89",        # 1E, 30
        "Function_31_705B",        # 1F, 31
        "Function_32_707A",        # 20, 32
        "Function_33_709E",        # 21, 33
        "Function_34_70C2",        # 22, 34
        "Function_35_710E",        # 23, 35
        "Function_36_71B9",        # 24, 36
        "Function_37_71F8",        # 25, 37
        "Function_38_7294",        # 26, 38
        "Function_39_7308",        # 27, 39
        "Function_40_7368",        # 28, 40
        "Function_41_73AC",        # 29, 41
        "Function_42_73EB",        # 2A, 42
        "Function_43_7445",        # 2B, 43
        "Function_44_7484",        # 2C, 44
        "Function_45_74C3",        # 2D, 45
        "Function_46_7502",        # 2E, 46
        "Function_47_7555",        # 2F, 47
        "Function_48_7594",        # 30, 48
        "Function_49_75D8",        # 31, 49
        "Function_50_7617",        # 32, 50
        "Function_51_7656",        # 33, 51
        "Function_52_7695",        # 34, 52
        "Function_53_76ED",        # 35, 53
        "Function_54_7731",        # 36, 54
        "Function_55_7755",        # 37, 55
        "Function_56_7779",        # 38, 56
        "Function_57_77A5",        # 39, 57
        "Function_58_77BF",        # 3A, 58
        "Function_59_77D9",        # 3B, 59
        "Function_60_77F3",        # 3C, 60
        "Function_61_780D",        # 3D, 61
        "Function_62_7827",        # 3E, 62
        "Function_63_7841",        # 3F, 63
        "Function_64_78AF",        # 40, 64
        "Function_65_7922",        # 41, 65
        "Function_66_7995",        # 42, 66
        "Function_67_7A08",        # 43, 67
        "Function_68_7A7B",        # 44, 68
        "Function_69_7AEE",        # 45, 69
        "Function_70_7B05",        # 46, 70
        "Function_71_7B8B",        # 47, 71
        "Function_72_7CE3",        # 48, 72
        "Function_73_7D20",        # 49, 73
        "Function_74_7D43",        # 4A, 74
    )


    def Function_0_40A(): pass

    label("Function_0_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_41D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_41D")

    Return()

    # Function_0_40A end

    def Function_1_41E(): pass

    label("Function_1_41E")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE6DA8, 0x23009C)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_72(0x1000, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_461")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x17B)
    ClearMapFlags(0x100000)

    label("loc_461")

    Return()

    # Function_1_41E end

    def Function_2_462(): pass

    label("Function_2_462")

    OP_D2(0x2906D9, 0x2906DD, 0x0)
    OP_D2(0x2906DA, 0x2906DE, 0x1)
    OP_D2(0x26020B, 0x260210, 0x2)
    OP_D2(0x26029A, 0x26029F, 0x3)
    OP_D2(0x2701F8, 0x2701FD, 0x4)
    OP_D2(0x270176, 0x270183, 0x5)
    OP_D2(0x270177, 0x270184, 0x6)
    OP_D2(0x27058C, 0x270590, 0x7)
    OP_D2(0x27058D, 0x270591, 0x8)
    OP_D2(0x270088, 0x27008C, 0x9)
    OP_D2(0x270089, 0x27008D, 0xA)
    OP_D2(0x2705AF, 0x2705B3, 0xB)
    OP_D2(0x2701D0, 0x2701D5, 0xC)
    OP_D2(0x260119, 0x26011E, 0xD)
    OP_D2(0x270293, 0x27029D, 0xE)
    OP_D2(0x27028E, 0x270298, 0xF)
    OP_D2(0x270296, 0x2702A0, 0x10)
    OP_D2(0x260357, 0x26035C, 0x11)
    OP_D2(0x270179, 0x270186, 0x12)
    OP_D2(0x27058F, 0x270593, 0x13)
    OP_D2(0x260358, 0x26035D, 0x14)
    Return()

    # Function_2_462 end

    def Function_3_535(): pass

    label("Function_3_535")

    OP_D2(0x27023E, 0x270248, 0x2)
    OP_D2(0x27023F, 0x270249, 0x3)
    OP_D2(0x270110, 0x270120, 0x9)
    OP_D2(0x270111, 0x270121, 0xA)
    OP_D2(0x27051E, 0x27052B, 0xB)
    OP_D2(0x27051F, 0x27052C, 0xC)
    OP_D2(0x270504, 0x270511, 0xD)
    OP_D2(0x270505, 0x270512, 0xE)
    OP_D2(0x270538, 0x270545, 0xF)
    OP_D2(0x270539, 0x270546, 0x10)
    OP_D2(0x27036E, 0x27037B, 0x11)
    OP_D2(0x27036F, 0x27037C, 0x12)
    OP_D2(0x70219, 0x70225, 0x13)
    OP_D2(0x70232, 0x7023E, 0x14)
    OP_D2(0x70230, 0x7023C, 0x15)
    OP_D2(0x70231, 0x7023D, 0x16)
    OP_D2(0x70248, 0x70254, 0x17)
    OP_D2(0x70249, 0x70255, 0x18)
    OP_D2(0x702B4, 0x702BB, 0x19)
    OP_D2(0x702B5, 0x702BC, 0x1A)
    OP_D2(0x70326, 0x7032D, 0x1B)
    OP_D2(0x70327, 0x7032E, 0x1C)
    OP_D2(0x2702C2, 0x2702CC, 0x1D)
    OP_D2(0x2702C3, 0x2702CD, 0x1E)
    OP_D2(0x702D2, 0x702D9, 0x1F)
    OP_D2(0x702D3, 0x702DA, 0x20)
    OP_D2(0x2702D6, 0x2702E0, 0x21)
    OP_D2(0x2702D7, 0x2702E1, 0x22)
    OP_D2(0x70218, 0x70224, 0x23)
    Return()

    # Function_3_535 end

    def Function_4_658(): pass

    label("Function_4_658")

    LoadEffect(0x0, "battle\\btgun00.eff")
    LoadEffect(0x1, "battle\\btgun60.eff")
    LoadEffect(0x2, "battle\\mgaria0.eff")
    LoadEffect(0x3, "map\\mp003_00.eff")
    LoadEffect(0x4, "battle\\btbomb00.eff")
    LoadEffect(0x5, "magic\\mg051_0.eff")
    LoadEffect(0x6, "magic\\mg023_0.eff")
    OP_D2(0x270509, 0x270516, 0xE)
    OP_D2(0x27053A, 0x270547, 0x10)
    OP_D2(0x270373, 0x270380, 0x12)
    OP_D2(0x70219, 0x70225, 0x13)
    OP_D2(0x70232, 0x7023E, 0x15)
    OP_D2(0x702B6, 0x702BD, 0x1A)
    Return()

    # Function_4_658 end

    def Function_5_725(): pass

    label("Function_5_725")

    OP_D2(0x2906DB, 0x2906DF, 0x1)
    OP_D2(0x2906DC, 0x2906E0, 0x2)
    OP_D2(0x2701F8, 0x2701FD, 0x4)
    OP_D2(0x270176, 0x270183, 0x5)
    OP_D2(0x270177, 0x270184, 0x6)
    OP_D2(0x27058C, 0x270590, 0x7)
    OP_D2(0x27058D, 0x270591, 0x8)
    OP_D2(0x270112, 0x270122, 0x9)
    OP_D2(0x7021A, 0x70226, 0xA)
    OP_D2(0x270520, 0x27052D, 0xB)
    OP_D2(0x270246, 0x270250, 0xD)
    OP_D2(0x27023F, 0x270249, 0xF)
    OP_D2(0x70219, 0x70225, 0x14)
    OP_D2(0x70232, 0x7023E, 0x15)
    OP_D2(0x7024A, 0x70256, 0x17)
    OP_D2(0x70328, 0x7032F, 0x1B)
    OP_D2(0x2702C4, 0x2702CE, 0x1D)
    OP_D2(0x702D4, 0x702DB, 0x1F)
    OP_D2(0x2702D8, 0x2702E2, 0x21)
    Return()

    # Function_5_725 end

    def Function_6_7E4(): pass

    label("Function_6_7E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 7)), scpexpr(EXPR_END)), "loc_7EC")
    Return()

    label("loc_7EC")

    Call(0, 7)
    Call(0, 10)
    Return()

    # Function_6_7E4 end

    def Function_7_7F5(): pass

    label("Function_7_7F5")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 2)
    LoadEffect(0x0, "map\\mp267_00.eff")
    LoadEffect(0x1, "monster\\msc1000.eff")
    LoadEffect(0x2, "map\\mp251_00.eff")
    LoadEffect(0x3, "map\\mp251_01.eff")
    LoadEffect(0x4, "monster\\ms32000.eff")
    LoadEffect(0x5, "map\\mp121_00.eff")
    LoadEffect(0x6, "map\\mp268_00.eff")
    LoadEffect(0x7, "map\\mp269_00.eff")
    SetChrPos(0x109, -820, 1400, 24800, 0)
    SetChrPos(0x10F, 900, 1400, 24590, 0)
    OP_6D(-1980, 1160, 27070, 0)
    OP_67(0, 4670, -10000, 0)
    OP_6B(2310, 0)
    OP_6C(315000, 0)
    OP_6E(416, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x10F,
        "#1934F#6P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1069F#6P到了吗……！\x02",
    )

    CloseMessageWindow()

    def lambda_98B():
        OP_6D(-4050, 5360, 65160, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_98B)

    def lambda_9A3():
        OP_67(0, 7000, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_9A3)

    def lambda_9BB():
        OP_6B(5410, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_9BB)

    def lambda_9CB():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_9CB)

    def lambda_9DB():
        OP_6E(332, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9DB)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)
    Fade(1000)
    OP_6D(0, 14260, 68030, 0)
    OP_67(0, 3850, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(0, 0)
    OP_6E(371, 0)

    def lambda_A37():
        OP_6D(0, 9110, 66180, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_A37)

    def lambda_A4F():
        OP_67(0, 0, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_A4F)

    def lambda_A67():
        OP_6B(4030, 7000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_A67)

    def lambda_A77():
        OP_6E(441, 7000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A77)
    WaitChrThread(0xEE, 0x1)
    Sleep(1000)

    def lambda_A91():
        OP_6D(0, 3060, 48480, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_A91)

    def lambda_AA9():
        OP_67(0, 3390, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_AA9)

    def lambda_AC1():
        OP_6B(3500, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_AC1)

    def lambda_AD1():
        OP_6E(330, 5000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_AD1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 3160, 56800, 180)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(2000)
    SetChrPos(0x109, -340, 1160, 39710, 0)
    SetChrPos(0x10F, 800, 1160, 38710, 0)

    def lambda_B33():
        OP_8E(0xFE, 0xFFFFFE7A, 0x488, 0xB11C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B33)
    Sleep(200)

    def lambda_B53():
        OP_8E(0xFE, 0x32A, 0x488, 0xAF96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_B53)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #2
        0x10F,
        (
            "#1933F#6P『炼狱门』……\x02\x03",

            "#1936F『彼门以扭曲为牢固之基。\x01",
            "  乃生者与亡者分隔之关口……』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1065F#6P这与圣典记载的典故……\x01",
            "真是一模一样啊……\x02\x03",

            "#1063F现在的问题是，\x01",
            "要怎样才能打开这扇大门……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x02呵呵……\x01",
            "遗憾的是你不可能做到。\x07\x00\x02",
        )
    )

    Jump("loc_CB6")

    label("loc_CB6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_20(0x7D0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0x10F,
        "#1934F#6P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x109,
        "#1063F#6P（……这声音是……！）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(1610, 3160, 58190, 0)
    OP_67(0, 4520, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(44000, 0)
    OP_6E(360, 0)

    def lambda_DAC():
        OP_6B(2550, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_DAC)
    OP_0D()
    OP_22(0x137, 0x1, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 3160, 56800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    def lambda_DFC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DFC)
    OP_22(0x2DF, 0x0, 0x64)
    WaitChrThread(0x10, 0x0)
    OP_23(0x137)
    WaitChrThread(0xEE, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x82, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS472._CH")
    OP_C6(0x0, 0x0, 160000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    OP_1D(0xB6)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("怀斯曼")

    AnonymousTalk(    #7
        (
            "\x07\x02别来无恙。\x01",
            "凯文·格拉汉姆……\x02\x03",

            "万没想到会在这种地方\x01",
            "和你再次相遇……\x07\x00\x02",
        )
    )

    Jump("loc_EDE")

    label("loc_EDE")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #8
        0x109,
        (
            "#1075F#1P哼，果然出现了。\x02\x03",

            "#1073F在这里闲荡的尽是些被我正法的人，\x01",
            "就算碰上你也不是件奇怪的事情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1942F#1P……他、他是谁？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        (
            "#1065F#1P前任封圣省司教——\x01",
            "教会史上最邪恶的破戒僧……\x02\x03",

            "之后投身于『噬身之蛇』的使徒——\x01",
            "外号『白面』的魔人。\x02\x03",

            "#1072F半年前被我就地正法的『异端』——\x01",
            "盖鲁格·怀斯曼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1949F#1P#3S！！！#2S\x02\x03",

            "这、这个男人就是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(3450, 1160, 54380, 0)
    OP_67(0, 3690, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(44000, 0)
    OP_6E(414, 0)
    OP_6D(3450, 1160, 54380, 0)
    OP_67(0, 3990, -10000, 0)
    OP_6B(3310, 0)
    OP_6C(44000, 0)
    OP_6E(414, 0)
    OP_6D(3650, 1160, 55320, 0)
    OP_67(0, 3180, -10000, 0)
    OP_6B(3310, 0)
    OP_6C(39000, 0)
    OP_6E(414, 0)
    SetChrPos(0x10, 0, 3160, 56790, 180)
    SetChrPos(0x109, -1200, 1160, 45660, 0)
    SetChrPos(0x10F, 440, 1160, 45830, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0x10,
        (
            "\x07\x02#1154F#5P哼哼……\x01",
            "被你乘虚而入是我的失策。\x02\x03",

            "#1150F『异端制裁者』凯文·格拉汉姆。\x02\x03",

            "让我万没想到的是，\x01",
            "你竟是继承了许久不曾出现的『第五位』的人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1075F#6P我这个『守护骑士』，\x01",
            "一直以来都是扮演着『隐藏王牌』的角色。\x02\x03",

            "#1073F将你正法之后，\x01",
            "『王牌』也就已经出完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "\x07\x02#1151F#5P哼哼……封圣省那帮人…\x01",
            "还真是用心良苦啊……\x02\x03",

            "#1154F恐怕在你显露『圣痕』之后不久，\x01",
            "教会那些杂碎就已经酝酿好这计划了。\x02\x03",

            "『盐之桩』和『守护骑士』……\x02\x03",

            "#1150F只要拥有这两个条件，\x01",
            "要讨伐本人可以说是万无一失的事情。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1844F#6P啊啊，应该就是这样。\x02\x03",

            "#1843F从这种意义上……\x01",
            "正如你之前所说的那样，\x01",
            "我的的确确是一条走狗。\x02\x03",

            "#1076F……但我觉得对付你已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "\x07\x02#1151F#5P哼哼，\x01",
            "看来你还很引以为荣嘛。\x02\x03",

            "#1154F话说回来……\x01",
            "该说你不愧为『守护骑士』吗。\x02\x03",

            "在关于『圣痕』这方面，\x01",
            "我也反反复复做了很多独立的研究……\x02\x03",

            "#1150F真没想到，\x01",
            "原始的圣痕竟然拥有那样\x01",
            "超然的潜在能力。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        "#1072F#6P你在说什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "\x07\x02#1154F#5P哼哼……\x01",
            "我想你也应该多少感觉到了吧。\x02\x03",

            "这个『炼狱』就是你的潜在期望，\x01",
            "是一个受到你的意念影响\x01",
            "而衍生出来的世界……\x02\x03",

            "#1151F说得更准确一点——\x01",
            "一切缘由都归于你自己的『圣痕』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x109,
        "#1847F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10F,
        "#1931F#12P究竟是什么意思……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "\x07\x02#1152F#5P『环』的毁灭……\x01",
            "会为以『子系统』形式存在的『影之国』\x01",
            "带来致命的混乱。\x02\x03",

            "这也是没办法的事情……\x01",
            "因为掌管自己的存在\x01",
            "突然消失得无影无踪。\x02\x03",

            "#1154F之后，『影之国』……\x01",
            "期望着有一个可以接管自己的新『主人』。\x02\x03",

            "#1151F说得更准确一点……\x01",
            "那个时候，它会在靠近『环』的人里面，\x01",
            "挑选一名带有严重精神创伤的人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10F,
        "#1949F#3S#12P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        "#1079F#6P………啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "\x07\x02#1150F#5P而且……\x01",
            "『影之国』能够探索到你内心深处的圣痕，\x01",
            "然后以吸取的形式将其复制。\x02\x03",

            "而且『圣痕』……\x01",
            "会制造一个你潜在的期望——『炼狱』，\x01",
            "并使其出现在『影之国』之中。\x02\x03",

            "#1154F呵呵……\x01",
            "所以，在如此的情况和理由之下，\x01",
            "『影之王』就诞生了出来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        "#1076F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10F,
        "#1942F#12P………凯文…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "\x07\x02#1154F#5P呵呵……\x01",
            "我想，解释还是到此为止吧。\x02\x03",

            "#1150F根据本人所研究的成果……\x01",
            "在这里，我就给你指一条正确的路吧。\x02\x03",

            "要想解决如今的事态——\x01",
            "除了你作出自我牺牲之外，别无他法。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #28
        0x10F,
        "#1934F#12P哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        "#1847F#6P什、什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "\x07\x02#1154F#5P如何，够简单的吧。\x02\x03",

            "#1155F只要舍弃你那作为人类的心就行了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        "#1931F#3S#12P！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        "#1067F#6P………啊……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "\x07\x02#1155F#5P说到底，你身上的『圣痕』\x01",
            "是一种由绝望和罪恶感所衍生出来的产物。\x02\x03",

            "只要你愿意成为那一种\x01",
            "不受低级感情所束缚的存在就行了……\x02\x03",

            "也就是说——变成一个不依靠任何客体，\x01",
            "可以自如控制自己的『超人』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1076F#6P…………………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10F,
        (
            "#1935F#12P鬼、鬼话连篇……\x02\x03",

            "#1931F你所说的……\x01",
            "对人类来说绝对不是正确的道路！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "\x07\x02#1151F#5P哼哼，可是对本人来说，\x01",
            "那一直是我梦寐以求的崇高理想。\x02\x03",

            "#1154F『圣痕』的研究本身就是一环……\x02\x03",

            "虽然在约修亚身上的实验失败了，\x01",
            "不过，如今的你却有着有过之而无不及的价值。\x02\x03",

            "#1150F更何况，当成为了『超人』的时候……\x01",
            "你就可以完完全全控制『圣痕』，\x01",
            "成为新的『影之王』也不在话下。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        (
            "#1951F#12P住嘴，你这个『白面』……！\x02\x03",

            "#1939F已经够了。\x01",
            "我不许你再这么花言巧语挑唆凯文！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "\x07\x02#1151F#5P哼哼……\x01",
            "不是挑唆，无非是建议罢了。\x02\x03",

            "我可以在此向你们发誓……\x01",
            "我刚才所说的一切绝无戏言。\x02\x03",

            "虽然他是亲手毁灭我的仇人……\x01",
            "不过，既然事态已发展到如此地步，\x01",
            "过去的恩怨也显得微不足道。\x02\x03",

            "#1154F我好想见识一下……\x02\x03",

            "#1155F我不惜舍弃七耀教义，\x01",
            "于『结社』所追求的『超人』之路\x01",
            "在真正意义上实现的那瞬间……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        "#1935F#12P………痴人说梦…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        (
            "#1843F#6P#40W……莉丝，可以了。\x02\x03",

            "#1845F别再说了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x10F, 0x109, 500)
    Sleep(200)

    ChrTalk(    #41
        0x10F,
        "#1949F#11P凯文……！？\x02",
    )

    CloseMessageWindow()

    def lambda_210F():

        label("loc_210F")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_210F")

    QueueWorkItem2(0x10F, 3, lambda_210F)

    def lambda_2120():
        OP_6D(3650, 1160, 56300, 1600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2120)

    def lambda_2138():
        OP_8F(0xFE, 0xFFFFFD44, 0x488, 0xB8F6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2138)
    WaitChrThread(0x109, 0x0)
    OP_44(0x10F, 0x3)
    OP_8C(0x10F, 0, 0)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    Sleep(500)

    ChrTalk(    #42
        0x10,
        (
            "\x07\x02#1154F#5P哼哼……这就好。\x02\x03",

            "#1151F我知道你是个聪明人，\x01",
            "一定明白我刚才说的意思。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1076F#6P#40W的确……\x01",
            "我必须变得更坚强才行。\x02\x03",

            "不管是亲手\x01",
            "杀死露菲娜姐姐……\x02\x03",

            "还是对陷入绝境的母亲\x01",
            "见死不救……\x02\x03",

            "#1065F还有现在，因为我，\x01",
            "把莉丝和其他伙伴都牵连进来……\x02\x03",

            "所有这些事情……\x01",
            "都是因为我这个懦弱的废物引起的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        "#1942F#12P凯文……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "\x07\x02#1154F#5P呵呵，的确如此。\x02\x03",

            "#1151F不过……\x01",
            "这种弱点也不是不可克服的。\x02\x03",

            "只要你照我说的选择『超人』这一条路。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        (
            "#1076F#6P#40W啊……\x01",
            "或许，这是解决问题的办法。\x02\x03",

            "#1843F#20W——但是，\x01",
            "我果然还是无法选择这条路。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x10,
        "\x07\x02#1153F#5P………什么……………\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB2)
    Sleep(500)

    ChrTalk(    #48
        0x109,
        (
            "#1844F#6P#40W看来，\x01",
            "我是一个比你想像的还要懦弱的人啊。\x02\x03",

            "那时候的巧克力味道……\x01",
            "我是一辈子也不会忘记的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "\x07\x02#1156F#5P什……！？\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1934F#12P…………啊………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1076F#6P#40W那时候……\x01",
            "我的的确确陷入了绝望的境地……\x02\x03",

            "但是，正因为如此……\x01",
            "那块巧克力对我来说，\x01",
            "是一种一辈子也难以忘怀的味道。\x02\x03",

            "#1065F心酸的事、痛苦的事、悲哀的事、\x01",
            "愉快的事、欢乐的事……\x02\x03",

            "#1840F连同所有这些，\x01",
            "还有那鼓励我继续前进的、甘苦同在的，\x01",
            "却又让人难以忘怀的味道……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        "#1952F#12P………凯文…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1075F#6P#40W所以，很抱歉，『白面』。\x02\x03",

            "#1078F你的建议……\x01",
            "请恕我无法接纳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "\x07\x02#1152F#5P…………………………………\x02\x03",

            "#1154F哼哼……没关系。\x02\x03",

            "你要选择什么样的路……\x01",
            "是你的自由……\x02\x03",

            "#1155F——但是，凭你那份天真的感伤，\x01",
            "要如何才能度过危机呢！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(0, 3160, 61610, 0)
    OP_67(0, 2090, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(0, 0)
    OP_6E(385, 0)
    OP_0D()
    SetChrChipByIndex(0x10, 13)
    SetChrSubChip(0x10, 0)

    def lambda_27ED():
        OP_99(0x10, 0x0, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_27ED)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_2837():
        OP_99(0x10, 0x3, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2837)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x10, 14)
    SetChrSubChip(0x10, 0)

    def lambda_2860():

        label("loc_2860")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2860")

    QueueWorkItem2(0x10, 0, lambda_2860)
    Sleep(1500)
    OP_22(0x99, 0x0, 0x64)
    OP_0D()

    def lambda_287E():
        OP_6B(4300, 300)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_287E)
    FadeToDark(300, 16777215, -1)
    OP_0D()
    SetChrPos(0x11, -7500, -8160, 47000, 132)
    OP_A1(0x11, 0x1)
    OP_72(0x401, 0x0)
    ExitThread()
    SetChrPos(0x12, 7500, -8160, 47000, 219)
    OP_A1(0x12, 0x2)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_44(0x13, 0x2)
    OP_6D(-70, 1460, 51580, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(4230, 0)
    OP_6C(0, 0)
    OP_6E(440, 0)

    def lambda_2912():
        OP_6B(3800, 6000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2912)
    SetChrPos(0x109, -170, 1160, 47920, 0)
    SetChrPos(0x10F, 760, 1160, 46700, 0)
    Sleep(500)
    FadeToBright(300, 16777215)
    OP_0D()
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0xFF, -7500, 1200, 47000, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xFF, 7500, 1200, 47000, 0, 0, 0, 1400, 1400, 1400, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x85, 0x1, 0x64)

    def lambda_29DA():

        label("loc_29DA")

        OP_7C(0x96, 0x96, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_29DA")

    QueueWorkItem2(0x109, 3, lambda_29DA)
    OP_22(0x137, 0x1, 0x50)
    OP_22(0x32E, 0x0, 0x64)
    PlayEffect(0x3, 0x3, 0xFF, -7500, 1200, 47000, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xFF, 7500, 1200, 47000, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2AA1():
        OP_8F(0xFE, 0xFFFFE2B4, 0x488, 0xB798, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2AA1)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x8)
    OP_43(0x10F, 0x0, 0x0, 0x9)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)

    def lambda_2ADE():
        OP_8F(0xFE, 0x1D4C, 0x488, 0xB798, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_2ADE)
    Fade(500)
    OP_44(0x13, 0x2)
    OP_6D(-9820, 1180, 58880, 0)
    OP_67(0, 2640, -10000, 0)
    OP_6B(4300, 0)
    OP_6C(348000, 0)
    OP_6E(402, 0)

    def lambda_2B3F():
        OP_6B(3800, 4000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2B3F)
    OP_0D()
    Sleep(2500)
    Fade(500)
    OP_44(0x13, 0x2)
    OP_6D(10440, 1180, 58480, 0)
    OP_67(0, 2640, -10000, 0)
    OP_6B(4300, 0)
    OP_6C(12000, 0)
    OP_6E(402, 0)

    def lambda_2B9B():
        OP_6B(3800, 4000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2B9B)
    OP_0D()
    Sleep(2500)
    Fade(1000)
    OP_6D(-80, 3160, 60190, 0)
    OP_67(0, 2500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(300, 0)
    OP_43(0x10, 0x3, 0x0, 0x4A)
    OP_44(0x109, 0x3)
    OP_23(0x85)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    PlayEffect(0x4, 0x5, 0x11, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x12, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2C77():
        OP_6D(0, 2000, 56380, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2C77)

    def lambda_2C8F():
        OP_67(0, 2000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2C8F)

    def lambda_2CA7():
        OP_6B(4250, 3000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2CA7)

    def lambda_2CB7():
        OP_6E(400, 3000)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_2CB7)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    Sleep(500)
    OP_44(0x10, 0x0)
    OP_82(0x0, 0x2)
    SetChrChipByIndex(0x10, 15)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x10, 0x3)
    Sleep(500)

    ChrTalk(    #55
        0x10F,
        "#1949F#6P……啊………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x109,
        (
            "#1063F#6P阿斯塔尔特和洛斯托尔姆……\x02\x03",

            "监守『炼狱门』\x01",
            "左右的恶魔……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "\x07\x02#1154F#5P哼哼……\x01",
            "就算是『守护骑士』，\x01",
            "对付这些怪物也没有胜算吧。\x02\x03",

            "#1151F就算是为了保护她也好，\x01",
            "你应该选择哪一条路呢……\x02\x03",

            "难道，你没有改变主意的念头吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        "#1067F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10F,
        (
            "#1939F#5P凯文……\x01",
            "没有必要再听他胡说八道！\x02\x03",

            "因为我一点儿也不怕……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        (
            "#1841F#6P除了『白面』之外，\x01",
            "还有两个高级的恶魔要对付……\x02\x03",

            "的确，\x01",
            "大概连万分之一的胜算都没有吧。\x02\x03",

            "#1840F……对于以前的我来说。\x02",
        )
    )

    Jump("loc_2F47")

    label("loc_2F47")

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x10,
        "\x07\x02#1153F#5P什么……\x07\x00\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x99)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0x0, "map\\mp121_01.eff")
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x5, 0x0)
    OP_6D(1160, 1160, 42750, 0)
    OP_67(0, 4000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(90000, 0)
    OP_6E(290, 0)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 1)
    OP_22(0x85, 0x1, 0x64)

    def lambda_300E():

        label("loc_300E")

        OP_7C(0x64, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_300E")

    QueueWorkItem2(0x10F, 3, lambda_300E)

    def lambda_3029():
        OP_6B(2000, 4500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3029)

    def lambda_3039():
        OP_6E(380, 4500)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3039)

    def lambda_3049():
        OP_67(0, 3650, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3049)

    def lambda_3061():
        OP_6C(122000, 4500)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_3061)
    OP_22(0x34F, 0x0, 0x64)
    PlayEffect(0x6, 0x0, 0x109, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)

    ChrTalk(    #62 op#A op#5
        0x109,
        "#1847F#4S#28A#5P啊啊啊啊啊……！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_0D()

    def lambda_30F0():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_30F0)
    WaitChrThread(0x13, 0x0)
    OP_82(0x0, 0x2)
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    Sleep(300)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x5, 0x1, 0x109, 0, 1000, -700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x109, 20)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0x353, 0x0, 0x64)
    OP_22(0x34F, 0x0, 0x64)
    PlayEffect(0x7, 0x2, 0x109, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_31A9():

        label("loc_31A9")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_31A9")

    QueueWorkItem2(0x10F, 3, lambda_31A9)

    def lambda_31C4():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_31C4)

    ChrTalk(    #63 op#A op#5
        0x109,
        "#1069F#4S#20A#5P哦哦哦哦哦哦……！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_44(0x10F, 0x3)
    OP_23(0x85)
    OP_82(0x2, 0x2)
    Fade(500)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x4, 0x5, 0x11, 0, 1200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x109, 0, 1000, -700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_6D(-1880, 1160, 45240, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(1700, 0)
    OP_6C(315000, 0)
    OP_6E(448, 0)

    def lambda_32D1():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_32D1)
    OP_0D()
    WaitChrThread(0x109, 0x2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #64
        (
            "\x07\x05凯文学会了新的Ｓ战技\x01",
            "\x07\x02『圣枪乌尔』\x07\x05。\x02",
        )
    )

    Jump("loc_332D")

    label("loc_332D")

    CloseMessageWindow()
    OP_22(0x21E, 0x0, 0x64)

    AnonymousTalk(    #65
        (
            "\x07\x05拥有空属性的全体攻击能力，\x01",
            "对付恶魔系的敌人能够发挥出惊人的威力。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #66
        "\x07\x05将『圣枪乌尔』设定为Ｓ爆发技吗？\x18\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3441")

    Menu(
        1,
        -1,
        200,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_33F7")

    label("loc_33F7")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3415"),
        (SWITCH_DEFAULT, "loc_342D"),
    )


    label("loc_3415")

    OP_35(0x8, 0x12B)
    OP_BB(0x8, 0x6, 0x12B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_343E")

    label("loc_342D")

    OP_35(0x8, 0x12B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_343E")

    label("loc_343E")

    Jump("loc_33C1")

    label("loc_3441")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(0, 3100, 49950, 0)
    OP_67(0, 2340, -10000, 0)
    OP_6B(3290, 0)
    OP_6C(0, 0)
    OP_6E(399, 0)
    SetChrPos(0x109, -200, 1160, 45300, 0)
    SetChrPos(0x10F, 900, 1160, 43000, 0)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x11, -6500, 1160, 47000, 132)
    SetChrPos(0x12, 6500, 1160, 47000, 219)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #67
        0x10F,
        "#1934F#12P………真厉害……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        (
            "\x07\x02#1157F#5P不、不可能……\x02\x03",

            "这道『圣痕』的亮光是……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x109,
        (
            "#1065F#6P这是我身上的『圣痕』\x01",
            "原本所拥有的另外一种形态……\x02\x03",

            "#1063F对迄今为止的我来说，\x01",
            "是没有被发现的光明的一面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        "\x07\x02#1156F#5P什、什么意思……！？\x07\x00\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x109,
        (
            "#1840F#6P多谢了，『白面』……\x02\x03",

            "#1075F多亏谢绝了你的建议……\x01",
            "我对自己\x01",
            "开始有些信心了。\x02\x03",

            "#1063F非常抱歉……\x01",
            "就让我将这种新力量在你身上试验一下吧。\x02",
        )
    )

    Jump("loc_36C7")

    label("loc_36C7")

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "\x07\x02#1157F#5P你这条……走狗！！\x02\x03",

            "#1154F就凭你这临阵磨枪的一点本事，\x01",
            "也想凌驾于我『白面』之上……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #73
        0x10,
        "\x07\x02#1155F#4S想试验的话，我奉陪到底！\x07\x00\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_378A():
        OP_6D(0, 3410, 50150, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_378A)

    def lambda_37A2():
        OP_67(0, 2870, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_37A2)

    def lambda_37BA():
        OP_6B(3480, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_37BA)

    def lambda_37CA():
        OP_6E(451, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_37CA)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 16)
    SetChrSubChip(0x10, 0)
    Sleep(500)
    OP_D8(0x1, 0x3E8)
    OP_D8(0x2, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x2002, 0x0)
    ExitThread()
    OP_22(0xED, 0x0, 0x64)
    OP_6F(0x1, 81)
    OP_70(0x1, 0x5A)
    OP_6F(0x2, 41)
    OP_70(0x2, 0x32)
    OP_73(0x1)
    OP_73(0x2)
    WaitChrThread(0xEE, 0x0)

    def lambda_3833():
        OP_6D(0, 3110, 49800, 300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3833)

    def lambda_384B():
        OP_67(0, 3400, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_384B)

    def lambda_3863():
        OP_6B(2700, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3863)

    def lambda_3873():
        OP_6E(400, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3873)
    OP_22(0xF1, 0x0, 0x64)
    OP_6F(0x1, 91)
    OP_70(0x1, 0x68)
    OP_6F(0x2, 51)
    OP_70(0x2, 0x40)
    OP_73(0x1)
    OP_73(0x2)
    WaitChrThread(0xEE, 0x0)
    Battle(0x2CF, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_7_7F5 end

    def Function_8_38B7(): pass

    label("Function_8_38B7")

    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)

    def lambda_38CC():
        OP_96(0xFE, 0xFFFFFD30, 0x488, 0xABEA, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38CC)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 315, 0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_8_38B7 end

    def Function_9_3905(): pass

    label("Function_9_3905")

    Sleep(150)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)

    def lambda_391F():
        OP_96(0xFE, 0x370, 0x488, 0xAB18, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_391F)
    WaitChrThread(0xFE, 0x1)
    OP_8C(0xFE, 45, 0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_9_3905 end

    def Function_10_3958(): pass

    label("Function_10_3958")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Call(0, 2)
    LoadEffect(0x0, "map\\mp270_00.eff")
    LoadEffect(0x1, "map\\snddst0.eff")
    LoadEffect(0x7, "map\\mp266_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, -740, 1160, 47780, 0)
    SetChrPos(0x10F, 850, 1160, 47700, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 3160, 56790, 180)
    SetChrChipByIndex(0x10, 12)
    SetChrSubChip(0x10, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_43(0x10, 0x3, 0x0, 0x49)
    OP_22(0x137, 0x1, 0x46)
    PlayEffect(0x0, 0x0, 0x10, 0, 200, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_6D(-3610, 1160, 55880, 0)
    OP_67(0, 4260, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(357, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_6B(3400, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #74
        0x10,
        (
            "\x07\x02#1151F#40W嘿嘿……干得不赖嘛……\x02\x03",

            "#1154F但是，只要这个『影之国』仍然存在，\x01",
            "『我』这个概念就是不会灭亡的……\x02\x03",

            "你这种拼命的逞强\x01",
            "到底还能撑到什么时候……\x02\x03",

            "在这片炼狱的缝隙之中，\x01",
            "我一定会拭目以待……\x02\x03",

            "#1155F哼哼哼……哈哈哈哈哈哈哈……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_44(0x10, 0x3)
    OP_6D(-1340, 3160, 57720, 0)
    OP_67(0, 4260, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(315000, 0)
    OP_6E(372, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)

    def lambda_3C28():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3C28)
    OP_23(0x137)
    OP_22(0x2DF, 0x0, 0x64)

    def lambda_3C40():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3C40)
    OP_82(0x0, 0x2)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    WaitChrThread(0xEE, 0x0)
    Sleep(1000)

    def lambda_3C69():
        OP_6D(-1590, 1160, 49680, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3C69)

    def lambda_3C81():
        OP_67(0, 4430, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3C81)

    def lambda_3C99():
        OP_6B(2770, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3C99)

    def lambda_3CA9():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3CA9)

    def lambda_3CB9():
        OP_6E(307, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3CB9)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #75
        0x109,
        (
            "#1075F#5P哈哈，拼命的逞强吗……\x02\x03",

            "#1840F真是的……\x01",
            "被他说中了要害之处啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #76
        0x10F,
        "#1942F#12P哎……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-2360, 1160, 46800, 0)
    OP_67(0, 4430, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(230000, 0)
    OP_6E(307, 0)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x800)
    OP_0D()
    Sleep(300)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0x10F,
        "#1939F#6P凯文……！\x02",
    )

    CloseMessageWindow()
    OP_8F(0x10F, 0xC8, 0x488, 0xBBC6, 0xBB8, 0x0)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 11)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #78
        0x10F,
        (
            "#1949F#6P你没事吧……！？\x01",
            "振作点……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x109,
        (
            "#1841F#5P#40W唉……\x01",
            "毕竟刚才是硬撑过来的啊……\x02\x03",

            "#1844F不过，不要紧……\x01",
            "我不会像之前那样不堪一击了。\x02\x03",

            "我已经下定决心……\x01",
            "要认真去面对我自身，\x01",
            "以及露菲娜姐姐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10F,
        "#1946F#6P………凯文……………\x02",
    )

    CloseMessageWindow()

    def lambda_3F3A():

        label("loc_3F3A")

        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0x7D0)
        OP_48()
        Jump("loc_3F3A")

    QueueWorkItem2(0x109, 3, lambda_3F3A)
    Sleep(300)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_8C(0x10F, 270, 0)
    OP_0D()

    def lambda_3F82():
        OP_8F(0xFE, 0x226, 0x488, 0xBAB8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3F82)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x800)
    OP_0D()
    OP_44(0x109, 0x3)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)
    OP_8C(0x10F, 0, 400)

    def lambda_3FCC():
        OP_6D(-580, 3530, 55570, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3FCC)

    def lambda_3FE4():
        OP_67(0, 3000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_3FE4)

    def lambda_3FFC():
        OP_6B(3550, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3FFC)

    def lambda_400C():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_400C)

    def lambda_401C():
        OP_6E(363, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_401C)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #81
        0x109,
        (
            "#1840F#5P哈哈……不过，这回真惨了。\x02\x03",

            "虽然我们好容易才打倒了『白面』……\x01",
            "不过看来还是找不到\x01",
            "打开这扇大门的方法……\x02\x03",

            "#1065F即使合我们二人之力，\x01",
            "也似乎无法让它出现一丝的裂纹。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-1650, 1160, 49650, 0)
    OP_67(0, 4430, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(315000, 0)
    OP_6E(307, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #82
        0x10F,
        (
            "#1935F#6P……嗯。\x02\x03",

            "#1936F不过……\x01",
            "我们千辛万苦才来到这儿……\x02\x03",

            "#1932F事到如今，\x01",
            "我们也唯有靠武力强行破坏它了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #83
        0x109,
        (
            "#1068F#5P我都说了，\x01",
            "能不能最后再考虑过激的方法……\x02\x03",

            "#1067F而且，\x01",
            "这里是支撑『炼狱』的最重要的构造部分，\x02\x03",

            "我想不会那么容易就被我们……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -480, 1160, 36790, 0)
    SetChrChipByIndex(0x13, 4)

    NpcTalk(    #84
        0x13,
        "声音",
        "#2P喂～喂……！\x02",
    )

    Jump("loc_42D5")

    label("loc_42D5")

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4314():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4314)
    Sleep(100)
    OP_8C(0x10F, 270, 600)
    OP_8C(0x10F, 180, 600)
    Sleep(200)

    ChrTalk(    #85
        0x10F,
        "#1934F#11P这声音是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x109,
        "#1064F#5P开、开玩笑的吧……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrPos(0x13, 0, -50, 3000, 0)
    Fade(1000)
    OP_6D(-560, -50, 15940, 0)
    OP_67(0, 9140, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(225000, 0)
    OP_6E(324, 0)
    OP_43(0x13, 0x0, 0x0, 0x46)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    def lambda_43FF():
        OP_6D(-600, 1160, 33710, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_43FF)

    def lambda_4417():
        OP_6B(2460, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4417)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #87
        0x13,
        (
            "#1228F#5P#60W呼～呼～呼～呼……\x02\x03",

            "#1223F#30W真、真是绝处逢生啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-1070, 1160, 35000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(1930, 0)
    OP_6C(314000, 0)
    OP_6E(378, 0)

    def lambda_44DF():
        OP_6D(-1070, 1160, 36670, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_44DF)
    SetChrPos(0x109, -590, 1160, 42540, 180)
    SetChrPos(0x10F, 540, 1160, 43390, 180)
    SetChrPos(0x13, 350, 1160, 34360, 0)

    def lambda_452A():
        OP_8E(0xFE, 0xFFFFFD30, 0x488, 0x8FC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_452A)
    Sleep(200)

    def lambda_454A():
        OP_8E(0xFE, 0x1F4, 0x488, 0x90F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_454A)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x3)

    ChrTalk(    #88
        0x109,
        (
            "#1068F#5P唉……\x01",
            "这位小哥也真不是普通人啊。\x02\x03",

            "#1063F你怎么也\x01",
            "跑到这种地方来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10F,
        (
            "#1936F#11P……的确很不寻常。\x02\x03",

            "#1945F难道你……\x01",
            "和『影之王』串通好了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrPos(0x13, 170, 1160, 34360, 0)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 1)
    ClearChrFlags(0x13, 0x20)
    ClearChrFlags(0x13, 0x800)
    ClearChrFlags(0x13, 0x2)
    OP_44(0x13, 0x3)
    OP_0D()
    Sleep(500)

    ChrTalk(    #90
        0x13,
        (
            "#1224F#6P那、那是谁啊……\x02\x03",

            "#1228F……啊啊，够了够了！\x01",
            "现在可不是闲聊的时候！\x02\x03",

            "#1225F咱们赶快逃吧！\x01",
            "否则就会被那些家伙吃掉的！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x109,
        "#1064F#5P哎……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0x148, 0x0, 0x3C)
    Sleep(1000)
    OP_43(0x13, 0x0, 0x0, 0x45)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x109,
        "#1847F#5P那是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10F,
        (
            "#1931F#11P这咆哮声、振翅声……\x01",
            "……而且数量还很多！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x9A)
    OP_44(0x13, 0x0)
    OP_23(0x120)
    OP_22(0x17C, 0x0, 0x64)
    Fade(1000)
    OP_6D(0, 5310, 37000, 0)
    OP_67(0, 9300, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(360, 0)
    OP_43(0x14, 0x0, 0x0, 0x3F)
    OP_43(0x15, 0x0, 0x0, 0x40)
    OP_43(0x16, 0x0, 0x0, 0x41)
    OP_43(0x17, 0x0, 0x0, 0x42)
    OP_43(0x18, 0x0, 0x0, 0x43)
    OP_43(0x19, 0x0, 0x0, 0x44)
    Sleep(1000)

    def lambda_485B():
        OP_6D(-770, 1160, 37470, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_485B)

    def lambda_4873():
        OP_67(0, 6500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4873)

    def lambda_488B():
        OP_6B(3100, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_488B)

    def lambda_489B():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_489B)

    def lambda_48AB():
        OP_6E(360, 8000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_48AB)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x13, 180, 600)

    def lambda_48E4():
        OP_8F(0xFE, 0xFA, 0x488, 0x8A20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_48E4)

    ChrTalk(    #94 op#A op#5
        0x13,
        "#1227F#5P#15A#4S哇呀呀呀～～～！！\x05\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 5)
    SetChrSubChip(0x109, 0)

    def lambda_4948():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4948)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 0)

    def lambda_496A():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_496A)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #95
        0x10F,
        "#1949F#5P是、是一大群恶魔……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1067F#5P虽然不及之前碰到的那两只可怕，\x01",
            "但也都是一些等级相当高的家伙……\x02\x03",

            "混帐……\x01",
            "数量也多得有点夸张吧……！\x02",
        )
    )

    Jump("loc_4A55")

    label("loc_4A55")

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x13, 90, 600)
    Sleep(300)
    OP_8C(0x13, 270, 600)
    Sleep(300)
    OP_8C(0x13, 180, 600)

    ChrTalk(    #97
        0x13,
        (
            "#1225F#6P你、你们两个！\x01",
            "无论如何都要负起保护我的责任哦！\x02\x03",

            "我、我可不想\x01",
            "在这种鬼地方死掉！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10F,
        "#1939F#5P我们也是一样啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1068F#5P是啊，我也已经受够了。\x02\x03",

            "#1067F（糟了……\x01",
            "  刚才使用『圣痕』的力量有些过度……）\x02\x03",

            "（要想想办法才行……\x01",
            "  至少也要让莉丝和这家伙能够逃走……）\x02",
        )
    )

    CloseMessageWindow()
    OP_23(0x120)

    def lambda_4BD9():
        OP_6D(-770, 1160, 37800, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4BD9)

    def lambda_4BF1():
        OP_67(0, 6500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4BF1)

    def lambda_4C09():
        OP_6B(2450, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_4C09)

    def lambda_4C19():
        OP_6E(375, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4C19)
    OP_22(0x148, 0x0, 0x64)
    OP_43(0x14, 0x0, 0x0, 0x39)
    OP_43(0x15, 0x0, 0x0, 0x3A)
    OP_43(0x16, 0x0, 0x0, 0x3B)
    OP_43(0x17, 0x0, 0x0, 0x3C)
    OP_43(0x18, 0x0, 0x0, 0x3D)
    OP_43(0x19, 0x0, 0x0, 0x3E)
    OP_43(0x109, 0x0, 0x0, 0x36)
    OP_43(0x10F, 0x0, 0x0, 0x37)
    OP_43(0x13, 0x0, 0x0, 0x38)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #100
        0x13,
        (
            "#1227F#6P别、别过来……\x01",
            "别过来啊啊啊～～～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10F,
        "#1949F#5P……凯文……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x109,
        (
            "#1069F#5P可恶……\x01",
            "这样下去的话……！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x19, 0x0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_4D32():

        label("loc_4D32")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_4D32")

    QueueWorkItem2(0x13, 3, lambda_4D32)
    OP_22(0x14F, 0x0, 0x64)
    PlayEffect(0x7, 0x7, 0xFF, 0, 5000, 57000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0xBB8)
    Call(0, 3)
    Fade(1000)
    PlayEffect(0x7, 0x7, 0xFF, 0, 6800, 64500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6D(190, 7160, 60720, 0)
    OP_67(0, 3360, -10000, 0)
    OP_6B(4360, 0)
    OP_6C(0, 0)
    OP_6E(395, 0)

    def lambda_4E69():
        OP_6B(4059, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4E69)
    OP_6F(0x0, 1)
    OP_70(0x0, 0x5A)
    OP_73(0x0)
    OP_23(0x85)
    OP_44(0x13, 0x3)
    OP_22(0x88, 0x0, 0x64)
    Sleep(300)
    OP_1D(0x99)

    def lambda_4E9D():
        OP_6D(0, 3000, 62070, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4E9D)

    def lambda_4EB5():
        OP_67(0, 4300, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4EB5)

    def lambda_4ECD():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4ECD)

    def lambda_4EDD():
        OP_6E(310, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_4EDD)
    OP_43(0x26, 0x0, 0x0, 0x28)
    Sleep(300)
    OP_43(0x1E, 0x0, 0x0, 0x29)
    Sleep(100)
    OP_43(0x1A, 0x0, 0x0, 0x2E)
    Sleep(100)
    OP_43(0x23, 0x0, 0x0, 0x31)
    Sleep(500)
    OP_43(0x28, 0x0, 0x0, 0x35)
    Sleep(100)
    OP_43(0x25, 0x0, 0x0, 0x2D)
    Sleep(500)
    OP_43(0x27, 0x0, 0x0, 0x34)
    Sleep(100)
    OP_43(0x24, 0x0, 0x0, 0x2A)
    Sleep(100)
    OP_43(0x21, 0x0, 0x0, 0x2B)
    Sleep(100)
    OP_43(0x1F, 0x0, 0x0, 0x2C)
    Sleep(500)
    OP_43(0x1D, 0x0, 0x0, 0x30)
    Sleep(100)
    OP_43(0x1B, 0x0, 0x0, 0x33)
    Sleep(100)
    OP_43(0x1C, 0x0, 0x0, 0x32)
    Sleep(100)
    OP_43(0x22, 0x0, 0x0, 0x2F)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x1B, 0x0)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x22, 0x0)
    Sleep(400)

    ChrTalk(    #103
        0x26,
        (
            "#1018F#5P#3S你们都不要紧吧！？\x01",
            "凯文先生、莉丝小姐！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #104
        0x1E,
        (
            "#1514F#5P太好了……\x01",
            "看来我们来得还算及时！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #105
        0x1D,
        "#216F#5P什、什么，这里是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x1A,
        "#065F#5P地、地狱……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x28,
        (
            "#1306F#5P唔……\x01",
            "看来是类似『炼狱』的地方。\x02\x03",

            "#261F嘻嘻，真是耐人寻味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x25,
        (
            "#051F#5P嘿，\x01",
            "还好我们及时赶来这里！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x24,
        (
            "#1536F#5P呵呵……\x01",
            "可以大展一番拳脚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x23,
        (
            "#819F#5P好、好像……\x01",
            "有个很面善的人也混在这里面呢。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x109, -520, 1160, 37350, 0)
    SetChrPos(0x10F, 640, 1160, 37560, 0)
    Sleep(300)
    Fade(500)
    OP_6D(-1950, 1160, 40140, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(307, 0)
    OP_8C(0x109, 0, 0)
    OP_8C(0x10F, 0, 0)
    OP_8C(0x13, 0, 0)
    OP_8C(0x14, 0, 0)
    OP_8C(0x15, 0, 0)
    OP_8C(0x16, 0, 0)
    OP_8C(0x17, 0, 0)
    OP_8C(0x18, 0, 0)
    OP_8C(0x19, 0, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #111
        0x109,
        "#1064F#5P你、你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10F,
        "#1934F#6P为、为什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x1B,
        (
            "#172F#3P自从失散之后，\x01",
            "我们就请赛雷斯托大人\x01",
            "帮忙四处搜寻你们的下落。\x02\x03",

            "因为你们拿着『方石』，\x01",
            "所以总算能够查明你们的位置！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x1F,
        (
            "#1382F#3P就在不久之前，\x01",
            "她帮我们打开了连通这里的门！\x02\x03",

            "只要穿过这扇门，\x01",
            "我们就可以回到『庭院』了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x109,
        "#1840F#5P是吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10F,
        "#1946F#6P……真是得救了……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x13,
        "#1221F#6P难、难以置信……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x22,
        (
            "#076F#3P……有话回去再说！\x02\x03",

            "我们现在冲过去\x01",
            "将那些家伙的包围阵打散！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x27,
        (
            "#112F#3P你们只要看准机会，\x01",
            "赶快跑进门里面就可以了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x109,
        "#1062F#5P……多谢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10F,
        "#1932F#6P拜托大家了……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-2000, 3160, 60400, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(315000, 0)
    OP_6E(307, 0)
    SetChrPos(0x26, -650, 3160, 56460, 180)
    SetChrPos(0x1E, 780, 3160, 56730, 180)
    SetChrPos(0x1C, 2400, 3160, 59800, 180)
    SetChrPos(0x1F, -1110, 3160, 58800, 180)
    SetChrPos(0x1B, -2140, 3160, 59600, 180)
    OP_0D()
    Sleep(500)

    ChrTalk(    #122
        0x21,
        (
            "#1545F#11P呵呵……\x01",
            "那么现在就开始吧。\x02\x03",

            "#1550F在灼热的火焰之中，\x01",
            "与这些恶魔一同起舞！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x1C,
        "#272F#11P破邪显正……\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #124
        0x1C,
        (
            "#271F#11P#3S在范德尔手中的剑前，\x01",
            "你们就老老实实给我粉碎吧！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #125
        0x26,
        "#1005F#5P#4S各位……要上了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("全员")

    AnonymousTalk(    #126
        "\x07\x00#5S是！\x02",
    )

    Jump("loc_56DB")

    label("loc_56DB")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(150)
    Call(0, 4)
    OP_43(0x26, 0x0, 0x0, 0x1F)
    OP_43(0x1E, 0x0, 0x0, 0x20)
    OP_43(0x28, 0x0, 0x0, 0x21)
    OP_43(0x1B, 0x0, 0x0, 0x22)
    OP_43(0x25, 0x0, 0x0, 0x23)
    OP_43(0x22, 0x0, 0x0, 0x24)
    OP_43(0x23, 0x0, 0x0, 0x25)
    OP_43(0x1C, 0x0, 0x0, 0x26)
    OP_43(0x27, 0x0, 0x0, 0x27)
    SetChrChipByIndex(0x1F, 18)
    SetChrSubChip(0x1F, 0)

    def lambda_5750():

        label("loc_5750")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_5750")

    QueueWorkItem2(0x1F, 3, lambda_5750)
    PlayEffect(0x2, 0x0, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrChipByIndex(0x24, 14)
    SetChrSubChip(0x24, 0)

    def lambda_57A7():

        label("loc_57A7")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_57A7")

    QueueWorkItem2(0x24, 3, lambda_57A7)
    PlayEffect(0x2, 0x1, 0x24, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    SetChrChipByIndex(0x21, 16)
    SetChrSubChip(0x21, 0)
    OP_43(0x21, 0x0, 0x0, 0x1C)
    Sleep(100)
    SetChrChipByIndex(0x1A, 21)
    SetChrSubChip(0x1A, 0)
    OP_43(0x1A, 0x0, 0x0, 0x1E)
    Sleep(300)
    SetChrChipByIndex(0x1D, 26)
    SetChrSubChip(0x1D, 0)
    OP_43(0x1D, 0x0, 0x0, 0x1D)
    Sleep(2500)
    Call(0, 5)
    OP_43(0x21, 0x0, 0x0, 0x19)
    OP_43(0x1A, 0x0, 0x0, 0x1B)
    OP_43(0x1D, 0x0, 0x0, 0x1A)
    Fade(1000)
    OP_6D(-2620, 1160, 33690, 0)
    OP_67(0, 5460, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(225000, 0)
    OP_6E(332, 0)

    def lambda_5891():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5891)
    PlayEffect(0x5, 0xFF, 0x17, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0x16, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x26, 0x0, 0x0, 0x10)
    OP_43(0x1E, 0x0, 0x0, 0x11)
    OP_43(0x28, 0x0, 0x0, 0x12)
    OP_43(0x1B, 0x0, 0x0, 0x13)
    OP_43(0x25, 0x0, 0x0, 0x14)
    OP_43(0x22, 0x0, 0x0, 0x15)
    OP_43(0x23, 0x0, 0x0, 0x16)
    OP_43(0x1C, 0x0, 0x0, 0x17)
    OP_43(0x27, 0x0, 0x0, 0x18)
    OP_43(0x14, 0x0, 0x0, 0xF)
    OP_43(0x15, 0x0, 0x0, 0xF)
    OP_43(0x16, 0x0, 0x0, 0xF)
    OP_43(0x17, 0x0, 0x0, 0xF)
    OP_43(0x18, 0x0, 0x0, 0xF)
    OP_43(0x19, 0x0, 0x0, 0xF)
    OP_0D()
    SetChrPos(0x21, 2350, 3160, 57030, 180)
    SetChrPos(0x1D, 3580, 3160, 57630, 180)
    Sleep(1500)
    OP_43(0x109, 0x0, 0x0, 0xC)
    OP_43(0x10F, 0x0, 0x0, 0xD)
    OP_43(0x13, 0x0, 0x0, 0xE)
    Sleep(1500)
    Fade(500)
    OP_6D(-2170, 3160, 61480, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(315000, 0)
    OP_6E(387, 0)
    OP_44(0xEE, 0x3)

    def lambda_59FC():
        OP_6D(0, 6360, 63260, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_59FC)

    def lambda_5A14():
        OP_67(0, 3170, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5A14)

    def lambda_5A2C():
        OP_6B(3280, 6000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5A2C)

    def lambda_5A3C():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5A3C)

    def lambda_5A4C():
        OP_6E(432, 6000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_5A4C)
    WaitChrThread(0xEE, 0x1)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    OP_22(0x85, 0x1, 0x64)
    OP_6F(0x0, 90)
    OP_70(0x0, 0x0)
    WaitChrThread(0xEE, 0x1)
    FadeToBright(2000, 16777215)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0xB)
    WaitChrThread(0x109, 0x0)
    OP_44(0x21, 0x0)
    OP_44(0x1A, 0x0)
    OP_44(0x1D, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_44(0x26, 0x0)
    OP_44(0x1E, 0x0)
    OP_44(0x28, 0x0)
    OP_44(0x1B, 0x0)
    OP_44(0x25, 0x0)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x1C, 0x0)
    OP_44(0x27, 0x0)
    OP_44(0x1F, 0x3)
    OP_44(0x24, 0x3)
    OP_44(0x21, 0x0)
    OP_44(0x1A, 0x0)
    OP_44(0x1D, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    OP_44(0x18, 0x0)
    OP_44(0x19, 0x0)
    OP_73(0x0)
    OP_23(0x85)
    OP_22(0x88, 0x0, 0x64)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_20(0x7D0)
    OP_21()
    Sleep(4000)
    OP_A2(0x2C0F)
    OP_AA(65281)
    OP_AD(0x2400F3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_5B93")

    label("loc_5B93")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BA7")
    ShowSaveMenu()

    label("loc_5BA7")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2506)
    OP_A2(0x2507)
    NewScene("ED6_DT21/U7000   ._SN", 104, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_10_3958 end

    def Function_11_5BF3(): pass

    label("Function_11_5BF3")

    ClearMapFlags(0x100000)
    OP_24(0x17B, 0x5A)
    OP_24(0x151, 0x5A)
    OP_24(0x21A, 0x5A)
    OP_24(0x1F4, 0x5A)
    OP_24(0x1F5, 0x5A)
    OP_24(0x1FD, 0x5A)
    OP_24(0x1F8, 0x5A)
    OP_24(0x1F9, 0x5A)
    OP_24(0x1F7, 0x5A)
    OP_24(0x1FA, 0x5A)
    OP_24(0x20E, 0x5A)
    OP_24(0x1FE, 0x5A)
    OP_24(0x1FE, 0x5A)
    Sleep(200)
    OP_24(0x17B, 0x50)
    OP_24(0x151, 0x50)
    OP_24(0x21A, 0x50)
    OP_24(0x1F4, 0x50)
    OP_24(0x1F5, 0x50)
    OP_24(0x1FD, 0x50)
    OP_24(0x1F8, 0x50)
    OP_24(0x1F9, 0x50)
    OP_24(0x1F7, 0x50)
    OP_24(0x1FA, 0x50)
    OP_24(0x20E, 0x50)
    OP_24(0x1FE, 0x50)
    OP_24(0x1FE, 0x50)
    Sleep(200)
    OP_24(0x17B, 0x46)
    OP_24(0x151, 0x46)
    OP_24(0x21A, 0x46)
    OP_24(0x1F4, 0x46)
    OP_24(0x1F5, 0x46)
    OP_24(0x1FD, 0x46)
    OP_24(0x1F8, 0x46)
    OP_24(0x1F9, 0x46)
    OP_24(0x1F7, 0x46)
    OP_24(0x1FA, 0x46)
    OP_24(0x20E, 0x46)
    OP_24(0x1FE, 0x46)
    OP_24(0x1FE, 0x46)
    Sleep(200)
    OP_24(0x17B, 0x3C)
    OP_24(0x151, 0x3C)
    OP_24(0x21A, 0x3C)
    OP_24(0x1F4, 0x3C)
    OP_24(0x1F5, 0x3C)
    OP_24(0x1FD, 0x3C)
    OP_24(0x1F8, 0x3C)
    OP_24(0x1F9, 0x3C)
    OP_24(0x1F7, 0x3C)
    OP_24(0x1FA, 0x3C)
    OP_24(0x20E, 0x3C)
    OP_24(0x1FE, 0x3C)
    OP_24(0x1FE, 0x3C)
    Sleep(200)
    OP_24(0x17B, 0x32)
    OP_24(0x151, 0x32)
    OP_24(0x21A, 0x32)
    OP_24(0x1F4, 0x32)
    OP_24(0x1F5, 0x32)
    OP_24(0x1FD, 0x32)
    OP_24(0x1F8, 0x32)
    OP_24(0x1F9, 0x32)
    OP_24(0x1F7, 0x32)
    OP_24(0x1FA, 0x32)
    OP_24(0x20E, 0x32)
    OP_24(0x1FE, 0x32)
    OP_24(0x1FE, 0x32)
    Sleep(200)
    OP_24(0x17B, 0x28)
    OP_24(0x151, 0x28)
    OP_24(0x21A, 0x28)
    OP_24(0x1F4, 0x28)
    OP_24(0x1F5, 0x28)
    OP_24(0x1FD, 0x28)
    OP_24(0x1F8, 0x28)
    OP_24(0x1F9, 0x28)
    OP_24(0x1F7, 0x28)
    OP_24(0x1FA, 0x28)
    OP_24(0x20E, 0x28)
    OP_24(0x1FE, 0x28)
    OP_24(0x1FE, 0x28)
    Sleep(200)
    OP_24(0x17B, 0x1E)
    OP_24(0x151, 0x1E)
    OP_24(0x21A, 0x1E)
    OP_24(0x1F4, 0x1E)
    OP_24(0x1F5, 0x1E)
    OP_24(0x1FD, 0x1E)
    OP_24(0x1F8, 0x1E)
    OP_24(0x1F9, 0x1E)
    OP_24(0x1F7, 0x1E)
    OP_24(0x1FA, 0x1E)
    OP_24(0x20E, 0x1E)
    OP_24(0x1FE, 0x1E)
    OP_24(0x1FE, 0x1E)
    Sleep(200)
    OP_24(0x17B, 0x14)
    OP_24(0x151, 0x14)
    OP_24(0x21A, 0x14)
    OP_24(0x1F4, 0x14)
    OP_24(0x1F5, 0x14)
    OP_24(0x1FD, 0x14)
    OP_24(0x1F8, 0x14)
    OP_24(0x1F9, 0x14)
    OP_24(0x1F7, 0x14)
    OP_24(0x1FA, 0x14)
    OP_24(0x20E, 0x14)
    OP_24(0x1FE, 0x14)
    OP_24(0x1FE, 0x14)
    Sleep(200)
    OP_24(0x17B, 0xA)
    OP_24(0x151, 0xA)
    OP_24(0x21A, 0xA)
    OP_24(0x1F4, 0xA)
    OP_24(0x1F5, 0xA)
    OP_24(0x1FD, 0xA)
    OP_24(0x1F8, 0xA)
    OP_24(0x1F9, 0xA)
    OP_24(0x1F7, 0xA)
    OP_24(0x1FA, 0xA)
    OP_24(0x20E, 0xA)
    OP_24(0x1FE, 0xA)
    OP_24(0x1FE, 0xA)
    Sleep(200)
    OP_24(0x17B, 0x0)
    OP_24(0x151, 0x0)
    OP_24(0x21A, 0x0)
    OP_24(0x1F4, 0x0)
    OP_24(0x1F5, 0x0)
    OP_24(0x1FD, 0x0)
    OP_24(0x1F8, 0x0)
    OP_24(0x1F9, 0x0)
    OP_24(0x1F7, 0x0)
    OP_24(0x1FA, 0x0)
    OP_24(0x20E, 0x0)
    OP_24(0x1FE, 0x0)
    OP_24(0x1FE, 0x0)
    OP_23(0x17B)
    OP_23(0x151)
    OP_23(0x21A)
    OP_23(0x1F4)
    OP_23(0x1F5)
    OP_23(0x1FD)
    OP_23(0x1F8)
    OP_23(0x1F9)
    OP_23(0x1F7)
    OP_23(0x1FA)
    OP_23(0x20E)
    OP_23(0x1FE)
    OP_23(0x1FE)
    Return()

    # Function_11_5BF3 end

    def Function_12_5E55(): pass

    label("Function_12_5E55")

    OP_8E(0xFE, 0xFFFFF394, 0x488, 0xA0AA, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFFE52, 0x488, 0xC1E8, 0x1770, 0x0)
    OP_8E(0xFE, 0x1A4, 0xC58, 0xDB38, 0x1770, 0x0)
    OP_8E(0xFE, 0x1A4, 0xC58, 0xFF6E, 0x1770, 0x0)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFFBBE, 0xC58, 0x10B26, 0x1770, 0x0)
    Return()

    # Function_12_5E55 end

    def Function_13_5EBF(): pass

    label("Function_13_5EBF")

    Sleep(500)
    OP_8E(0xFE, 0xA96, 0x488, 0xA186, 0x1770, 0x0)
    OP_8E(0xFE, 0x3E8, 0x488, 0xC300, 0x1770, 0x0)
    OP_8E(0xFE, 0x1A4, 0xC58, 0xDB38, 0x1770, 0x0)
    OP_8E(0xFE, 0x1A4, 0xC58, 0xFF3C, 0x1770, 0x0)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x1A4, 0xC58, 0x10AF4, 0x1770, 0x0)
    Return()

    # Function_13_5EBF end

    def Function_14_5F2E(): pass

    label("Function_14_5F2E")

    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xA96, 0x488, 0xA186, 0x1770, 0x0)
    OP_8E(0xFE, 0x3E8, 0x488, 0xC300, 0x1770, 0x0)
    OP_8E(0xFE, 0x1A4, 0xC58, 0xDB38, 0x1770, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0x1A4, 0xC58, 0xFF3C, 0x1770, 0x0)
    OP_22(0x99, 0x0, 0x64)
    OP_8E(0xFE, 0x1A4, 0xC58, 0x10AF4, 0x1770, 0x0)
    Return()

    # Function_14_5F2E end

    def Function_15_5FC1(): pass

    label("Function_15_5FC1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61BE")
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6024")
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 1)
    OP_22(0x151, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)

    def lambda_600F():

        label("loc_600F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_600F")

    QueueWorkItem2(0xFE, 3, lambda_600F)
    Sleep(500)
    Jump("loc_61BB")

    label("loc_6024")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_607C")
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_22(0x21A, 0x0, 0x64)
    OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)

    def lambda_6067():

        label("loc_6067")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6067")

    QueueWorkItem2(0xFE, 3, lambda_6067)
    Sleep(500)
    Jump("loc_61BB")

    label("loc_607C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60C5")
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 1)
    OP_22(0x151, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)

    def lambda_60B0():

        label("loc_60B0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_60B0")

    QueueWorkItem2(0xFE, 3, lambda_60B0)
    Sleep(1000)
    Jump("loc_61BB")

    label("loc_60C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_611D")
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_22(0x21A, 0x0, 0x64)
    OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)

    def lambda_6108():

        label("loc_6108")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6108")

    QueueWorkItem2(0xFE, 3, lambda_6108)
    Sleep(1000)
    Jump("loc_61BB")

    label("loc_611D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6166")
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 1)
    OP_22(0x151, 0x0, 0x64)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)

    def lambda_6151():

        label("loc_6151")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6151")

    QueueWorkItem2(0xFE, 3, lambda_6151)
    Sleep(1500)
    Jump("loc_61BB")

    label("loc_6166")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61BB")
    OP_44(0xFE, 0x3)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_22(0x21A, 0x0, 0x64)
    OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)

    def lambda_61A9():

        label("loc_61A9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_61A9")

    QueueWorkItem2(0xFE, 3, lambda_61A9)
    Sleep(1500)

    label("loc_61BB")

    Jump("Function_15_5FC1")

    label("loc_61BE")

    Return()

    # Function_15_5FC1 end

    def Function_16_61BF(): pass

    label("Function_16_61BF")

    SetChrPos(0xFE, -790, 1160, 42390, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)

    def lambda_61EF():

        label("loc_61EF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_61EF")

    QueueWorkItem2(0xFE, 3, lambda_61EF)

    label("loc_61FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6212")
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_61FC")

    label("loc_6212")

    Return()

    # Function_16_61BF end

    def Function_17_6213(): pass

    label("Function_17_6213")

    SetChrPos(0xFE, 960, 1160, 43000, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x3C0, 0x488, 0xA410, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)

    def lambda_625E():

        label("loc_625E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_625E")

    QueueWorkItem2(0xFE, 3, lambda_625E)

    label("loc_626B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6281")
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_626B")

    label("loc_6281")

    Return()

    # Function_17_6213 end

    def Function_18_6282(): pass

    label("Function_18_6282")

    SetChrPos(0xFE, 10, 1160, 50100, 180)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFFF92, 0x488, 0xB4DC, 0x1388, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_62CB():
        OP_96(0xFE, 0xFFFFFFCE, 0x960, 0xA136, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_62CB)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_6307():
        OP_96(0xFE, 0x5A, 0x488, 0x828C, 0x7D0, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6307)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x3, 0x5DC)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x29, 13)
    OP_22(0x202, 0x0, 0x64)
    SetChrSubChip(0x29, 0)
    SetChrPos(0x29, 60, 2160, 31980, 0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x2)

    def lambda_637B():

        label("loc_637B")

        OP_99(0xFE, 0x78, 0x7F, 0xBB8)
        OP_48()
        Jump("loc_637B")

    QueueWorkItem2(0x29, 3, lambda_637B)

    def lambda_638E():
        OP_8F(0xFE, 0x0, 0x870, 0x39C6, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 0, lambda_638E)
    OP_99(0xFE, 0x4, 0xD, 0x5DC)
    OP_22(0x1FD, 0x0, 0x64)
    Return()

    # Function_18_6282 end

    def Function_19_63B2(): pass

    label("Function_19_63B2")

    SetChrPos(0xFE, -3730, 1160, 42380, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFEE4E, 0x488, 0x9A74, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 33)
    SetChrSubChip(0xFE, 0)
    OP_22(0x1F8, 0x0, 0x64)

    def lambda_63FB():

        label("loc_63FB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_63FB")

    QueueWorkItem2(0xFE, 3, lambda_63FB)

    label("loc_6408")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_641E")
    OP_22(0x1F8, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_6408")

    label("loc_641E")

    Return()

    # Function_19_63B2 end

    def Function_20_641F(): pass

    label("Function_20_641F")

    SetChrPos(0xFE, -5990, 1160, 40280, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFE89A, 0x488, 0x9970, 0x1388, 0x0)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)

    def lambda_646A():

        label("loc_646A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_646A")

    QueueWorkItem2(0xFE, 3, lambda_646A)

    label("loc_6477")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_648D")
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_6477")

    label("loc_648D")

    Return()

    # Function_20_641F end

    def Function_21_648E(): pass

    label("Function_21_648E")

    SetChrPos(0xFE, -2270, 1160, 37260, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF254, 0x488, 0x8408, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)

    def lambda_64D2():

        label("loc_64D2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_64D2")

    QueueWorkItem2(0xFE, 3, lambda_64D2)

    label("loc_64DF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64F5")
    OP_22(0x1FB, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_64DF")

    label("loc_64F5")

    Return()

    # Function_21_648E end

    def Function_22_64F6(): pass

    label("Function_22_64F6")

    SetChrPos(0xFE, 3740, 1160, 41020, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xE9C, 0x488, 0x9D80, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)

    def lambda_653A():

        label("loc_653A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_653A")

    QueueWorkItem2(0xFE, 3, lambda_653A)

    label("loc_6547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_655D")
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_6547")

    label("loc_655D")

    Return()

    # Function_22_64F6 end

    def Function_23_655E(): pass

    label("Function_23_655E")

    SetChrPos(0xFE, 7300, 1160, 38770, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x1914, 0x488, 0x88B8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 0)

    def lambda_65A2():

        label("loc_65A2")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_65A2")

    QueueWorkItem2(0xFE, 3, lambda_65A2)

    label("loc_65AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65C5")
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_65AF")

    label("loc_65C5")

    Return()

    # Function_23_655E end

    def Function_24_65C6(): pass

    label("Function_24_65C6")

    SetChrPos(0xFE, 5360, 1160, 43890, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 32)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x157C, 0x488, 0x9D12, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)

    def lambda_660A():

        label("loc_660A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_660A")

    QueueWorkItem2(0xFE, 3, lambda_660A)

    label("loc_6617")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_662D")
    OP_22(0x1F5, 0x0, 0x64)
    Sleep(1500)
    Jump("loc_6617")

    label("loc_662D")

    Return()

    # Function_24_65C6 end

    def Function_25_662E(): pass

    label("Function_25_662E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_684C")
    SetChrSubChip(0xFE, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 0, 1100, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x1, 0x7, 0xA28)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66DA")
    PlayEffect(0x3, 0xFF, 0x14, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_6849")

    label("loc_66DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6724")
    PlayEffect(0x3, 0xFF, 0x15, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_6849")

    label("loc_6724")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_676E")
    PlayEffect(0x3, 0xFF, 0x16, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_6849")

    label("loc_676E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B8")
    PlayEffect(0x3, 0xFF, 0x17, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_6849")

    label("loc_67B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6802")
    PlayEffect(0x3, 0xFF, 0x18, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_6849")

    label("loc_6802")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6849")
    PlayEffect(0x3, 0xFF, 0x19, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_6849")

    Jump("Function_25_662E")

    label("loc_684C")

    Return()

    # Function_25_662E end

    def Function_26_684D(): pass

    label("Function_26_684D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A6F")
    OP_99(0xFE, 0x0, 0x2, 0xA28)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x3, 0x7, 0xA28)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68FD")
    PlayEffect(0x3, 0xFF, 0x14, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_6A6C")

    label("loc_68FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6947")
    PlayEffect(0x3, 0xFF, 0x15, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_6A6C")

    label("loc_6947")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6991")
    PlayEffect(0x3, 0xFF, 0x16, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_6A6C")

    label("loc_6991")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69DB")
    PlayEffect(0x3, 0xFF, 0x17, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_6A6C")

    label("loc_69DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A25")
    PlayEffect(0x3, 0xFF, 0x18, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_6A6C")

    label("loc_6A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A6C")
    PlayEffect(0x3, 0xFF, 0x19, 200, 1300, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_6A6C")

    Jump("Function_26_684D")

    label("loc_6A6F")

    Return()

    # Function_26_684D end

    def Function_27_6A70(): pass

    label("Function_27_6A70")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6C84")
    PlayEffect(0x1, 0xFF, 0xFE, 0, 800, 900, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x1, 0xD, 0x5DC)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B12")
    PlayEffect(0x4, 0xFF, 0x14, 0, 800, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_6C81")

    label("loc_6B12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5C")
    PlayEffect(0x4, 0xFF, 0x15, 0, 800, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_6C81")

    label("loc_6B5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BA6")
    PlayEffect(0x4, 0xFF, 0x16, 0, 800, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_6C81")

    label("loc_6BA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BF0")
    PlayEffect(0x4, 0xFF, 0x17, 0, 800, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_6C81")

    label("loc_6BF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C3A")
    PlayEffect(0x4, 0xFF, 0x18, 0, 800, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_6C81")

    label("loc_6C3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C81")
    PlayEffect(0x4, 0xFF, 0x19, 0, 800, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_6C81")

    Jump("Function_27_6A70")

    label("loc_6C84")

    Return()

    # Function_27_6A70 end

    def Function_28_6C85(): pass

    label("Function_28_6C85")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EA3")
    SetChrSubChip(0xFE, 0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 1000, 600, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x1, 0x7, 0xA28)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D31")
    PlayEffect(0x3, 0xFF, 0x14, -200, 1100, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("loc_6EA0")

    label("loc_6D31")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7B")
    PlayEffect(0x3, 0xFF, 0x15, -200, 1100, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jump("loc_6EA0")

    label("loc_6D7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC5")
    PlayEffect(0x3, 0xFF, 0x16, -200, 1100, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    Jump("loc_6EA0")

    label("loc_6DC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E0F")
    PlayEffect(0x3, 0xFF, 0x17, -200, 1100, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    Jump("loc_6EA0")

    label("loc_6E0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E59")
    PlayEffect(0x3, 0xFF, 0x18, -200, 1100, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    Jump("loc_6EA0")

    label("loc_6E59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EA0")
    PlayEffect(0x3, 0xFF, 0x19, -200, 1100, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    label("loc_6EA0")

    Jump("Function_28_6C85")

    label("loc_6EA3")

    Return()

    # Function_28_6C85 end

    def Function_29_6EA4(): pass

    label("Function_29_6EA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F88")
    OP_99(0xFE, 0x0, 0x2, 0xA28)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 1000, 500, -100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x3, 0x7, 0xA28)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F1F")
    Sleep(500)
    Jump("loc_6F85")

    label("loc_6F1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F34")
    Sleep(600)
    Jump("loc_6F85")

    label("loc_6F34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F49")
    Sleep(700)
    Jump("loc_6F85")

    label("loc_6F49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F5E")
    Sleep(800)
    Jump("loc_6F85")

    label("loc_6F5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F73")
    Sleep(900)
    Jump("loc_6F85")

    label("loc_6F73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F85")
    Sleep(1000)

    label("loc_6F85")

    Jump("Function_29_6EA4")

    label("loc_6F88")

    Return()

    # Function_29_6EA4 end

    def Function_30_6F89(): pass

    label("Function_30_6F89")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_705A")
    PlayEffect(0x1, 0xFF, 0xFE, 0, 800, 900, 0, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0xFE, 0x1, 0xD, 0x5DC)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF1")
    Sleep(500)
    Jump("loc_7057")

    label("loc_6FF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7006")
    Sleep(600)
    Jump("loc_7057")

    label("loc_7006")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_701B")
    Sleep(700)
    Jump("loc_7057")

    label("loc_701B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7030")
    Sleep(800)
    Jump("loc_7057")

    label("loc_7030")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7045")
    Sleep(900)
    Jump("loc_7057")

    label("loc_7045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7057")
    Sleep(1000)

    label("loc_7057")

    Jump("Function_30_6F89")

    label("loc_705A")

    Return()

    # Function_30_6F89 end

    def Function_31_705B(): pass

    label("Function_31_705B")

    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFFE16, 0x488, 0x9F9C, 0x1388, 0x0)
    Return()

    # Function_31_705B end

    def Function_32_707A(): pass

    label("Function_32_707A")

    Sleep(100)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x5AA, 0x488, 0xA3CA, 0x1388, 0x0)
    Return()

    # Function_32_707A end

    def Function_33_709E(): pass

    label("Function_33_709E")

    Sleep(500)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x49C, 0x488, 0x9CF4, 0x1388, 0x0)
    Return()

    # Function_33_709E end

    def Function_34_70C2(): pass

    label("Function_34_70C2")

    Sleep(600)
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF902, 0xC58, 0xE0BA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFFDA8, 0xC58, 0xDA7A, 0x1388, 0x0)
    OP_8E(0xFE, 0x1C2, 0x488, 0x9DBC, 0x1388, 0x0)
    Return()

    # Function_34_70C2 end

    def Function_35_710E(): pass

    label("Function_35_710E")

    SetChrFlags(0xFE, 0x4)
    Sleep(300)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF8DA, 0xC58, 0xDE44, 0x1388, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_7146():
        OP_96(0xFE, 0xFFFFF7EA, 0xDAC, 0xD7D2, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7146)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 7)

    def lambda_7182():
        OP_96(0xFE, 0xFFFFF13C, 0x488, 0xC5A8, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7182)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8F(0xFE, 0xFFFFEEE4, 0x488, 0xB180, 0x1388, 0x0)
    Return()

    # Function_35_710E end

    def Function_36_71B9(): pass

    label("Function_36_71B9")

    Sleep(800)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0xC8, 0xC58, 0xE60A, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xC8, 0x488, 0x9DBC, 0x1388, 0x0)
    Return()

    # Function_36_71B9 end

    def Function_37_71F8(): pass

    label("Function_37_71F8")

    SetChrFlags(0xFE, 0x4)
    Sleep(200)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_721C():
        OP_96(0xFE, 0x8F2, 0xDAC, 0xD836, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_721C)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_7258():
        OP_96(0xFE, 0xEF6, 0x488, 0xC33C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7258)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    OP_8F(0xFE, 0x1C2, 0x488, 0x9DBC, 0x1388, 0x0)
    Return()

    # Function_37_71F8 end

    def Function_38_7294(): pass

    label("Function_38_7294")

    SetChrFlags(0xFE, 0x4)
    Sleep(700)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xB5E, 0xC58, 0xE146, 0x1388, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_72CC():
        OP_96(0xFE, 0x12CA, 0x488, 0xC396, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72CC)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    OP_8F(0xFE, 0x1810, 0x488, 0xAB36, 0x1388, 0x0)
    Return()

    # Function_38_7294 end

    def Function_39_7308(): pass

    label("Function_39_7308")

    SetChrFlags(0xFE, 0x4)
    Sleep(400)
    SetChrChipByIndex(0xFE, 32)
    SetChrSubChip(0xFE, 0)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 2)

    def lambda_732C():
        OP_96(0xFE, 0x113A, 0x488, 0xCAA8, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_732C)
    WaitChrThread(0xFE, 0x1)
    SetChrSubChip(0xFE, 5)
    OP_22(0xA4, 0x0, 0x64)
    OP_8F(0xFE, 0x1C2, 0x488, 0x9DBC, 0x1388, 0x0)
    Return()

    # Function_39_7308 end

    def Function_40_7368(): pass

    label("Function_40_7368")

    OP_22(0x99, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -590, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFFD76, 0xC58, 0xDDB8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_40_7368 end

    def Function_41_73AC(): pass

    label("Function_41_73AC")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 690, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x30C, 0xC58, 0xDEC6, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_41_73AC end

    def Function_42_73EB(): pass

    label("Function_42_73EB")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1890, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF880, 0xC58, 0xE86C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFF330, 0xC58, 0xE4FC, 0x1388, 0x0)
    OP_8C(0xFE, 180, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_42_73EB end

    def Function_43_7445(): pass

    label("Function_43_7445")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1290, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 16)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x4B0, 0xC58, 0xE4FC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_43_7445 end

    def Function_44_7484(): pass

    label("Function_44_7484")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1190, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFFBAA, 0xC58, 0xE650, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 17)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_44_7484 end

    def Function_45_74C3(): pass

    label("Function_45_74C3")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1300, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF92A, 0xC58, 0xE178, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 35)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_45_74C3 end

    def Function_46_7502(): pass

    label("Function_46_7502")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1890, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF830, 0xC58, 0xF2D0, 0x1388, 0x0)
    OP_8F(0xFE, 0xFFFFF524, 0xC58, 0xDF48, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_46_7502 end

    def Function_47_7555(): pass

    label("Function_47_7555")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -890, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 24)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFFCCC, 0xC58, 0xECF4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_47_7555 end

    def Function_48_7594(): pass

    label("Function_48_7594")

    OP_22(0x99, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 890, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x334, 0xC58, 0xEE2A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_48_7594 end

    def Function_49_75D8(): pass

    label("Function_49_75D8")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1690, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 28)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x83E, 0xC58, 0xE006, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_49_75D8 end

    def Function_50_7617(): pass

    label("Function_50_7617")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1890, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 30)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x834, 0xC58, 0xEA9C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_50_7617 end

    def Function_51_7656(): pass

    label("Function_51_7656")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -1800, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 34)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0xFFFFF7A4, 0xC58, 0xE97A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 33)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_51_7656 end

    def Function_52_7695(): pass

    label("Function_52_7695")

    OP_22(0x99, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 1800, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 32)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x834, 0xC58, 0xE9CA, 0x1388, 0x0)
    OP_8F(0xFE, 0xCD0, 0xC58, 0xE1B4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_52_7695 end

    def Function_53_76ED(): pass

    label("Function_53_76ED")

    OP_22(0x99, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, 3150, 67540, 180)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x28, 0xC58, 0xE2E0, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_53_76ED end

    def Function_54_7731(): pass

    label("Function_54_7731")

    Sleep(1400)
    SetChrFlags(0xFE, 0x20)
    OP_91(0xFE, 0xC8, 0x0, 0x12C, 0x1F4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_54_7731 end

    def Function_55_7755(): pass

    label("Function_55_7755")

    Sleep(1200)
    SetChrFlags(0xFE, 0x20)
    OP_91(0xFE, 0xFFFFFF38, 0x0, 0x0, 0x1F4, 0x0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_55_7755 end

    def Function_56_7779(): pass

    label("Function_56_7779")

    Sleep(1000)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_91(0xFE, 0x0, 0x0, 0x1F4, 0x1F4, 0x0)
    Return()

    # Function_56_7779 end

    def Function_57_77A5(): pass

    label("Function_57_77A5")

    Sleep(300)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFCE0, 0x190, 0x0)
    Return()

    # Function_57_77A5 end

    def Function_58_77BF(): pass

    label("Function_58_77BF")

    Sleep(100)
    OP_91(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFFCE0, 0x190, 0x0)
    Return()

    # Function_58_77BF end

    def Function_59_77D9(): pass

    label("Function_59_77D9")

    Sleep(600)
    OP_91(0xFE, 0xFFFFFC18, 0x0, 0x1F4, 0x190, 0x0)
    Return()

    # Function_59_77D9 end

    def Function_60_77F3(): pass

    label("Function_60_77F3")

    Sleep(200)
    OP_91(0xFE, 0x258, 0x0, 0x5DC, 0x190, 0x0)
    Return()

    # Function_60_77F3 end

    def Function_61_780D(): pass

    label("Function_61_780D")

    Sleep(700)
    OP_91(0xFE, 0x3E8, 0x0, 0x3E8, 0x190, 0x0)
    Return()

    # Function_61_780D end

    def Function_62_7827(): pass

    label("Function_62_7827")

    Sleep(1000)
    OP_91(0xFE, 0x384, 0x0, 0xFFFFFDA8, 0x1F4, 0x0)
    Return()

    # Function_62_7827 end

    def Function_63_7841(): pass

    label("Function_63_7841")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x800)
    SetChrPos(0xFE, 30, 20300, 42000, 180)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 1)

    def lambda_7872():

        label("loc_7872")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_7872")

    QueueWorkItem2(0xFE, 3, lambda_7872)
    OP_91(0xFE, 0x0, 0xFFFFB5C8, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xC1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_63_7841 end

    def Function_64_78AF(): pass

    label("Function_64_78AF")

    Sleep(1000)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x800)
    SetChrPos(0xFE, 5500, 20300, 39600, 225)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 1)

    def lambda_78E5():

        label("loc_78E5")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_78E5")

    QueueWorkItem2(0xFE, 3, lambda_78E5)
    OP_91(0xFE, 0x0, 0xFFFFB5C8, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xC1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_64_78AF end

    def Function_65_7922(): pass

    label("Function_65_7922")

    Sleep(700)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x800)
    SetChrPos(0xFE, 7000, 20300, 33000, 270)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 1)

    def lambda_7958():

        label("loc_7958")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_7958")

    QueueWorkItem2(0xFE, 3, lambda_7958)
    OP_91(0xFE, 0x0, 0xFFFFB5C8, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xC1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_65_7922 end

    def Function_66_7995(): pass

    label("Function_66_7995")

    Sleep(300)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x800)
    SetChrPos(0xFE, 240, 20300, 28450, 0)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 1)

    def lambda_79CB():

        label("loc_79CB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_79CB")

    QueueWorkItem2(0xFE, 3, lambda_79CB)
    OP_91(0xFE, 0x0, 0xFFFFB5C8, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xC1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_66_7995 end

    def Function_67_7A08(): pass

    label("Function_67_7A08")

    Sleep(600)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x800)
    SetChrPos(0xFE, -3820, 20300, 31500, 45)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 1)

    def lambda_7A3E():

        label("loc_7A3E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_7A3E")

    QueueWorkItem2(0xFE, 3, lambda_7A3E)
    OP_91(0xFE, 0x0, 0xFFFFB5C8, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xC1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_67_7A08 end

    def Function_68_7A7B(): pass

    label("Function_68_7A7B")

    Sleep(1200)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x800)
    SetChrPos(0xFE, -4800, 20300, 38340, 135)
    OP_51(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 1)

    def lambda_7AB1():

        label("loc_7AB1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_7AB1")

    QueueWorkItem2(0xFE, 3, lambda_7AB1)
    OP_91(0xFE, 0x0, 0xFFFFB5C8, 0x0, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xC1, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    Return()

    # Function_68_7A7B end

    def Function_69_7AEE(): pass

    label("Function_69_7AEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B04")
    OP_22(0x120, 0x0, 0x3C)
    Sleep(800)
    Jump("Function_69_7AEE")

    label("loc_7B04")

    Return()

    # Function_69_7AEE end

    def Function_70_7B05(): pass

    label("Function_70_7B05")

    SetChrChipByIndex(0xFE, 4)
    OP_8F(0xFE, 0xC8, 0x488, 0x79AE, 0x1F40, 0x0)
    SetChrFlags(0xFE, 0x800)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 2)
    SetChrSubChip(0xFE, 0)
    OP_22(0x19E, 0x0, 0x64)

    def lambda_7B3D():
        OP_96(0xFE, 0xD2, 0x488, 0x805C, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B3D)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x228, 0x0, 0x64)
    OP_43(0xFE, 0x2, 0x0, 0x47)
    OP_8F(0xFE, 0xAA, 0x488, 0x8638, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x20)
    OP_43(0xFE, 0x3, 0x0, 0x48)
    OP_44(0xFE, 0x2)
    Return()

    # Function_70_7B05 end

    def Function_71_7B8B(): pass

    label("Function_71_7B8B")

    PlayEffect(0x1, 0x0, 0xFE, 0, 0, -800, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x1, 0xFE, 0, 0, -800, 0, 0, 0, 1900, 1900, 1900, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x2, 0xFE, 0, 0, -800, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x3, 0xFE, 0, 0, -800, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x4, 0xFE, 0, 0, -800, 0, 0, 0, 1600, 1600, 1600, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0x5, 0xFE, 0, 0, -800, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_71_7B8B end

    def Function_72_7CE3(): pass

    label("Function_72_7CE3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D1F")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_72_7CE3")

    label("loc_7D1F")

    Return()

    # Function_72_7CE3 end

    def Function_73_7D20(): pass

    label("Function_73_7D20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D42")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x64, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("Function_73_7D20")

    label("loc_7D42")

    Return()

    # Function_73_7D20 end

    def Function_74_7D43(): pass

    label("Function_74_7D43")

    OP_24(0x137, 0x50)
    OP_24(0x32E, 0x50)
    Sleep(300)
    OP_24(0x137, 0x46)
    OP_24(0x32E, 0x46)
    Sleep(300)
    OP_24(0x137, 0x3C)
    OP_24(0x32E, 0x3C)
    Sleep(300)
    OP_24(0x137, 0x32)
    OP_24(0x32E, 0x32)
    Sleep(300)
    OP_24(0x137, 0x28)
    OP_24(0x32E, 0x28)
    Sleep(300)
    OP_24(0x137, 0x1E)
    OP_24(0x32E, 0x1E)
    Sleep(300)
    OP_24(0x137, 0x14)
    OP_24(0x32E, 0x14)
    Sleep(300)
    OP_24(0x137, 0xA)
    OP_24(0x32E, 0xA)
    Sleep(300)
    OP_24(0x137, 0x0)
    OP_24(0x32E, 0x0)
    OP_23(0x137)
    OP_23(0x32E)
    Return()

    # Function_74_7D43 end

    SaveToFile()

Try(main)
