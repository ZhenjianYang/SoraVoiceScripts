from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1132   ._SN',
        MapName             = 'Bose',
        Location            = 'T1132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 12,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1132_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '巴雷里奥',                             # 9
        '蒂娜',                                 # 10
        '达维尔大使',                           # 11
        '杰拉尔德',                             # 12
        '杰拉尔德',                             # 13
        '巴克雷书记官',                         # 14
        '巴克',                                 # 15
        '德拉多',                               # 16
        '普蕾沙',                               # 17
        '波波',                                 # 18
        '思潘斯老人',                           # 19
        '米蕾婆婆',                             # 20
        '里布罗',                               # 21
        '艾米',                                 # 22
        '哈尔德',                               # 23
        '罗亚',                                 # 24
        '提克',                                 # 25
        '莫莉',                                 # 26
        '赛希莉亚号乘客',                       # 27
        '赛希莉亚号乘客',                       # 28
        '赛希莉亚号乘客',                       # 29
        '赛希莉亚号乘客',                       # 30
        '目标用照相机',                         # 31
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


    AddCharChip(
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01350 ._CH',             # 01
        'ED6_DT27/CH03710 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01560 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01040 ._CH',             # 06
        'ED6_DT07/CH01130 ._CH',             # 07
        'ED6_DT07/CH01060 ._CH',             # 08
        'ED6_DT07/CH01000 ._CH',             # 09
        'ED6_DT07/CH01010 ._CH',             # 0A
        'ED6_DT07/CH01050 ._CH',             # 0B
        'ED6_DT07/CH01120 ._CH',             # 0C
        'ED6_DT07/CH01020 ._CH',             # 0D
        'ED6_DT07/CH01170 ._CH',             # 0E
        'ED6_DT07/CH01460 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01350P._CP',             # 01
        'ED6_DT27/CH03710P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01560P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01040P._CP',             # 06
        'ED6_DT07/CH01130P._CP',             # 07
        'ED6_DT07/CH01060P._CP',             # 08
        'ED6_DT07/CH01000P._CP',             # 09
        'ED6_DT07/CH01010P._CP',             # 0A
        'ED6_DT07/CH01050P._CP',             # 0B
        'ED6_DT07/CH01120P._CP',             # 0C
        'ED6_DT07/CH01020P._CP',             # 0D
        'ED6_DT07/CH01170P._CP',             # 0E
        'ED6_DT07/CH01460P._CP',             # 0F
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -49910,
        Z                   = 0,
        Y                   = 118350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -122680,
        Z                   = 0,
        Y                   = 179240,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -126260,
        Z                   = 0,
        Y                   = 138000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -127460,
        Z                   = 0,
        Y                   = 181340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -123490,
        Z                   = 0,
        Y                   = 178400,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -85120,
        Z                   = 0,
        Y                   = 121590,
        Direction           = 130,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -86580,
        Z                   = 0,
        Y                   = 119500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -45690,
        Z                   = 0,
        Y                   = 152320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -48210,
        Z                   = 0,
        Y                   = 155300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -49050,
        Z                   = 0,
        Y                   = 120240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -85770,
        Z                   = 0,
        Y                   = 152520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -85280,
        Z                   = 0,
        Y                   = 153820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 182260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 6470,
        Z                   = 0,
        Y                   = 191180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -45610,
        Z                   = 0,
        Y                   = 153280,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = -88500,
        Z                   = 0,
        Y                   = 122920,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -84260,
        Z                   = 0,
        Y                   = 119710,
        Direction           = 291,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = -49680,
        Z                   = 0,
        Y                   = 119810,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -86090,
        Z                   = 0,
        Y                   = 151630,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -82340,
        Z                   = 0,
        Y                   = 158280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = -47150,
        Z                   = 0,
        Y                   = 152620,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -126260,
        Y                   = 0,
        Z                   = 138000,
        Range               = 1000,
        Unknown_10          = 0x514,
        Unknown_14          = 0x0,
        Unknown_18          = 0x10040,
        Unknown_1C          = 0,
    )


    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 700,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_472",          # 00, 0
        "Function_1_668",          # 01, 1
        "Function_2_67B",          # 02, 2
        "Function_3_69F",          # 03, 3
        "Function_4_6EC",          # 04, 4
        "Function_5_710",          # 05, 5
        "Function_6_734",          # 06, 6
        "Function_7_758",          # 07, 7
        "Function_8_75D",          # 08, 8
        "Function_9_DFB",          # 09, 9
        "Function_10_14B9",        # 0A, 10
        "Function_11_18C5",        # 0B, 11
        "Function_12_1C8C",        # 0C, 12
        "Function_13_20C4",        # 0D, 13
        "Function_14_232E",        # 0E, 14
        "Function_15_2333",        # 0F, 15
        "Function_16_26D5",        # 10, 16
        "Function_17_29A8",        # 11, 17
        "Function_18_2BB3",        # 12, 18
        "Function_19_31D6",        # 13, 19
        "Function_20_35FC",        # 14, 20
        "Function_21_391B",        # 15, 21
        "Function_22_3BE0",        # 16, 22
        "Function_23_3DA8",        # 17, 23
        "Function_24_3F2B",        # 18, 24
        "Function_25_409B",        # 19, 25
        "Function_26_4171",        # 1A, 26
        "Function_27_4279",        # 1B, 27
        "Function_28_42BE",        # 1C, 28
        "Function_29_4322",        # 1D, 29
        "Function_30_4418",        # 1E, 30
    )


    def Function_0_472(): pass

    label("Function_0_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_48C")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Event(1, 10)

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4F0")
    OP_B2(0x0, 0x0, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x9, -124920, 0, 178920, 0)
    OP_43(0x9, 0x0, 0x0, 0x4)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D9")
    ClearChrFlags(0x19, 0x80)
    Jump("loc_4ED")

    label("loc_4D9")

    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)

    label("loc_4ED")

    Jump("loc_600")

    label("loc_4F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_51F")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x9, -126520, 0, 181820, 90)
    Jump("loc_600")

    label("loc_51F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x9, -42800, 0, 152070, 270)
    SetChrPos(0x16, -128430, 0, 128900, 270)
    Jump("loc_600")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_5C0")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x9, -130180, 0, 130460, 270)
    Jump("loc_600")

    label("loc_5C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_600")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x9, -130180, 0, 130460, 270)

    label("loc_600")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_623")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)

    label("loc_623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_667")
    SetChrPos(0xA, -123450, 0, 178760, 270)
    SetChrPos(0xD, -122420, 0, 179380, 270)
    SetChrPos(0xC, -128500, 0, 178640, 90)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_667")

    Return()

    # Function_0_472 end

    def Function_1_668(): pass

    label("Function_1_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67A")
    OP_10(0x1, 0x0)
    OP_10(0xE, 0x1)

    label("loc_67A")

    Return()

    # Function_1_668 end

    def Function_2_67B(): pass

    label("Function_2_67B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69E")
    OP_8D(0xFE, 3860, 184520, 5490, 181970, 1500)
    Jump("Function_2_67B")

    label("loc_69E")

    Return()

    # Function_2_67B end

    def Function_3_69F(): pass

    label("Function_3_69F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6EB")
    OP_8E(0xFE, 0xFFFE20C8, 0x0, 0x2C2B8, 0x5DC, 0x0)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFE20C8, 0x0, 0x2BC28, 0x5DC, 0x0)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Jump("Function_3_69F")

    label("loc_6EB")

    Return()

    # Function_3_69F end

    def Function_4_6EC(): pass

    label("Function_4_6EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70F")
    OP_8D(0xFE, -127570, 177960, -122660, 179600, 1000)
    Jump("Function_4_6EC")

    label("loc_70F")

    Return()

    # Function_4_6EC end

    def Function_5_710(): pass

    label("Function_5_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_733")
    OP_8D(0xFE, -51430, 121490, -47820, 118410, 1500)
    Jump("Function_5_710")

    label("loc_733")

    Return()

    # Function_5_710 end

    def Function_6_734(): pass

    label("Function_6_734")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_757")
    OP_8D(0xFE, -84580, 120430, -82970, 119500, 1500)
    Jump("Function_6_734")

    label("loc_757")

    Return()

    # Function_6_734 end

    def Function_7_758(): pass

    label("Function_7_758")

    Call(0, 8)
    Return()

    # Function_7_758 end

    def Function_8_75D(): pass

    label("Function_8_75D")

    TalkBegin(0x8)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77A")
    OP_A9(0x35)
    TalkEnd(0x8)
    Return()

    label("loc_77A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78B")
    TalkEnd(0x8)
    Return()

    label("loc_78B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_87C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_825")

    ChrTalk(    #0
        0x8,
        (
            "定期船的恢复航行，\x01",
            "到底要等到什么时候呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "本酒店也有\x01",
            "等待出发的客人在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "对从事旅游业的人们来说\x01",
            "真是个头痛的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_879")

    label("loc_825")


    ChrTalk(    #3
        0x8,
        (
            "定期船的恢复\x01",
            "会是什么时候呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "对从事旅游业的人们来说\x01",
            "真是个头痛的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_879")

    Jump("loc_DF7")

    label("loc_87C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_956")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_912")

    ChrTalk(    #5
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临富莱登酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "导力器虽然无法工作，\x01",
            "但本酒店依然照常营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "我们深知会给您带来不便，\x01",
            "但还请多多原谅。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_953")

    label("loc_912")


    ChrTalk(    #8
        0x8,
        (
            "导力器虽然无法工作，\x01",
            "但本酒店依然照常营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "请多担待。\x02",
    )

    CloseMessageWindow()

    label("loc_953")

    Jump("loc_DF7")

    label("loc_956")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9C1")

    ChrTalk(    #10
        0x8,
        (
            "超市的修复工程\x01",
            "给大家添了不少麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "今天和平时一样正常营业。\x01",
            "请大家多多惠顾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3F")

    label("loc_9C1")


    ChrTalk(    #12
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临富莱登酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "超市的修复工程\x01",
            "给大家添了不少麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "今天和平时一样正常营业。\x01",
            "请大家多多惠顾。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A3F")

    Jump("loc_DF7")

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AAD")

    ChrTalk(    #15
        0x8,
        (
            "看来超市的修复工程\x01",
            "进行的很顺利嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "嗯，\x01",
            "很快就要和这迷你百货市场说再见了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2F")

    label("loc_AAD")


    ChrTalk(    #17
        0x8,
        (
            "看来超市的修复工程\x01",
            "进行的很顺利嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "嗯，\x01",
            "很快就要和这迷你百货市场说再见了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "想到这里，\x01",
            "感觉稍稍有点寂寞呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B2F")

    Jump("loc_DF7")

    label("loc_B32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BC4")

    ChrTalk(    #20
        0x8,
        (
            "现在，\x01",
            "本酒店开放为商人们的临时店铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "非常时期的团结以及互相协助\x01",
            "正是我们柏斯商人的美德啊。\x01",
            "我很乐意为大家效犬马之劳。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C3A")

    label("loc_BC4")


    ChrTalk(    #22
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临富莱登酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "现在，\x01",
            "本酒店开放为商人们的临时店铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "怎么回事，\x01",
            "有点百货超市的感觉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C3A")

    Jump("loc_DF7")

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C6D")

    ChrTalk(    #25
        0x8,
        (
            "唉哟哟……\x01",
            "出大事儿了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D08")

    label("loc_C6D")


    ChrTalk(    #26
        0x8,
        (
            "唉哟哟……\x01",
            "唉哟哟，出大事情了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "遵从梅贝尔市长的请求，\x01",
            "本酒店会将客房开放，\x01",
            "用于保护商人们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "但是那个怪物要是再来的话\x01",
            "该怎么办啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D08")

    Jump("loc_DF7")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_DF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D68")

    ChrTalk(    #29
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临富莱登酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "帝国大使大人\x01",
            "目前正在本酒店下榻暂住。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF7")

    label("loc_D68")


    ChrTalk(    #31
        0x8,
        (
            "欢迎。\x01",
            "欢迎光临富莱登酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "帝国大使大人\x01",
            "目前正在本酒店下榻暂住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "出于安全的考虑，\x01",
            "我们深知会给您带来不便，\x01",
            "还请务必多包涵。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DF7")

    TalkEnd(0x8)
    Return()

    # Function_8_75D end

    def Function_9_DFB(): pass

    label("Function_9_DFB")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_F34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDF")

    ChrTalk(    #34
        0xFE,
        (
            "酒店里现在住的客人是\x01",
            "因为定期船停航才住下的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "啊啊，\x01",
            "虽然觉得客人们挺可怜的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "但突然间被增加工作量的\x01",
            "我才更可怜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "本来以为超市的销售量可以\x01",
            "有所上升的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "……唉，真是灾难啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_F31")

    label("loc_EDF")


    ChrTalk(    #39
        0xFE,
        (
            "定期船的客人\x01",
            "虽然觉得挺可怜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "但是突然间被增加工作量的\x01",
            "我才更可怜啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F31")

    Jump("loc_14B5")

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1025")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC0")

    ChrTalk(    #41
        0xFE,
        (
            "啊～真是的……\x01",
            "太费时间了，真没办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "如果扫地不用吸尘器，\x01",
            "还是会很麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "就好像煎蛋\x01",
            "不用锅子一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1022")

    label("loc_FC0")


    ChrTalk(    #44
        0xFE,
        (
            "如果扫地不用吸尘器，\x01",
            "还是会很麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "唉，老板那家伙总说我……\x01",
            "倒是让他自己来试试看啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1022")

    Jump("loc_14B5")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_111B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1088")

    ChrTalk(    #46
        0xFE,
        (
            "那个帝国大使什么的，\x01",
            "总算是回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "总是摆着一副臭架子，\x01",
            "感觉好讨厌哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1118")

    label("loc_1088")


    ChrTalk(    #48
        0xFE,
        (
            "那个帝国大使什么的，\x01",
            "可算回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "总是摆着一副臭架子，\x01",
            "感觉好讨厌哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "虽然商人先生回去了挺遗憾的，\x01",
            "但那个人走了可真叫人高兴。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1118")

    Jump("loc_14B5")

    label("loc_111B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_11FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_118E")

    ChrTalk(    #51
        0xFE,
        (
            "这位商人先生\x01",
            "做的是碟子和小商品的生意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "上班时还可以买东西，\x01",
            "真是梦一般的职场环境啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_118E")


    ChrTalk(    #53
        0xFE,
        (
            "这位商人先生\x01",
            "做的是碟子和小商品的生意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "刚好我正在\x01",
            "寻找茶杯呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "等等有时间\x01",
            "再来看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11FA")

    Jump("loc_14B5")

    label("loc_11FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_130B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1270")

    ChrTalk(    #56
        0xFE,
        (
            "短时间内，我们酒店\x01",
            "会成为商人们的临时住所呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "工作能够变轻松的话，\x01",
            "不管是什么我都欢迎。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1308")

    label("loc_1270")


    ChrTalk(    #58
        0xFE,
        (
            "短时间内，我们酒店\x01",
            "会成为商人们的临时住所呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "这也就是说，负责客房的人\x01",
            "可以不用工作了是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "去看看就知道，\x01",
            "几乎都处在开店休业状态嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1308")

    Jump("loc_14B5")

    label("loc_130B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_13F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1379")

    ChrTalk(    #61
        0xFE,
        (
            "总，总觉得商人们好像\x01",
            "在往客房里搬运货物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "这里会被梅贝尔市长收购\x01",
            "变成超市2号店吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13F0")

    label("loc_1379")


    ChrTalk(    #63
        0xFE,
        (
            "总，总觉得商人们好像\x01",
            "在往客房里搬运货物。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "啊，难道说！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "这里会被梅贝尔市长收购\x01",
            "变成超市２号店之类？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_13F0")

    Jump("loc_14B5")

    label("loc_13F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_14B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1450")

    ChrTalk(    #66
        0xFE,
        (
            "住在２楼的人\x01",
            "好像颇有来头呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "不过，\x01",
            "好像一直待在房间里不出来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B5")

    label("loc_1450")


    ChrTalk(    #68
        0xFE,
        (
            "住在２楼的人\x01",
            "好像颇有来头呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "不过，\x01",
            "好像一直待在房间里不出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "到底在做什么呢？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_14B5")

    TalkEnd(0x9)
    Return()

    # Function_9_DFB end

    def Function_10_14B9(): pass

    label("Function_10_14B9")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1543")

    ChrTalk(    #71
        0xA,
        (
            "#1100F对我来说只要把\x01",
            "勋章取回来就足够了。\x02\x03",

            "『怪盗Ｂ』的逮捕\x01",
            "是国家及协会全体考虑的问题……\x02\x03",

            "我觉得\x01",
            "你们没有必要太担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_1543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1622")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15B5")

    ChrTalk(    #72
        0xA,
        (
            "#1100F我最后决定\x01",
            "乘坐王国军警备艇回王都。\x02\x03",

            "嗯，对待帝国大使，\x01",
            "这样的安排是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_161F")

    label("loc_15B5")


    ChrTalk(    #73
        0xA,
        (
            "#1100F计划将乘坐王国军的警备艇\x01",
            "于不久后返回王都。\x02\x03",

            "无论如何都要在这之前把勋章找回来！\x01",
            "一定要找回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_161F")

    Jump("loc_18C1")

    label("loc_1622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1708")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1698")

    ChrTalk(    #74
        0xA,
        (
            "#1100F定期船停航了，\x01",
            "就算想回王都也没有办法。\x02\x03",

            "我，我可是帝国大使！\x01",
            "敢挡我去路，胆子可不小。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1705")

    label("loc_1698")


    ChrTalk(    #75
        0xA,
        (
            "#1100F勋章是陛下赏赐予\x01",
            "本家族荣誉的象征……\x02\x03",

            "但是，我差不多\x01",
            "该回王都了。\x02\x03",

            "无论如何\x01",
            "都要在这之前找回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1705")

    Jump("loc_18C1")

    label("loc_1708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_17FB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1792")

    ChrTalk(    #76
        0xA,
        (
            "#1100F即使我打算恢复视察，\x01",
            "可是超市现在那副样子也没办法继续……\x02\x03",

            "唔，预定的行程终于结束了。\x01",
            "应该是时候回王都了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17F8")

    label("loc_1792")


    ChrTalk(    #77
        0xA,
        (
            "#1100F那勋章是皇帝陛下赏赐的，\x01",
            "是本家族荣誉的象征……\x02\x03",

            "难道超市也被牵连到了……\x01",
            "真是没有想到啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F8")

    Jump("loc_18C1")

    label("loc_17FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_18C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_187A")

    ChrTalk(    #78
        0xA,
        (
            "#1100F我觉得是时候恢复\x01",
            "对这座城市的视察了。\x02\x03",

            "听说柏斯超市里有\x01",
            "很多我国的商人。\x02\x03",

            "首先\x01",
            "得从那里开始啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C1")

    label("loc_187A")


    ChrTalk(    #79
        0xA,
        (
            "#1100F那个勋章\x01",
            "是殿下赏赐给我家的荣誉……\x02\x03",

            "无论如何都要找回来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C1")

    TalkEnd(0xA)
    Return()

    # Function_10_14B9 end

    def Function_11_18C5(): pass

    label("Function_11_18C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_19C6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1983")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_192C")

    ChrTalk(    #80
        0xFE,
        "非常感谢各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "勋章完好无损的找回来了，\x01",
            "这样就可以放心回国了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1980")

    label("loc_192C")


    ChrTalk(    #82
        0xFE,
        (
            "在王国军的协助下，\x01",
            "能够回王都了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "大使大人非常感谢\x01",
            "王国方面所表示的诚意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1980")

    Jump("loc_19C3")

    label("loc_1983")


    ChrTalk(    #84
        0xFE,
        (
            "王国军为了大使\x01",
            "出动了飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "在船到达前\x01",
            "能找到勋章吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C3")

    Jump("loc_1C88")

    label("loc_19C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1AB9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A39")

    ChrTalk(    #86
        0xFE,
        "非常感谢各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "但是，超市\x01",
            "暂时休业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "若是能在日程内\x01",
            "完成视察就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A76")

    label("loc_1A39")


    ChrTalk(    #89
        0xFE,
        (
            "帝国的人当中，\x01",
            "好像没有人负伤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "真是不幸中的大幸。\x02",
    )

    CloseMessageWindow()

    label("loc_1A76")

    Jump("loc_1AB6")

    label("loc_1A79")


    ChrTalk(    #91
        0xFE,
        "能找到勋章吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "只要……\x01",
            "能在回王都前找到就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB6")

    Jump("loc_1C88")

    label("loc_1AB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B0F")

    ChrTalk(    #93
        0xFE,
        "非常感谢各位。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "但是，\x01",
            "超市遭受破坏的程度如何呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B32")

    label("loc_1B0F")


    ChrTalk(    #95
        0xFE,
        (
            "超市遭受的破坏，\x01",
            "的程度如何？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B32")


    ChrTalk(    #96
        0xFE,
        (
            "难道会影响到视察行程的安排，\x01",
            "说不定会取消行程。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB2")

    label("loc_1B6A")


    ChrTalk(    #97
        0xFE,
        (
            "超市遭受的破坏，\x01",
            "的程度如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "受伤人员中\x01",
            "可能也有我国的商人。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB2")

    Jump("loc_1C88")

    label("loc_1BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1C88")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1C44")

    ChrTalk(    #99
        0xFE,
        (
            "象征功劳的勋章……\x01",
            "衷心祝贺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "这枚勋章是授予那些\x01",
            "为帝国做出过贡献的人们的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "授予外国人，\x01",
            "可是非常罕见的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C88")

    label("loc_1C44")


    ChrTalk(    #102
        0xFE,
        (
            "各位，务必\x01",
            "就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "这样下去\x01",
            "视察肯定无法恢复了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C88")

    TalkEnd(0xFE)
    Return()

    # Function_11_18C5 end

    def Function_12_1C8C(): pass

    label("Function_12_1C8C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1DA2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D21")

    ChrTalk(    #104
        0xFE,
        (
            "大使已经预定好了返回王都的时间。\x01",
            "很快就要起程了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "这次事件能圆满解决真是多亏你们的帮忙。\x01",
            "非常感谢你们，各位游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D9F")

    label("loc_1D21")


    ChrTalk(    #106
        0xFE,
        "调查的情况怎么样了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "大使已经预定好了返回王都的时间。\x01",
            "很快就要起程了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "调查所剩的时间已经不多了。\x01",
            "请多加努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9F")

    Jump("loc_20C0")

    label("loc_1DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1EB4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E3B")

    ChrTalk(    #109
        0xFE,
        (
            "由于王国处于警戒状态，\x01",
            "我们正在考虑返回王都的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "由于王国军的戒严，\x01",
            "定期船又无法使用，\x01",
            "我们唯有竭尽全力寻找其他的方法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB1")

    label("loc_1E3B")


    ChrTalk(    #111
        0xFE,
        "各位，调查有进展吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "由于王国处于警戒状态，\x01",
            "我们正在寻找返回王都的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "离开大使馆太长时间\x01",
            "可不行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB1")

    Jump("loc_20C0")

    label("loc_1EB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1FF2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F0C")

    ChrTalk(    #114
        0xFE,
        (
            "按照行程，\x01",
            "正要恢复视察……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "没想到却出了那种事……\x01",
            "唉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F7C")

    ChrTalk(    #116
        0xFE,
        (
            "光是勋章被盗事件就够\x01",
            "我们忙的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "竟然接二连三的出事\x01",
            "俗话说屋漏偏逢连夜雨，就是这样的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FEF")

    label("loc_1F7C")


    ChrTalk(    #118
        0xFE,
        (
            "光是勋章被盗事件就够\x01",
            "我们忙的了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "再加上超市那件事\x01",
            "唉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "俗话说屋漏偏逢连夜雨，就是这样的吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FEF")

    Jump("loc_20C0")

    label("loc_1FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_20C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2070")

    ChrTalk(    #121
        0xFE,
        (
            "各位游击士，\x01",
            "大使也计划不久后恢复视察。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "之前真是承蒙你们的照顾。\x01",
            "衷心对各位这次的协助表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C0")

    label("loc_2070")


    ChrTalk(    #123
        0xFE,
        (
            "为了我帝国的荣誉，\x01",
            "请各位一定要发挥实力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "务必请将大使的勋章\x01",
            "找回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C0")

    TalkEnd(0xD)
    Return()

    # Function_12_1C8C end

    def Function_13_20C4(): pass

    label("Function_13_20C4")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_232A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 2)), scpexpr(EXPR_END)), "loc_2159")

    ChrTalk(    #125
        0xFE,
        (
            "打算暂时借用这里\x01",
            "继续营业啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "货源虽然不足，\x01",
            "但是我还是会一如既往继续努力的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "想要什么的话，\x01",
            "就和那边的伙计说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232A")

    label("loc_2159")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #128
        0xFE,
        "啊，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "谢谢。\x01",
            "危难时多亏有你们相救啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1002F哪里，在非常时期这是应该做的。\x02\x03",

            "超市里面的人\x01",
            "全部都成功逃出来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "是啊，暂时是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "在小姐的安排下\x01",
            "暂时在这里营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "商店全部关闭的话，\x01",
            "会给市民的生活带来麻烦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1011F不愧是梅贝尔市长。\x01",
            "这种时候的反应真迅速。\x02\x03",

            "#1006F虽然很不容易但加油。\x01",
            "有什么事我们也会帮忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "噢，就算是为了小姐也要加油啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "想要什么的话，\x01",
            "就和那边的伙计说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A42)

    label("loc_232A")

    TalkEnd(0xE)
    Return()

    # Function_13_20C4 end

    def Function_14_232E(): pass

    label("Function_14_232E")

    Call(0, 15)
    Return()

    # Function_14_232E end

    def Function_15_2333(): pass

    label("Function_15_2333")

    TalkBegin(0xF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2394")
    OP_0D()
    OP_A9(0x50)
    OP_56(0x0)
    TalkEnd(0xF)
    Return()

    label("loc_2394")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23A5")
    TalkEnd(0xF)
    Return()

    label("loc_23A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_24B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_240E")

    ChrTalk(    #137
        0xFE,
        (
            "由于军队的作战，\x01",
            "定期船一直停航中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "虽然是无可奈何的事，\x01",
            "但是库存也快没有了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B4")

    label("loc_240E")


    ChrTalk(    #139
        0xFE,
        (
            "由于军队的作战，\x01",
            "定期船一直停航中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "虽然是无可奈何的事，\x01",
            "但是库存也快没有了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "但是，大家都是一样辛苦啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "就算无视利益，\x01",
            "也会维持现在的价格的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_24B4")

    Jump("loc_26D1")

    label("loc_24B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_25C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(    #143
        0xFE,
        (
            "超市的修复工程\x01",
            "今早开始动工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "不愧是天才般的梅贝尔市长。\x01",
            "处理事情的手腕的确英明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C2")

    label("loc_2526")


    ChrTalk(    #145
        0xFE,
        "呀，欢迎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "超市修复工程，\x01",
            "好像今早开始动工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "巴克那家伙\x01",
            "听到消息就飞奔过去帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "对那家伙在这种时候的干劲，\x01",
            "说真的，我很羡慕啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_25C2")

    Jump("loc_26D1")

    label("loc_25C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_26D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_260B")

    ChrTalk(    #149
        0xFE,
        "还没冷静下来呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "唔……\x01",
            "超市今后会怎样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26D1")

    label("loc_260B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_268B")

    ChrTalk(    #151
        0xFE,
        (
            "啊……\x01",
            "不过总觉得无法安心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "虽然我们设法让店铺继续营业下去……\x01",
            "但是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "唔……\x01",
            "超市今后会怎样啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_26D1")

    label("loc_268B")


    ChrTalk(    #154
        0xFE,
        "呀，刚才真多亏你们帮忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "总之，\x01",
            "莉拉没事就真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_26D1")

    TalkEnd(0xF)
    Return()

    # Function_15_2333 end

    def Function_16_26D5(): pass

    label("Function_16_26D5")

    TalkBegin(0x10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2736")
    OP_0D()
    OP_A9(0x40)
    OP_56(0x0)
    TalkEnd(0x10)
    Return()

    label("loc_2736")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2747")
    TalkEnd(0x10)
    Return()

    label("loc_2747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2859")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_27BE")

    ChrTalk(    #156
        0xFE,
        (
            "说起我老公，\x01",
            "他还在担心村子的事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "真希望他能多为家里着想，\x01",
            "就算是担心村子的几分之一都行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2856")

    label("loc_27BE")


    ChrTalk(    #158
        0xFE,
        "我丈夫真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "都到这地步了，\x01",
            "还在为村里的事担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "村人们又不是小孩子，\x01",
            "总会自己想办法的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "本来就不是\x01",
            "该轮到他操心的事儿嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2856")

    Jump("loc_29A4")

    label("loc_2859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_292D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_28B2")

    ChrTalk(    #162
        0xFE,
        (
            "拉文努村的\x01",
            "那位先生来了噢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "这种时候，有男人在\x01",
            "可真帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_292A")

    label("loc_28B2")


    ChrTalk(    #164
        0xFE,
        (
            "拉文努村的\x01",
            "那位先生来了噢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "这种时候，有男人在\x01",
            "可真帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "虽然有一肚子话想说，\x01",
            "还是暂时忍了下来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_292A")

    Jump("loc_29A4")

    label("loc_292D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_29A4")

    ChrTalk(    #167
        0xFE,
        (
            "但我到现在还是不相信\x01",
            "会有龙出现。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "在故乡拉文努村\x01",
            "过去也有着这样的传说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        "但没想到居然会是真的。\x02",
    )

    CloseMessageWindow()

    label("loc_29A4")

    TalkEnd(0x10)
    Return()

    # Function_16_26D5 end

    def Function_17_29A8(): pass

    label("Function_17_29A8")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_29FF")

    ChrTalk(    #170
        0xFE,
        (
            "妈妈虽然跟我\x01",
            "抱怨了很多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "不过爸爸能来，\x01",
            "她果然还是很开心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BAF")

    label("loc_29FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2A60")

    ChrTalk(    #172
        0xFE,
        (
            "好像拉文努村也\x01",
            "出现龙了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "虽然没有人受伤，\x01",
            "但是果树园却被烧毁了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF1")

    label("loc_2A60")


    ChrTalk(    #174
        0xFE,
        (
            "好像听说拉文努村也\x01",
            "出现了龙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "虽然没有人受伤，\x01",
            "但是果树园却被烧毁了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "虽然我很庆幸\x01",
            "爸爸他没有受伤。\x01",
            "但是感觉有点笑不太出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2AF1")

    Jump("loc_2BAF")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2BAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2B4C")

    ChrTalk(    #177
        0xFE,
        (
            "龙朝着爸爸所在的村子的方向\x01",
            "飞走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "但愿不要出什么事才好……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BAF")

    label("loc_2B4C")


    ChrTalk(    #179
        0xFE,
        (
            "龙好像朝\x01",
            "西北方飞去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "那方向就是\x01",
            "爸爸所在的拉文努村。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "但愿不要出什么事才好……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2BAF")

    TalkEnd(0x11)
    Return()

    # Function_17_29A8 end

    def Function_18_2BB3(): pass

    label("Function_18_2BB3")

    TalkBegin(0x12)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C14")
    OP_0D()
    OP_A9(0x3C)
    OP_56(0x0)
    TalkEnd(0x12)
    Return()

    label("loc_2C14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C25")
    TalkEnd(0x12)
    Return()

    label("loc_2C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x11, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C32")
    OP_A2(0xA)

    label("loc_2C32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA8")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇前编QST017通关】\x01",          # 0
            "【◇前编QST017没有通关】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C9C"),
        (1, "loc_2CA2"),
        (SWITCH_DEFAULT, "loc_2CA8"),
    )


    label("loc_2C9C")

    OP_A2(0xA)
    Jump("loc_2CA8")

    label("loc_2CA2")

    OP_A3(0xA)
    Jump("loc_2CA8")

    label("loc_2CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2D12")

    ChrTalk(    #182
        0xFE,
        (
            "看来超市的修复工程\x01",
            "进展很顺利啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "好像很久都没有听到\x01",
            "好消息了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E67")

    label("loc_2D12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2D5C")

    ChrTalk(    #184
        0xFE,
        (
            "超市的修复工作\x01",
            "好像开始了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "要是能\x01",
            "早日恢复就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E67")

    label("loc_2D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2E67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2DD1")

    ChrTalk(    #186
        0xFE,
        (
            "目前我们的计划是\x01",
            "借用这里的场地来维持买卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "因为大家都不知道\x01",
            "超市什么时候才能恢复营运啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E67")

    label("loc_2DD1")


    ChrTalk(    #188
        0xFE,
        (
            "哎呀哎呀，总之\x01",
            "把做买卖的道具都带出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "目前我们的计划是\x01",
            "借用这里的场地来维持买卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "因为大家都不知道\x01",
            "超市什么时候才能恢复营运啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2E67")

    Jump("loc_2EBC")

    label("loc_2E6A")


    ChrTalk(    #191
        0xFE,
        (
            "这药代表了我\x01",
            "支持你们的心意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "这药的效果很不错，\x01",
            "我想应该能够派上用场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBC")

    Jump("loc_31D2")

    label("loc_2EBF")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #193
        0xFE,
        "啊，各位是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "曾经帮我寻找药草的\x01",
            "游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1016F好像……\x01",
            "的确有这么回事。\x02\x03",

            "#1000F老爷爷\x01",
            "现在还在这里做买卖？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "是的，目前这段时间……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "如果这时候药店关门的话，\x01",
            "大家会很为难的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_304C")

    ChrTalk(    #198
        0x101,
        (
            "#1006F嘿，我们也正需要您的药品。\x02\x03",

            "#1015F因为我们马上\x01",
            "准备去做一件麻烦的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "麻烦的工作？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "是关于龙的事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x101,
        "#1011F啊，是的，怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_30E8")

    label("loc_304C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_30E8")

    ChrTalk(    #202
        0x101,
        (
            "#1006F嘿，我们也正需要您的药品。\x02\x03",

            "#1015F因为我们马上\x01",
            "准备出城调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "调查？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "是关于之前龙的那件事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#1011F嗯，是与之相关的调查。\x02",
    )

    CloseMessageWindow()

    label("loc_30E8")


    ChrTalk(    #206
        0xFE,
        (
            "这样的话，\x01",
            "让我也来帮你们一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #207
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x205, 1)

    ChrTalk(    #208
        0xFE,
        (
            "这是效果很不错的药，\x01",
            "我想肯定能帮到你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "那么，\x01",
            "期待你们工作顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1001F谢谢爷爷。\x01",
            "我们会好好使用的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A40)
    OP_A2(0x8)

    label("loc_31D2")

    TalkEnd(0x12)
    Return()

    # Function_18_2BB3 end

    def Function_19_31D6(): pass

    label("Function_19_31D6")

    TalkBegin(0x13)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3243")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3238")
    OP_A9(0x44)
    Jump("loc_323A")

    label("loc_3238")

    OP_A9(0x42)

    label("loc_323A")

    OP_56(0x0)
    TalkEnd(0x13)
    Return()

    label("loc_3243")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3254")
    TalkEnd(0x13)
    Return()

    label("loc_3254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3340")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_32B3")

    ChrTalk(    #211
        0xFE,
        (
            "由于军队的戒严，\x01",
            "定期船还在停航中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "哎呀，商品的货源\x01",
            "将更加紧张了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333D")

    label("loc_32B3")


    ChrTalk(    #213
        0xFE,
        (
            "由于军队的戒严，\x01",
            "定期船还在停开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "不过，为了抓住龙\x01",
            "这么做还是有必要的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "都做到这地步了，\x01",
            "真希望能够百分之一百成功啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_333D")

    Jump("loc_35F8")

    label("loc_3340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_342E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_33A7")

    ChrTalk(    #216
        0xFE,
        (
            "王国军好像\x01",
            "正在做抓捕龙的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "我还记得……\x01",
            "小时候老师说龙是神圣的生物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_342B")

    label("loc_33A7")


    ChrTalk(    #218
        0xFE,
        (
            "王国军好像\x01",
            "正在做抓捕龙的准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "我还记得……\x01",
            "小时候老师说龙是神圣的生物呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "假如去抓捕它的话，\x01",
            "是不是会遭天遣呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_342B")

    Jump("loc_35F8")

    label("loc_342E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_35F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_34E4")

    ChrTalk(    #221
        0xFE,
        (
            "那时候有一瞬间，我眼前浮现出\x01",
            "战争的景象了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "不过呢，我们的超市\x01",
            "就算化成了灰烬也还是会再建起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "不管是龙来了还是炸弹投下来了，\x01",
            "我们都会让它复活的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F8")

    label("loc_34E4")


    ChrTalk(    #224
        0xFE,
        (
            "瓦砾掉下来的时候，\x01",
            "我又想起了那时战争的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "那个时候也是天花板燃烧着往下塌，\x01",
            "大家一个劲的逃命……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "不过呢，不能忘记的是，\x01",
            "即便如此也能重新建起超市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "只要我们永不放弃，\x01",
            "不管遇到怎样的挫折都能够再次站立起来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "战争对我来说，\x01",
            "是一个不可磨灭的记忆了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_35F8")

    TalkEnd(0x13)
    Return()

    # Function_19_31D6 end

    def Function_20_35FC(): pass

    label("Function_20_35FC")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3672")

    ChrTalk(    #229
        0xFE,
        (
            "王国军抓捕龙的作战之中，\x01",
            "好像『埃尔赛尤』也参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "计划的真好，\x01",
            "真希望能顺利赶走龙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3714")

    label("loc_3672")


    ChrTalk(    #231
        0xFE,
        (
            "王国军抓捕龙的作战之中，\x01",
            "好像『埃尔赛尤』也参加了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "不愧是女王陛下发表的声明，\x01",
            "王国军给人一种全力出击的感觉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "那么到最后，\x01",
            "那次作战成功了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3714")

    Jump("loc_3917")

    label("loc_3717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_382A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_3784")

    ChrTalk(    #234
        0xFE,
        (
            "现在借用了酒店的房间\x01",
            "可以继续营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "柏斯商人的那种互相帮助\x01",
            "的精神可真令人钦佩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3827")

    label("loc_3784")


    ChrTalk(    #236
        0xFE,
        (
            "在梅贝尔市长的安排下，\x01",
            "现在借用了酒店的房间\x01",
            "可以继续营业了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "柏斯商人的那种互相帮助\x01",
            "的精神可真令人钦佩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "正因为有这样的基础\x01",
            "才能从战争中恢复啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3827")

    Jump("loc_3917")

    label("loc_382A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3917")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_388B")

    ChrTalk(    #239
        0xFE,
        (
            "米蕾婆婆跑回去拿商品，\x01",
            "可真让人着急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "婆婆真不愧是超市\x01",
            "里的风云人物。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3917")

    label("loc_388B")


    ChrTalk(    #241
        0xFE,
        (
            "我，我们……\x01",
            "总算是……平安逃出来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "米蕾婆婆在半路上\x01",
            "又跑回去拿商品可真让人着急。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "从战火中过来的人\x01",
            "的胆识果然了得啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_3917")

    TalkEnd(0x14)
    Return()

    # Function_20_35FC end

    def Function_21_391B(): pass

    label("Function_21_391B")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3A13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3987")

    ChrTalk(    #244
        0xFE,
        (
            "定期船明明停航了，\x01",
            "但蔬菜的价格却没有上涨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "真奇怪啊……\x01",
            "还以为一定会涨价呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A10")

    label("loc_3987")


    ChrTalk(    #246
        0xFE,
        (
            "我是来逛\x01",
            "蔬果店的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "定期船明明停航了，\x01",
            "但蔬菜的价格却没有上涨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "真奇怪啊……\x01",
            "原本以为一定会涨价，\x01",
            "结果提早买了很多。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3A10")

    Jump("loc_3BDC")

    label("loc_3A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3B15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3A82")

    ChrTalk(    #249
        0xFE,
        (
            "就算稍微贵一点，\x01",
            "好像也是现在买比较划算吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "不过，买没打折的东西\x01",
            "总有种失败感呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B12")

    label("loc_3A82")


    ChrTalk(    #251
        0xFE,
        (
            "听说了吗？定期船好像\x01",
            "还没恢复航行呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "这就是说，蔬菜的价格\x01",
            "渐渐会开始上涨是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "就算稍微贵一点，\x01",
            "好像也是现在买比较划算吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3B12")

    Jump("loc_3BDC")

    label("loc_3B15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_3B69")

    ChrTalk(    #254
        0xFE,
        (
            "嗯嗯……\x01",
            "商人们好像在避难的地方做买卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "这样真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BDC")

    label("loc_3B69")


    ChrTalk(    #256
        0xFE,
        (
            "嗯嗯……\x01",
            "商人们好像在避难的地方做买卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "这样真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "还没决定晚饭要吃什么呢。\x01",
            "吃什么好呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_3BDC")

    TalkEnd(0x15)
    Return()

    # Function_21_391B end

    def Function_22_3BE0(): pass

    label("Function_22_3BE0")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3C4A")

    ChrTalk(    #259
        0x16,
        (
            "定期船停航了，\x01",
            "每一家店铺都很繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x16,
        (
            "果然……\x01",
            "还没有到开商业洽谈会的时候。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD6")

    label("loc_3C4A")


    ChrTalk(    #261
        0x16,
        (
            "定期船停航了，\x01",
            "每一家店铺都很繁忙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x16,
        (
            "果然……\x01",
            "还没有到开商业洽谈会的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x16,
        (
            "直到超市恢复营业前，\x01",
            "除了等没有别的可做了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_3CD6")

    Jump("loc_3DA4")

    label("loc_3CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3DA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_3D2C")

    ChrTalk(    #264
        0x16,
        (
            "超市的店铺\x01",
            "好像暂时在这里营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x16,
        (
            "那么，\x01",
            "周围先转一圈吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA4")

    label("loc_3D2C")


    ChrTalk(    #266
        0x16,
        (
            "超市的店铺\x01",
            "好像暂时在这里营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x16,
        (
            "那么，\x01",
            "周围先转一圈吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x16,
        (
            "可能营业方面有点吃紧，\x01",
            "但是还是想去打个招呼。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_3DA4")

    TalkEnd(0x16)
    Return()

    # Function_22_3BE0 end

    def Function_23_3DA8(): pass

    label("Function_23_3DA8")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3E98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3DFD")

    ChrTalk(    #269
        0xFE,
        "我很担心拉文努村啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "贝斯卡和库赖\x01",
            "能和睦相处就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E95")

    label("loc_3DFD")


    ChrTalk(    #271
        0xFE,
        (
            "虽然匆匆忙忙\x01",
            "离开拉文努村来到了这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "但果然还是担心村子啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "贝斯卡和库赖\x01",
            "能和睦相处就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "毕竟他们两个\x01",
            "一直坚持到现在啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_3E95")

    Jump("loc_3F27")

    label("loc_3E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3F27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_3ED4")

    ChrTalk(    #275
        0xFE,
        (
            "老婆和孩子没有受伤，\x01",
            "我总算松了口气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F27")

    label("loc_3ED4")


    ChrTalk(    #276
        0xFE,
        (
            "这里的超市\x01",
            "好像被破坏了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "总之老婆和孩子没有受伤，\x01",
            "我总算松了口气。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_3F27")

    TalkEnd(0x17)
    Return()

    # Function_23_3DA8 end

    def Function_24_3F2B(): pass

    label("Function_24_3F2B")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3FCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9B")

    ChrTalk(    #278
        0xFE,
        "糟糕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "钱包差不多\x01",
            "快空了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "虽然手上有回去的船票，\x01",
            "但船不来也没用啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_3FCA")

    label("loc_3F9B")


    ChrTalk(    #281
        0xFE,
        "糟糕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "钱包差不多\x01",
            "快要光溜溜了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCA")

    Jump("loc_4097")

    label("loc_3FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_404B")

    ChrTalk(    #283
        0xFE,
        (
            "我是来柏斯参观\x01",
            "哈肯大门的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "没想到在旅行的目的地\x01",
            "会遇到这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "总之希望\x01",
            "能早日恢复啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_4097")

    label("loc_404B")


    ChrTalk(    #286
        0xFE,
        (
            "没想到在旅行的目的地\x01",
            "会出这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "真希望定期船能\x01",
            "早日恢复航行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4097")

    TalkEnd(0x18)
    Return()

    # Function_24_3F2B end

    def Function_25_409B(): pass

    label("Function_25_409B")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4127")

    ChrTalk(    #288
        0xFE,
        (
            "我的导力照相机也\x01",
            "无法使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "好不容易有机会\x01",
            "能拍到哈肯大门的威容……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "唔唔，好想快点\x01",
            "看到冲洗出来的照片啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_416D")

    label("loc_4127")


    ChrTalk(    #291
        0xFE,
        (
            "我的导力照相机也\x01",
            "无法使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "现在没办法冲洗\x01",
            "真让人着急啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_416D")

    TalkEnd(0x19)
    Return()

    # Function_25_409B end

    def Function_26_4171(): pass

    label("Function_26_4171")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_421B")

    ChrTalk(    #293
        0xFE,
        (
            "虽然安排的很仓促，\x01",
            "但还是很不错的酒店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "并且住宿费全由\x01",
            "飞船公社承担……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "觉得有种因祸得福的感觉呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "……不过现在\x01",
            "可不是高兴的时候。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_4275")

    label("loc_421B")


    ChrTalk(    #297
        0xFE,
        (
            "虽然安排的很仓促，\x01",
            "但还是很不错的酒店啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "飞船公社的服务还是\x01",
            "十分令人满意的嘛。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4275")

    TalkEnd(0x1A)
    Return()

    # Function_26_4171 end

    def Function_27_4279(): pass

    label("Function_27_4279")

    TalkBegin(0x1B)

    ChrTalk(    #299
        0xFE,
        (
            "能这么快住进酒店，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "我跟女儿\x01",
            "都很累了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x1B)
    Return()

    # Function_27_4279 end

    def Function_28_42BE(): pass

    label("Function_28_42BE")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4303")

    ChrTalk(    #301
        0xFE,
        (
            "这里的澡堂\x01",
            "很不错哦⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "好像是公主\x01",
            "用的呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)
    Jump("loc_431E")

    label("loc_4303")


    ChrTalk(    #303
        0xFE,
        (
            "这里的澡堂\x01",
            "很不错哦⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431E")

    TalkEnd(0x1C)
    Return()

    # Function_28_42BE end

    def Function_29_4322(): pass

    label("Function_29_4322")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C0")

    ChrTalk(    #304
        0xFE,
        (
            "虽然很感谢能\x01",
            "为我们准备房间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "但这也就是说，定期船要停航\x01",
            "很长一段时间是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "也罢，这也是没有办法的。\x01",
            "先去洗个澡放松一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_4414")

    label("loc_43C0")


    ChrTalk(    #307
        0xFE,
        (
            "看来定期船要\x01",
            "停航很久呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "也罢，这也是没有办法的。\x01",
            "先去洗个澡放松一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4414")

    TalkEnd(0x1D)
    Return()

    # Function_29_4322 end

    def Function_30_4418(): pass

    label("Function_30_4418")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #309
        (
            "\x07\x05　　　　　　　工作人员室　　　　　　　\x01",
            "          ※无关人员请勿入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_4418 end

    SaveToFile()

Try(main)
