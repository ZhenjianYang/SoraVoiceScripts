from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1500   ._SN',
        MapName             = 'Bose',
        Location            = 'T1500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        '雪拉扎德',                             # 9
        '阿加特',                               # 10
        '奥利维尔',                             # 11
        '科洛丝',                               # 12
        '提妲',                                 # 13
        '金',                                   # 14
        '凯文神父',                             # 15
        '基库',                                 # 16
        '小船',                                 # 17
        '小船',                                 # 18
        '克鲁茨',                               # 19
        '诺琪',                                 # 20
        '赫穆特',                               # 21
        '斯丁克',                               # 22
        '罗伊德',                               # 23
        '操舵士勒克司',                         # 24
        '酒杯',                                 # 25
        '酒杯',                                 # 26
        '酒杯',                                 # 27
        '酒杯',                                 # 28
        '库瓦诺老人',                           # 29
        '桶和魚',                               # 30
        '桶和魚',                               # 31
        '桶和魚',                               # 32
        '桶和魚',                               # 33
        '安赛尔新街方向',                       # 34
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
        'ED6_DT06/CH20045 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT07/CH00023 ._CH',             # 02
        'ED6_DT07/CH00053 ._CH',             # 03
        'ED6_DT07/CH00033 ._CH',             # 04
        'ED6_DT07/CH00043 ._CH',             # 05
        'ED6_DT07/CH00063 ._CH',             # 06
        'ED6_DT07/CH00073 ._CH',             # 07
        'ED6_DT27/CH03083 ._CH',             # 08
        'ED6_DT07/CH00020 ._CH',             # 09
        'ED6_DT07/CH00050 ._CH',             # 0A
        'ED6_DT07/CH00030 ._CH',             # 0B
        'ED6_DT07/CH00040 ._CH',             # 0C
        'ED6_DT07/CH00060 ._CH',             # 0D
        'ED6_DT07/CH00070 ._CH',             # 0E
        'ED6_DT27/CH03080 ._CH',             # 0F
        'ED6_DT07/CH02323 ._CH',             # 10
        'ED6_DT26/CH20235 ._CH',             # 11
        'ED6_DT26/CH20240 ._CH',             # 12
        'ED6_DT26/CH20402 ._CH',             # 13
        'ED6_DT06/CH20021 ._CH',             # 14
        'ED6_DT26/CH20372 ._CH',             # 15
        'ED6_DT26/CH20395 ._CH',             # 16
        'ED6_DT26/CH20394 ._CH',             # 17
        'ED6_DT26/CH20393 ._CH',             # 18
        'ED6_DT07/CH00150 ._CH',             # 19
        'ED6_DT07/CH00151 ._CH',             # 1A
        'ED6_DT07/CH00152 ._CH',             # 1B
        'ED6_DT07/CH00153 ._CH',             # 1C
        'ED6_DT07/CH00154 ._CH',             # 1D
        'ED6_DT07/CH00159 ._CH',             # 1E
        'ED6_DT06/CH20137 ._CH',             # 1F
        'ED6_DT07/CH00170 ._CH',             # 20
        'ED6_DT07/CH00171 ._CH',             # 21
        'ED6_DT07/CH00172 ._CH',             # 22
        'ED6_DT07/CH00173 ._CH',             # 23
        'ED6_DT07/CH00174 ._CH',             # 24
        'ED6_DT07/CH00178 ._CH',             # 25
        'ED6_DT07/CH01230 ._CH',             # 26
        'ED6_DT07/CH01220 ._CH',             # 27
        'ED6_DT27/CH03790 ._CH',             # 28
        'ED6_DT07/CH01000 ._CH',             # 29
        'ED6_DT07/CH01020 ._CH',             # 2A
        'ED6_DT27/CH03860 ._CH',             # 2B
        'ED6_DT26/CH20408 ._CH',             # 2C
    )

    AddCharChipPat(
        'ED6_DT06/CH20045P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT07/CH00023P._CP',             # 02
        'ED6_DT07/CH00053P._CP',             # 03
        'ED6_DT07/CH00033P._CP',             # 04
        'ED6_DT07/CH00043P._CP',             # 05
        'ED6_DT07/CH00063P._CP',             # 06
        'ED6_DT07/CH00073P._CP',             # 07
        'ED6_DT27/CH03083P._CP',             # 08
        'ED6_DT07/CH00020P._CP',             # 09
        'ED6_DT07/CH00050P._CP',             # 0A
        'ED6_DT07/CH00030P._CP',             # 0B
        'ED6_DT07/CH00040P._CP',             # 0C
        'ED6_DT07/CH00060P._CP',             # 0D
        'ED6_DT07/CH00070P._CP',             # 0E
        'ED6_DT27/CH03080P._CP',             # 0F
        'ED6_DT07/CH02323P._CP',             # 10
        'ED6_DT26/CH20235P._CP',             # 11
        'ED6_DT26/CH20240P._CP',             # 12
        'ED6_DT26/CH20402P._CP',             # 13
        'ED6_DT06/CH20021P._CP',             # 14
        'ED6_DT26/CH20372P._CP',             # 15
        'ED6_DT26/CH20395P._CP',             # 16
        'ED6_DT26/CH20394P._CP',             # 17
        'ED6_DT26/CH20393P._CP',             # 18
        'ED6_DT07/CH00150P._CP',             # 19
        'ED6_DT07/CH00151P._CP',             # 1A
        'ED6_DT07/CH00152P._CP',             # 1B
        'ED6_DT07/CH00153P._CP',             # 1C
        'ED6_DT07/CH00154P._CP',             # 1D
        'ED6_DT07/CH00159P._CP',             # 1E
        'ED6_DT06/CH20137P._CP',             # 1F
        'ED6_DT07/CH00170P._CP',             # 20
        'ED6_DT07/CH00171P._CP',             # 21
        'ED6_DT07/CH00172P._CP',             # 22
        'ED6_DT07/CH00173P._CP',             # 23
        'ED6_DT07/CH00174P._CP',             # 24
        'ED6_DT07/CH00178P._CP',             # 25
        'ED6_DT07/CH01230P._CP',             # 26
        'ED6_DT07/CH01220P._CP',             # 27
        'ED6_DT27/CH03790P._CP',             # 28
        'ED6_DT07/CH01000P._CP',             # 29
        'ED6_DT07/CH01020P._CP',             # 2A
        'ED6_DT27/CH03860P._CP',             # 2B
        'ED6_DT26/CH20408P._CP',             # 2C
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3480,
        Z                   = -2000,
        Y                   = 43140,
        Direction           = 128,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 2070,
        Z                   = -2000,
        Y                   = 38510,
        Direction           = 189,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -9480,
        Z                   = 0,
        Y                   = 62260,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -8170,
        Z                   = 500,
        Y                   = 40910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -11480,
        Z                   = -2000,
        Y                   = 34670,
        Direction           = 267,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327700,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -37610,
        Z                   = -2000,
        Y                   = 44850,
        Direction           = 178,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262188,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262188,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65580,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -8640,
        Z                   = 0,
        Y                   = 96040,
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


    DeclEvent(
        X                   = -46710,
        Y                   = -2400,
        Z                   = 40980,
        Range               = -43080,
        Unknown_10          = 0xFFFFFE70,
        Unknown_14          = 0xA604,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = -5850,
        Y                   = -1000,
        Z                   = 80880,
        Range               = -10140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x14438,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )


    DeclActor(
        TriggerX            = -9910,
        TriggerZ            = 500,
        TriggerY            = 47790,
        TriggerRange        = 800,
        ActorX              = -9910,
        ActorZ              = 1500,
        ActorY              = 47790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4980,
        TriggerZ            = 4000,
        TriggerY            = 54310,
        TriggerRange        = 800,
        ActorX              = -4980,
        ActorZ              = 5000,
        ActorY              = 54310,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5090,
        TriggerZ            = 4000,
        TriggerY            = 47820,
        TriggerRange        = 800,
        ActorX              = -5090,
        ActorZ              = 5000,
        ActorY              = 47820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2910,
        TriggerZ            = -2000,
        TriggerY            = 32500,
        TriggerRange        = 1000,
        ActorX              = -2980,
        ActorZ              = -3000,
        ActorY              = 29380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_622",          # 00, 0
        "Function_1_757",          # 01, 1
        "Function_2_812",          # 02, 2
        "Function_3_98F",          # 03, 3
        "Function_4_AD6",          # 04, 4
        "Function_5_D04",          # 05, 5
        "Function_6_E11",          # 06, 6
        "Function_7_17F3",         # 07, 7
        "Function_8_1CFC",         # 08, 8
        "Function_9_1F58",         # 09, 9
        "Function_10_1FA0",        # 0A, 10
        "Function_11_1FE8",        # 0B, 11
        "Function_12_2030",        # 0C, 12
        "Function_13_304E",        # 0D, 13
        "Function_14_3072",        # 0E, 14
        "Function_15_3096",        # 0F, 15
        "Function_16_30BA",        # 10, 16
        "Function_17_30CA",        # 11, 17
        "Function_18_315E",        # 12, 18
        "Function_19_31BC",        # 13, 19
        "Function_20_32F8",        # 14, 20
        "Function_21_3434",        # 15, 21
        "Function_22_34B9",        # 16, 22
        "Function_23_353E",        # 17, 23
        "Function_24_3860",        # 18, 24
        "Function_25_45E0",        # 19, 25
        "Function_26_4773",        # 1A, 26
        "Function_27_47CA",        # 1B, 27
        "Function_28_48F9",        # 1C, 28
    )


    def Function_0_622(): pass

    label("Function_0_622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_64A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B1("T1500_n")
    Event(0, 12)
    Jump("loc_67A")

    label("loc_64A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_67A")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_B1("T1500_y")
    OP_71(0x1, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F(0x64, 0x64)
    Event(0, 24)

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6FA")
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696")
    ClearChrFlags(0x17, 0x80)
    Jump("loc_6F7")

    label("loc_696")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_6BD")
    SetChrChipByIndex(0x16, 42)
    SetChrPos(0x16, -8170, 500, 40910, 180)
    OP_43(0x16, 0x0, 0x0, 0x2)
    Jump("loc_6DC")

    label("loc_6BD")

    SetChrChipByIndex(0x16, 44)
    SetChrFlags(0x16, 0x10)
    OP_44(0x16, 0x0)
    SetChrPos(0x16, -45020, -2000, 38510, 180)

    label("loc_6DC")

    SetChrPos(0x15, -22540, 0, 47490, 180)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x10)

    label("loc_6F7")

    Jump("loc_756")

    label("loc_6FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_704")
    Jump("loc_756")

    label("loc_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_729")
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 2440, -2000, 38510, 159)
    Jump("loc_756")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_745")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_742")
    SetChrFlags(0x15, 0x10)

    label("loc_742")

    Jump("loc_756")

    label("loc_745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_756")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_756")

    Return()

    # Function_0_622 end

    def Function_1_757(): pass

    label("Function_1_757")

    OP_16(0x2, 0xFA0, 0xFFFDC998, 0xFFFEE2D8, 0x230046)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_795")
    OP_B1("T1500_n")
    OP_71(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_788")
    Jump("loc_792")

    label("loc_788")

    OP_D2(0x600B6, 0x600BB, 0x2C)

    label("loc_792")

    Jump("loc_7C4")

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_7A8")
    OP_B1("T1500_n")
    Jump("loc_7C4")

    label("loc_7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_END)), "loc_7BB")
    OP_B1("T1500_y")
    Jump("loc_7C4")

    label("loc_7BB")

    OP_B1("T1500_n")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F7")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x0)
    OP_72(0x4, 0x10)
    OP_72(0x5, 0x10)
    OP_72(0x6, 0x10)
    Jump("loc_80C")

    label("loc_7F7")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_10(0x2, 0x1)
    OP_10(0x3, 0x1)
    OP_10(0x4, 0x1)

    label("loc_80C")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_757 end

    def Function_2_812(): pass

    label("Function_2_812")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_837")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_979")

    label("loc_837")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_979")

    label("loc_850")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_869")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_979")

    label("loc_869")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_882")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_979")

    label("loc_882")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_89B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_979")

    label("loc_89B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B4")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_979")

    label("loc_8B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_979")

    label("loc_8CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_979")

    label("loc_8E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_979")

    label("loc_8FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_918")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_979")

    label("loc_918")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_931")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_979")

    label("loc_931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_979")

    label("loc_94A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_963")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_979")

    label("loc_963")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_979")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_979")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_98E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_979")

    label("loc_98E")

    Return()

    # Function_2_812 end

    def Function_3_98F(): pass

    label("Function_3_98F")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_9EC")

    ChrTalk(    #0
        0xFE,
        (
            "只有钓鱼是\x01",
            "无论如何都不能停止的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "我想就算被婆婆质问\x01",
            "也会继续下去的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD2")

    label("loc_9EC")


    ChrTalk(    #2
        0xFE,
        (
            "呼，哎呀哎呀\x01",
            "终于回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "最近的骚动也解决了，\x01",
            "就慢慢享受钓鱼的乐趣吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "哎呀，只有钓鱼\x01",
            "那可是无论如何都不会放弃的爱好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "我想就算被婆婆质问\x01",
            "也会继续下去的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x386, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACC")

    ChrTalk(    #6
        0x101,
        "#1007F（好，好勇敢的发言呀……）\x02",
    )

    CloseMessageWindow()

    label("loc_ACC")

    OP_A2(0x1C32)
    OP_A2(0x6)

    label("loc_AD2")

    TalkEnd(0x1C)
    Return()

    # Function_3_98F end

    def Function_4_AD6(): pass

    label("Function_4_AD6")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B60")

    ChrTalk(    #7
        0xFE,
        "呼，多清爽的天气呀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "钓鱼比赛又赢了老公，\x01",
            "真是心情爽到了极点。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "呵呵，竟然想要向我挑战，\x01",
            "还早个一百年！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF4")

    label("loc_B60")


    ChrTalk(    #10
        0xFE,
        (
            "呵呵，今天也是个\x01",
            "清爽的天气呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "和老公的旅行今天是最后一天了。\x01",
            "晚上就要回王都了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "因为钓鱼赢了老公，\x01",
            "今天可以高高兴兴地回家了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_BF4")

    Jump("loc_D00")

    label("loc_BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C54")

    ChrTalk(    #13
        0xFE,
        (
            "我怎么说也是\x01",
            "『钓公师团』的团员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "对鱼竿的运用\x01",
            "我可是很有自信的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D00")

    label("loc_C54")


    ChrTalk(    #15
        0xFE,
        (
            "我们是从王都\x01",
            "大老远过来钓鱼的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "啊啊，我答应教老公钓鱼的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "别看我这个样子，怎么说\x01",
            "我也是『钓公师团』的团员哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "呵呵，对鱼竿的运用\x01",
            "我可是很有自信的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D00")

    TalkEnd(0x13)
    Return()

    # Function_4_AD6 end

    def Function_5_D04(): pass

    label("Function_5_D04")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_E0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D76")

    ChrTalk(    #19
        0xFE,
        (
            "嗯，在这次旅行中\x01",
            "多少要挽回些面子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "要是一直输给妻子\x01",
            "这做丈夫的威严可就保不住了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E0D")

    label("loc_D76")


    ChrTalk(    #21
        0xFE,
        (
            "话说本来是我\x01",
            "开始带她钓鱼的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "不知什么时候\x01",
            "妻子也迷上了钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "更可怕的是钓鱼技术\x01",
            "已经超过我了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "稍微偷学点技术\x01",
            "挽回点颜面吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E0D")

    TalkEnd(0x14)
    Return()

    # Function_5_D04 end

    def Function_6_E11(): pass

    label("Function_6_E11")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_E1E")
    OP_A2(0x2)

    label("loc_E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在前篇遇到过斯丁克】\x01",        # 0
            "【◇在前篇没遇到过斯丁克】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E8E"),
        (1, "loc_E94"),
        (SWITCH_DEFAULT, "loc_E9A"),
    )


    label("loc_E8E")

    OP_A2(0x2)
    Jump("loc_E9A")

    label("loc_E94")

    OP_A3(0x2)
    Jump("loc_E9A")

    label("loc_E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133E")

    ChrTalk(    #25
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(    #26
        0x101,
        (
            "#1000F啊，你是……\x02\x03",

            "斯丁克……对吧？\x01",
            "柏斯支部的游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #27
        0xFE,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "卢格兰老爷子提到的那个\x01",
            "那个正游击士的新人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1011F卢格兰爷爷说的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1041F这样的话，大概\x01",
            "说的是我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1000F唔，那种情况下是当然的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "最近在拉文努村\x01",
            "似乎没发生什么混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "你们就\x01",
            "专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1335")

    label("loc_104D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109E")

    ChrTalk(    #36
        0x103,
        "#020F好久不见，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x103, 400)
    Jump("loc_10F8")

    label("loc_109E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F1")

    ChrTalk(    #37
        0x106,
        "#050F很久不见了，斯丁克。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_10F8")

    label("loc_10F1")

    TurnDirection(0xFE, 0x101, 400)

    label("loc_10F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_117B")

    ChrTalk(    #38
        0xFE,
        "雪拉扎德吗…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        "#020F不，那种情况下是当然的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E9")

    label("loc_117B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11FE")

    ChrTalk(    #42
        0xFE,
        "阿加特吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x106,
        "#051F哪里，那是我们的义务啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E9")

    label("loc_11FE")


    ChrTalk(    #46
        0xFE,
        "你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "卢格兰老爷子提到的那个\x01",
            "那个正游击士的新人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1011F卢格兰爷爷说的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1041F这样的话，大概\x01",
            "我想是我们的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "你们在之前龙的骚动中\x01",
            "帮助过我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "……非常感谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1000F唔，那种情况下是当然的啊。\x02",
    )

    CloseMessageWindow()

    label("loc_12E9")


    ChrTalk(    #53
        0xFE,
        (
            "最近在柏斯地区\x01",
            "似乎没发生什么混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "你们就\x01",
            "专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1335")

    OP_A2(0x1A53)
    OP_A2(0x3)
    Jump("loc_1474")

    label("loc_133E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1394")

    ChrTalk(    #55
        0xFE,
        (
            "最近在柏斯地区\x01",
            "似乎没发生什么混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "你们就\x01",
            "专心完成自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1474")

    label("loc_1394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1426")

    ChrTalk(    #57
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "导力器停止现象\x01",
            "是在王国全境发生的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "这个状况要\x01",
            "持续到什么时候呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1474")

    label("loc_1426")


    ChrTalk(    #61
        0xFE,
        (
            "这样的状况拖太久的话\x01",
            "就非常危险了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "不过……\x01",
            "就现状也是毫无办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1474")

    Jump("loc_17EF")

    label("loc_1477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_17EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_158E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_14D2")

    ChrTalk(    #63
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "……龙的事情就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_154D")

    label("loc_14D2")


    ChrTalk(    #65
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "你们和军队协力\x01",
            "一起追捕龙呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "……那边就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_154D")

    Jump("loc_158B")

    label("loc_1550")


    ChrTalk(    #69
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "……龙的事情就拜托了。\x02",
    )

    CloseMessageWindow()

    label("loc_158B")

    Jump("loc_17EF")

    label("loc_158E")


    ChrTalk(    #71
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_165C")

    ChrTalk(    #72
        0x101,
        (
            "#1011F啊，你是……\x02\x03",

            "斯丁克……对吧？\x01",
            "柏斯支部的游击士。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #73
        0xFE,
        (
            "你是……\x01",
            "那时的准游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "噢，看样子已经升任正游击士了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1016F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16AB")

    label("loc_165C")


    ChrTalk(    #76
        0x101,
        (
            "#1015F（啊？这个人……）\x02\x03",

            "（仔细看看的话，\x01",
            "　竟然也戴着游击士的徽章啊？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AB")


    ChrTalk(    #77
        0x106,
        (
            "#050F很久不见了，斯丁克。\x02\x03",

            "竟然来到这种地方，\x01",
            "今天来是消灭通缉魔兽的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #78
        0xFE,
        "阿加特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "是来调查龙的事件吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#050F啊啊，和军队一起。\x02\x03",

            "从这里出发\x01",
            "向迷雾峡谷方向移动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "琐碎的事\x01",
            "就由我来做吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "……那边就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        "#051F喔，就交给我们吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x3)

    label("loc_17EF")

    TalkEnd(0x15)
    Return()

    # Function_6_E11 end

    def Function_7_17F3(): pass

    label("Function_7_17F3")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_1964")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D6")

    ChrTalk(    #85
        0xFE,
        (
            "嗯，真没想到\x01",
            "能钓到瓦雷利亚湖的『湖之主』呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "不过，钓鱼就是和自然战斗，\x01",
            "并且是一种挑战自我的过程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "就算没有『湖之主』\x01",
            "挑战的对手也数以万计。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "对了，去外国远征\x01",
            "说不定也可以呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1961")

    label("loc_18D6")


    ChrTalk(    #89
        0xFE,
        (
            "就算没有『湖之主』\x01",
            "挑战的对手也数以万计。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "钓鱼就是和自然战斗，\x01",
            "并且是一种挑战自我的过程。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "对了，去外国远征\x01",
            "说不定也不错呀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1961")

    Jump("loc_1A4A")

    label("loc_1964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A13")

    ChrTalk(    #92
        0xFE,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "……喂，来吧……………\x01",
            "瓦雷利亚湖的『湖之主』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1A4A")

    label("loc_1A13")


    ChrTalk(    #95
        0xFE,
        (
            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A4A")

    Jump("loc_1CF8")

    label("loc_1A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_END)), "loc_1B91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(    #96
        0xFE,
        (
            "这次为了能钓上『湖之主』，\x01",
            "我做好充分准备来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "嗯，没想到\x01",
            "被抢先了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "说实话真是受打击了呀，但是\x01",
            "钓鱼并没有结束。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "必须重新振作起来\x01",
            "寻找新的目标。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1B8E")

    label("loc_1B11")


    ChrTalk(    #100
        0xFE,
        (
            "没想到被抢先\x01",
            "钓上『湖之主』了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "说实话真是受打击呀，但是\x01",
            "钓鱼并没有结束。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "必须重新振作起来\x01",
            "寻找新的目标。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B8E")

    Jump("loc_1CF8")

    label("loc_1B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C67")

    ChrTalk(    #103
        0xFE,
        (
            "这次为了能钓上『湖之主』，\x01",
            "我做好充分准备来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "那、那个浮在天空中的\x01",
            "像岛一样的物体到底是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "平时经常吃的黑鲑和\x01",
            "鲑鱼也都钓不到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "也许是映在湖里的影子，\x01",
            "对鱼产生了影响吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1CF8")

    label("loc_1C67")


    ChrTalk(    #107
        0xFE,
        (
            "这次为了能钓上『湖之主』，\x01",
            "我做好充分准备来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "平时经常吃的黑鲑和\x01",
            "鲑鱼也都钓不到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "唔唔，这也许是场\x01",
            "比试忍耐力的较量吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF8")

    TalkEnd(0x16)
    Return()

    # Function_7_17F3 end

    def Function_8_1CFC(): pass

    label("Function_8_1CFC")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDD")

    ChrTalk(    #110
        0xFE,
        "哟，游击士们。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 5)), scpexpr(EXPR_END)), "loc_1D99")

    ChrTalk(    #111
        0x101,
        "#1000F啊，你好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        "#1040F你是来购物的吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #113
        0xFE,
        "哈哈，消息真快。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "没有错。\x01",
            "被他缠了好久只好答应。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E45")

    label("loc_1D99")


    ChrTalk(    #115
        0x101,
        (
            "#1001F啊，你好……\x02\x03",

            "#1004F……嗯，咦！？\x01",
            "怎么会有亲卫队的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#1044F从『埃尔赛尤』\x01",
            "上面来的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #117
        0xFE,
        "没错，划船过来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "其实我是被赶出来\x01",
            "采购食物的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E45")


    ChrTalk(    #119
        0x101,
        "#1016F啊哈哈，是这样呀。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #120
        0xFE,
        (
            "我是工作的时候\x01",
            "被硬拉过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "本来这是利奥的工作，\x01",
            "但那家伙跑了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "哈，我也真是\x01",
            "个苯好人呀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2096)
    Jump("loc_1F54")

    label("loc_1EDD")


    ChrTalk(    #123
        0xFE,
        (
            "不过，话说回来\x01",
            "艾柯那家伙真慢呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "不过是买些食物，\x01",
            "怎么会买这么久呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "真是，正是因为这样\x01",
            "我才不想去的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F54")

    TalkEnd(0x17)
    Return()

    # Function_8_1CFC end

    def Function_9_1F58(): pass

    label("Function_9_1F58")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #126
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_9_1F58 end

    def Function_10_1FA0(): pass

    label("Function_10_1FA0")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_10_1FA0 end

    def Function_11_1FE8(): pass

    label("Function_11_1FE8")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #128
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_11_1FE8 end

    def Function_12_2030(): pass

    label("Function_12_2030")

    EventBegin(0x0)
    OP_72(0x1, 0x4)
    OP_71(0x1, 0x40)
    OP_72(0x8, 0x4)
    OP_71(0x8, 0x40)
    OP_71(0x3, 0x4)
    OP_A1(0x10, 0x8)
    OP_A1(0x11, 0x1)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, -8530, -2500, 32509, 0)
    SetChrPos(0x11, -6040, -2500, 32020, 0)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xC, 0x4)
    ClearChrFlags(0x9, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x8, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0xD, 0x1)
    SetChrBattleFlags(0xA, 0x20)
    SetChrBattleFlags(0xC, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xE, 0x20)
    SetChrBattleFlags(0xB, 0x20)
    SetChrBattleFlags(0xF, 0x20)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0xD, 0x20)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0xA, 0)
    OP_48()
    OP_89(0xA, -6050, -2400, 29730, 180)
    OP_89(0xC, -6520, -2400, 31060, 180)
    OP_89(0x9, -5840, -2400, 30990, 180)
    OP_89(0xD, -6350, -2400, 32350, 180)
    OP_89(0x101, -8940, -2400, 31400, 180)
    OP_89(0xB, -8270, -2400, 31410, 180)
    OP_89(0xE, -8950, -2400, 32740, 180)
    OP_89(0xF, -8450, -2400, 30470, 0)
    OP_89(0x8, -8280, -2400, 32740, 180)
    OP_6D(-6750, -2800, 30900, 0)
    OP_67(0, 9030, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(280, 0)

    def lambda_2212():

        label("loc_2212")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_2212")

    QueueWorkItem2(0xA, 2, lambda_2212)
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    LoadEffect(0x1, "map\\\\mp013_01.eff")
    PlayEffect(0x0, 0x0, 0x10, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x10, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x11, 0, -300, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0x11, 0, -300, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    Sleep(300)
    OP_22(0x92, 0x0, 0x46)

    def lambda_2334():
        OP_6D(-5900, -2530, 24130, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2334)

    def lambda_234C():
        OP_67(0, 11840, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_234C)

    def lambda_2364():
        OP_6C(49000, 10000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2364)

    def lambda_2374():
        OP_6E(298, 10000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2374)
    OP_43(0x10, 0x0, 0x0, 0x13)
    Sleep(200)
    OP_43(0x11, 0x0, 0x0, 0x14)
    WaitChrThread(0x10, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_23(0x92)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #129
        (
            "\x07\x05上午，租借了小船\x01",
            "在湖上戏耍，十分开心……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_44(0xA, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xF, 0x20)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xC, 0x1)
    SetChrFlags(0x9, 0x1)
    SetChrFlags(0xE, 0x1)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xF, 0x1)
    SetChrFlags(0x8, 0x1)
    SetChrFlags(0xD, 0x1)
    ClearChrBattleFlags(0xA, 0x20)
    ClearChrBattleFlags(0xC, 0x20)
    ClearChrBattleFlags(0x9, 0x20)
    ClearChrBattleFlags(0xE, 0x20)
    ClearChrBattleFlags(0xB, 0x20)
    ClearChrBattleFlags(0xF, 0x20)
    ClearChrBattleFlags(0x8, 0x20)
    ClearChrBattleFlags(0xD, 0x20)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0xA, 0)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0xE, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xC, 6)
    SetChrChipByIndex(0xD, 14)
    SetChrChipByIndex(0xE, 8)
    SetChrSubChip(0xB, 2)
    SetChrSubChip(0xC, 2)
    SetChrPos(0x101, -900, -650, 43530, 90)
    SetChrPos(0x8, -1320, -400, 42540, 90)
    SetChrPos(0xA, -1370, -650, 41510, 90)
    SetChrPos(0xB, 660, -1800, 48640, 90)
    SetChrPos(0xC, 660, -1800, 47590, 90)
    SetChrPos(0xE, -1010, -650, 44400, 90)
    SetChrFlags(0x9, 0x800)
    SetChrPos(0x9, 2350, -2000, 40500, 0)
    SetChrPos(0xD, 2390, -2000, 45720, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0x9, 27)
    OP_6D(1600, -1260, 44290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(295000, 0)
    OP_6E(272, 0)
    LoadEffect(0x0, "scraft\\\\sc000_00.eff")
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_25DA():
        OP_6D(2290, -1260, 42460, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25DA)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 31)
    SetChrChipByIndex(0xD, 32)
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0xD)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xD, 0x618, 0xFFFFF830, 0xAC08, 0x15E, 0xFA0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xD, 0xA5A, 0xFFFFF830, 0xA8B6, 0x15E, 0x1770)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_264A():
        OP_96(0xD, 0x8D4, 0xFFFFF830, 0xA370, 0xC8, 0x1F40)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_264A)
    Sleep(100)
    SetChrChipByIndex(0xD, 34)

    def lambda_2672():
        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2672)
    OP_22(0x208, 0x0, 0x64)

    def lambda_2687():

        label("loc_2687")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_2687")

    QueueWorkItem2(0x9, 2, lambda_2687)

    def lambda_2698():
        OP_96(0x9, 0xC6C, 0xFFFFF830, 0xA078, 0xFA, 0x1F40)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2698)
    SetChrChipByIndex(0x9, 27)
    SetChrSubChip(0x9, 0)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xD, 0x0)
    TurnDirection(0xD, 0x9, 0)

    def lambda_26D1():
        OP_96(0xD, 0x604, 0xFFFFF830, 0xA168, 0xFA, 0x1770)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_26D1)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 32)
    Sleep(100)
    OP_44(0x9, 0x2)

    def lambda_2702():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2702)

    def lambda_2712():
        OP_8F(0xFE, 0x906, 0xFFFFF830, 0xA0AA, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2712)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(100)
    OP_96(0xD, 0x956, 0xFFFFF830, 0xA410, 0xFA, 0x1B58)
    TurnDirection(0xD, 0x9, 0)
    WaitChrThread(0x9, 0x2)
    TurnDirection(0x9, 0xD, 0)
    SetChrChipByIndex(0x9, 30)

    def lambda_276B():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_276B)
    WaitChrThread(0x9, 0x1)

    def lambda_2780():
        OP_99(0xFE, 0xA, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2780)
    Sleep(100)
    OP_43(0x101, 0x0, 0x0, 0xF)
    PlayEffect(0x1, 0x0, 0xD, 0, 500, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xD, 0)
    SetChrChipByIndex(0xD, 35)
    OP_96(0xD, 0x956, 0xFFFFF830, 0xAAC8, 0xFA, 0x1388)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 36)
    SetChrSubChip(0xD, 3)
    OP_8F(0xD, 0x956, 0xFFFFF830, 0xAEB0, 0x1388, 0x0)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 26)
    SetChrFlags(0xD, 0x8000)
    OP_96(0x9, 0x8A2, 0xFFFFF830, 0x9BAA, 0xC8, 0xFA0)
    SetChrChipByIndex(0xD, 32)
    SetChrSubChip(0xD, 0)

    def lambda_284A():
        OP_8F(0x9, 0x88E, 0xFFFFF830, 0xA78A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_284A)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_286F():
        OP_96(0xFE, 0x870, 0xFFFFF830, 0xAAC8, 0x190, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_286F)
    SetChrChipByIndex(0x9, 27)

    def lambda_2892():
        OP_99(0x9, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2892)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    Sleep(200)

    def lambda_28B1():
        OP_8C(0xFE, 270, 800)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28B1)

    def lambda_28BF():
        OP_8F(0xFE, 0xA82, 0xFFFFF830, 0xAE24, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_28BF)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0xD, 0)
    SetChrChipByIndex(0x9, 30)

    def lambda_28EB():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_28EB)
    WaitChrThread(0x9, 0x1)

    def lambda_2900():
        OP_99(0xFE, 0xA, 0xE, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2900)

    def lambda_2910():
        TurnDirection(0xD, 0x9, 0)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2910)
    Sleep(100)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0xD, 0x4)

    def lambda_2932():
        OP_96(0xD, 0xC80, 0xFFFFFAEC, 0xB6B2, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2932)
    WaitChrThread(0xD, 0x2)
    OP_43(0x101, 0x0, 0x0, 0xE)
    Sleep(100)
    WaitChrThread(0x9, 0x1)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 31)
    TurnDirection(0x9, 0xD, 0)
    SetChrChipByIndex(0xD, 34)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2981():
        OP_96(0xD, 0x898, 0xFFFFF830, 0xAD34, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2981)
    Sleep(100)

    def lambda_29A4():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_29A4)
    Sleep(100)
    OP_22(0x1FB, 0x0, 0x64)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0x9, 0, 1000, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0x9, 0x20)
    OP_43(0x101, 0x0, 0x0, 0xF)
    OP_8F(0x9, 0x708, 0xFFFFF830, 0xA794, 0x1770, 0x0)
    WaitChrThread(0xD, 0x1)
    OP_43(0x101, 0x0, 0x0, 0x10)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2A35():
        OP_96(0xFE, 0x816, 0xFFFFF830, 0xAA96, 0xC7, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A35)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 37)
    SetChrSubChip(0xD, 0)
    OP_99(0xD, 0x1, 0x3, 0x708)

    def lambda_2A75():
        OP_9E(0xFE, 0x32, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A75)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    PlayEffect(0x1, 0x0, 0x9, 0, 1300, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x106, 0x3, 0x0, 0x12)

    def lambda_2ADC():
        OP_8F(0x9, 0x6B8, 0xFFFFF830, 0xA53C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2ADC)
    Sleep(200)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)

    def lambda_2B0D():

        label("loc_2B0D")

        OP_9E(0xFE, 0x32, 0x0, 0x64, 0x1388)
        OP_48()
        Jump("loc_2B0D")

    QueueWorkItem2(0x9, 1, lambda_2B0D)
    OP_99(0xD, 0x8, 0xB, 0x5DC)
    OP_99(0xD, 0x8, 0xB, 0x5DC)
    OP_A2(0x5)
    OP_99(0xD, 0x10, 0x12, 0x5DC)

    def lambda_2B48():
        OP_99(0xFE, 0x18, 0x1B, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2B48)
    PlayEffect(0x1, 0x0, 0x9, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x64, 0x0, 0x1388, 0x3E8)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    OP_22(0x22A, 0x0, 0x64)
    SetChrChipByIndex(0x9, 28)
    OP_43(0x9, 0x1, 0x0, 0x11)
    WaitChrThread(0xD, 0x2)
    SetChrSubChip(0xD, 32)
    ClearChrFlags(0xD, 0x4)

    def lambda_2BC8():
        OP_96(0xFE, 0x898, 0xFFFFF830, 0xAD34, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2BC8)

    def lambda_2BE6():
        OP_99(0xFE, 0x28, 0x2C, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2BE6)
    WaitChrThread(0xD, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xD, 0x2)
    ClearChrFlags(0xD, 0x2)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xD, 0x40)
    OP_8C(0xD, 180, 0)
    SetChrChipByIndex(0xD, 32)
    SetChrSubChip(0xD, 0)
    WaitChrThread(0x9, 0x1)
    Sleep(1000)

    def lambda_2C2F():

        label("loc_2C2F")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_2C2F")

    QueueWorkItem2(0x9, 3, lambda_2C2F)
    Sleep(200)
    OP_99(0x9, 0x3, 0x0, 0x5DC)
    Fade(250)
    OP_44(0x9, 0x3)
    SetChrFlags(0x9, 0x2)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x9, 31)
    SetChrSubChip(0x9, 3)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #130
        (
            "\x07\x05中午，大家一起吃过午饭后，\x01",
            "开心地做健身运动……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x800)
    ClearChrFlags(0xD, 0x8000)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xE, 0)
    SetChrSubChip(0xD, 0)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x101, 21)
    SetChrChipByIndex(0xE, 24)
    SetChrChipByIndex(0xD, 23)
    SetChrChipByIndex(0x9, 22)
    SetChrPos(0x18, -11490, 1100, 41030, 0)
    SetChrPos(0x19, -10530, 1100, 41040, 0)
    SetChrPos(0x1A, -5850, 1100, 41090, 0)
    SetChrPos(0x1B, -4630, 1100, 41090, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrPos(0xD, -11840, -2300, 33400, 270)
    SetChrPos(0x101, -10130, -2300, 33190, 90)
    SetChrPos(0xE, -3920, -2300, 34150, 270)
    SetChrPos(0x9, -2100, -2300, 33480, 90)
    SetChrPos(0xA, -12850, 700, 41400, 90)
    SetChrPos(0x8, -9540, 700, 41200, 270)
    SetChrPos(0xC, -6940, 700, 41230, 90)
    SetChrPos(0xB, -3850, 700, 41270, 270)
    SetChrPos(0xF, -7030, 1400, 40400, 180)
    SetChrSubChip(0xA, 2)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0xB, 1)
    SetChrSubChip(0xC, 2)
    SetChrChipByIndex(0xA, 4)
    SetChrChipByIndex(0x8, 2)
    SetChrChipByIndex(0xB, 5)
    SetChrChipByIndex(0xC, 6)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x1D, -10730, -2000, 33190, 0)
    SetChrPos(0x1E, -3320, -2000, 34150, 0)
    SetChrPos(0x1F, -2700, -2000, 33480, 0)
    SetChrPos(0x20, -11140, -2000, 33500, 0)
    OP_6D(-8220, -2000, 45620, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(370, 0)
    LoadEffect(0x0, "scraft\\\\sc001_05.eff")

    def lambda_2EFC():

        label("loc_2EFC")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2EFC")

    QueueWorkItem2(0x101, 3, lambda_2EFC)

    def lambda_2F0F():

        label("loc_2F0F")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2F0F")

    QueueWorkItem2(0xE, 3, lambda_2F0F)

    def lambda_2F22():

        label("loc_2F22")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2F22")

    QueueWorkItem2(0xD, 3, lambda_2F22)

    def lambda_2F35():

        label("loc_2F35")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_2F35")

    QueueWorkItem2(0x9, 3, lambda_2F35)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_2F57():
        OP_6D(-7960, -2300, 38310, 6000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2F57)

    def lambda_2F6F():
        OP_67(0, 4840, -10000, 6000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2F6F)

    def lambda_2F87():
        OP_6C(341000, 6000)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_2F87)

    def lambda_2F97():
        OP_6E(465, 6000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2F97)
    WaitChrThread(0xD, 0x1)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #131
        (
            "\x07\x05下午，一边垂钓\x01",
            "一边悠闲地度过时间……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #132
        (
            "\x07\x05快乐又安稳的时间\x01",
            "很快就过去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1510   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2030 end

    def Function_13_304E(): pass

    label("Function_13_304E")

    SetChrSubChip(0xE, 2)
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(100)
    SetChrSubChip(0xA, 2)
    Return()

    # Function_13_304E end

    def Function_14_3072(): pass

    label("Function_14_3072")

    SetChrSubChip(0xE, 1)
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(100)
    SetChrSubChip(0x8, 1)
    Sleep(100)
    SetChrSubChip(0xA, 1)
    Return()

    # Function_14_3072 end

    def Function_15_3096(): pass

    label("Function_15_3096")

    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrSubChip(0xA, 0)
    Sleep(100)
    SetChrSubChip(0xE, 0)
    Return()

    # Function_15_3096 end

    def Function_16_30BA(): pass

    label("Function_16_30BA")

    SetChrSubChip(0x101, 2)
    Sleep(100)
    SetChrSubChip(0xE, 2)
    Return()

    # Function_16_30BA end

    def Function_17_30CA(): pass

    label("Function_17_30CA")


    def lambda_30D0():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_30D0)
    Sleep(100)

    def lambda_30F0():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_30F0)
    Sleep(100)

    def lambda_3110():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3110)
    Sleep(100)

    def lambda_3130():
        OP_8F(0xFE, 0xBE0, 0xFFFFF830, 0x9F88, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3130)
    WaitChrThread(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 29)
    OP_99(0x9, 0x0, 0x3, 0x5DC)
    Return()

    # Function_17_30CA end

    def Function_18_315E(): pass

    label("Function_18_315E")

    Sleep(200)

    label("loc_3163")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31BB")
    OP_22(0x321, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x9, 0, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_31B3")
    OP_23(0x321)
    Jump("loc_31BB")

    label("loc_31B3")

    Sleep(100)
    Jump("loc_3163")

    label("loc_31BB")

    Return()

    # Function_18_315E end

    def Function_19_31BC(): pass

    label("Function_19_31BC")


    def lambda_31C2():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31C2)
    Sleep(300)

    def lambda_31E2():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31E2)
    Sleep(300)

    def lambda_3202():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3202)
    Sleep(300)

    def lambda_3222():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3222)
    Sleep(300)

    def lambda_3242():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3242)
    Sleep(300)

    def lambda_3262():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3262)
    Sleep(300)

    def lambda_3282():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3282)
    Sleep(300)

    def lambda_32A2():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32A2)
    Sleep(300)

    def lambda_32C2():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x834, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C2)
    Sleep(300)

    def lambda_32E2():
        OP_8F(0xFE, 0xFFFFD81E, 0xFFFFF63C, 0x34F8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32E2)
    Return()

    # Function_19_31BC end

    def Function_20_32F8(): pass

    label("Function_20_32F8")


    def lambda_32FE():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32FE)
    Sleep(300)

    def lambda_331E():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_331E)
    Sleep(300)

    def lambda_333E():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_333E)
    Sleep(300)

    def lambda_335E():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_335E)
    Sleep(300)

    def lambda_337E():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_337E)
    Sleep(300)

    def lambda_339E():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_339E)
    Sleep(300)

    def lambda_33BE():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33BE)
    Sleep(300)

    def lambda_33DE():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33DE)
    Sleep(300)

    def lambda_33FE():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x834, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33FE)
    Sleep(300)

    def lambda_341E():
        OP_8F(0xFE, 0xFFFFF40C, 0xFFFFF63C, 0x32C8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_341E)
    Return()

    # Function_20_32F8 end

    def Function_21_3434(): pass

    label("Function_21_3434")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B8")
    OP_8C(0xFE, 135, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(200)
    OP_8C(0xFE, 45, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(500)
    OP_8C(0xFE, 45, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(200)
    OP_8C(0xFE, 135, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(500)
    OP_8C(0xFE, 135, 0)
    Sleep(200)
    OP_8C(0xFE, 90, 0)
    Sleep(500)
    Jump("Function_21_3434")

    label("loc_34B8")

    Return()

    # Function_21_3434 end

    def Function_22_34B9(): pass

    label("Function_22_34B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_353D")
    OP_8C(0xFE, 315, 0)
    Sleep(300)
    OP_8C(0xFE, 270, 0)
    Sleep(300)
    OP_8C(0xFE, 225, 0)
    Sleep(200)
    OP_8C(0xFE, 270, 0)
    Sleep(180)
    OP_8C(0xFE, 225, 0)
    Sleep(400)
    OP_8C(0xFE, 270, 0)
    Sleep(250)
    OP_8C(0xFE, 315, 0)
    Sleep(400)
    OP_8C(0xFE, 270, 0)
    Sleep(350)
    OP_8C(0xFE, 315, 0)
    Sleep(250)
    OP_8C(0xFE, 270, 0)
    Sleep(400)
    Jump("Function_22_34B9")

    label("loc_353D")

    Return()

    # Function_22_34B9 end

    def Function_23_353E(): pass

    label("Function_23_353E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_END)), "loc_3549")
    Return()

    label("loc_3549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3555")
    Return()

    label("loc_3555")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -44960, -2000, 41690, 180)
    OP_6D(-44990, -2000, 38500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(312000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    OP_6A(0x101)
    OP_8E(0x101, 0xFFFF5088, 0xFFFFF830, 0x972C, 0x5DC, 0x0)
    Sleep(500)
    OP_6A(0xFF)

    ChrTalk(    #133
        0x101,
        (
            "#1025F呼～……\x01",
            "真是美丽的晚霞呀～\x02\x03",

            "和那时侯一样……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_AD(0x2400C4, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #134
        0x101,
        "#1027F…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_365B():
        OP_67(0, 7200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_365B)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 1)
    SetChrChipByIndex(0x101, 17)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #135
        0x101,
        (
            "#1003F无论是天空还是湖水还是晚霞\x01",
            "都和那时侯一样……\x02\x03",

            "和大家一起\x01",
            "应当很开心才对，但是……\x02\x03",

            "果然……完全不一样。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #136
        0x101,
        (
            "#1007F啊啊，这样可不行……\x02\x03",

            "好不容易找到了答案，\x01",
            "要用自己的步调赶上他的……\x02\x03",

            "这样的话，会被约修亚，\x01",
            "还有母亲笑话的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(500)

    ChrTalk(    #137
        0x101,
        (
            "#1025F……对了。\x02\x03",

            "只有上次在梦里\x01",
            "成功的吹奏过……\x02\x03",

            "再练习一下吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 18)
    OP_0D()
    Sleep(1000)
    OP_21()

    def lambda_3819():

        label("loc_3819")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3819")

    QueueWorkItem2(0x101, 0, lambda_3819)
    OP_1D(0x46)
    OP_1F(0x64, 0xC8)

    def lambda_3834():
        OP_6B(3200, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3834)
    Sleep(5000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T1510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_353E end

    def Function_24_3860(): pass

    label("Function_24_3860")

    EventBegin(0x0)
    SetChrPos(0x101, -44920, -2000, 38700, 180)
    OP_6D(-44990, -2000, 38500, 0)
    OP_67(0, 7200, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(312000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 18)

    def lambda_38BB():

        label("loc_38BB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_38BB")

    QueueWorkItem2(0x101, 0, lambda_38BB)
    FadeToBright(1000, 0)
    OP_0D()
    OP_21()
    OP_44(0x101, 0x0)
    Sleep(1000)
    OP_99(0x101, 0x8, 0x9, 0x5DC)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x101, 10)
    OP_0D()
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x101, 17)
    SetChrSubChip(0x101, 1)

    ChrTalk(    #138
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 15)
    SetChrPos(0xE, -40350, -2000, 48090, 188)
    ClearChrFlags(0xE, 0x80)

    def lambda_3958():
        OP_6D(-43510, -2000, 43790, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3958)

    def lambda_3970():
        OP_6C(331000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3970)
    Sleep(1000)

    def lambda_3985():

        label("loc_3985")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_3985")

    QueueWorkItem2(0x101, 3, lambda_3985)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #139
        0xE,
        (
            "#1061F#6P嘿嘿，我听到了\x01",
            "十分优美的曲调哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1015F#5P凯文先生……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0xF)
    Sleep(500)

    def lambda_3A01():
        OP_6D(-45120, -2000, 39640, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A01)

    def lambda_3A19():
        OP_6C(315000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A19)
    OP_8F(0xE, 0xFFFF5100, 0xFFFFF830, 0xAABE, 0x7D0, 0x0)

    def lambda_3A3D():
        OP_8E(0xE, 0xFFFF5056, 0xFFFFF830, 0x9F06, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A3D)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x3)

    ChrTalk(    #141
        0xE,
        (
            "#1060F不过，我只是来看看\x01",
            "是谁在吹奏……\x02\x03",

            "真没想到\x01",
            "竟然是艾丝蒂尔。\x02\x03",

            "#1061F只知道你喜欢钓鱼和收集鞋子，\x01",
            "没想到你还有这样的兴趣？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1008F#6P嘿嘿……\x01",
            "和我的形象不符吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xE,
        (
            "#1064F不，没那回事。\x02\x03",

            "#1066F说实话，还是钓鱼方面\x01",
            "更擅长一点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1016F#6P哈哈，直接说\x01",
            "吹得很糟糕就可以了。\x02\x03",

            "就连我自己\x01",
            "也不认为吹的好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xE,
        (
            "#1065F嗯，的确\x01",
            "有些笨拙的地方，不过……\x02\x03",

            "#1060F音乐最重要的是用心去演奏。\x02\x03",

            "这点，从刚才的\x01",
            "吹奏中，已经很\x01",
            "好的流露出来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1025F#6P是，是吗……\x02\x03",

            "#1003F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xE,
        "#1060F可以站到你旁边吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1025F#6P啊……\x01",
            "啊，嗯，请。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CA1():
        OP_6D(-44990, -2000, 38510, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CA1)

    def lambda_3CB9():
        OP_8F(0xFE, 0xFFFF4E4E, 0xFFFFF830, 0x966E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CB9)
    Sleep(50)
    OP_8F(0x101, 0xFFFF51C8, 0xFFFFF830, 0x9678, 0x3E8, 0x0)
    OP_8C(0x101, 270, 200)
    WaitChrThread(0xE, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_62(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0xE)
    Sleep(500)

    ChrTalk(    #149
        0xE,
        (
            "#1065F#5P……我想问你一件事。\x02\x03",

            "#1067F艾丝蒂尔，\x01",
            "见到他之后你打算怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1004F#4P啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #151
        0xE,
        (
            "#1060F#5P听说因为一些事\x01",
            "从你们的面前消失了。\x02\x03",

            "如果你再遇到他，你想\x01",
            "对那家伙说些什么呢……\x02\x03",

            "你应该有想过吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1026F#4P…………………………………\x02\x03",

            "#1003F我曾经想过，\x01",
            "就算揍扁他也要带他回来……\x02\x03",

            "但是，这么鲁莽的事\x01",
            "我想我也做不到……\x02\x03",

            "#1007F坦白说，我的话也许\x01",
            "约修亚已经听不进去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xE,
        (
            "#1063F#5P即使知道这些……\x01",
            "你也不会放弃他吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1003F#4P嗯……\x02\x03",

            "#1025F约修亚背负的痛苦…\x01",
            "还有我自己的不成熟，\x01",
            "我考虑了很多……\x02\x03",

            "结果，无论我怎么考虑\x01",
            "都想不出要对约修亚\x01",
            "说些什么才好。\x02\x03",

            "#1010F因此──这些话\x01",
            "还是等遇到他的时候再考虑吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xE,
        "#1064F#5P……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1025F#4P可是，我的思念\x01",
            "不仅仅是我自己的。\x02\x03",

            "那是和约修亚在一起的时候\x01",
            "自然培养起来的感情。\x02\x03",

            "#1012F因此……遇到约修亚后\x01",
            "我一定会知道该说些什么的。\x02\x03",

            "#1017F只有我才能传达\x01",
            "给约修亚的话语──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xE,
        "#1064F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1006F#4P因此，我决定还没见面以前\x01",
            "就不再想这些只会令人烦恼的事了。\x02\x03",

            "#1016F嘿嘿，虽然偶尔\x01",
            "我也会像刚刚那样伤感……\x02\x03",

            "就当作那是少女的特权吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #159
        0xE,
        (
            "#1068F#5P……哈，真没法子。\x02\x03",

            "跟我原来的计划\x01",
            "根本完全不一样嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x101,
        "#1004F#4P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xE,
        (
            "#1065F#5P①沉浸在伤感中的艾丝蒂尔。\x02\x03",

            "#1063F②被我用尖锐言词刺激\x01",
            "  感到不知所措的艾丝蒂尔。\x02\x03",

            "#1062F③这时我温柔的安慰她。\x02\x03",

            "#1061F④艾丝蒂尔重新恢复了精神\x01",
            "  ≡ 于是对我的好感度直线上升。\x02\x03",

            "#1062F──这是我准备好的\x01",
            "必胜计划……\x02\x03",

            "#1068F结果②，③\x01",
            "还没开始就结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1016F#4P啊哈哈，抱歉抱歉。\x02\x03",

            "#1006F不过，凯文先生\x01",
            "真是名很棒的神父啊。\x02\x03",

            "对像我这样的\x01",
            "陷入苦恼的人\x01",
            "总是那么关心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xE,
        (
            "#1068F#5P啊唔……\x02\x03",

            "#1066F嗯，虽然这\x01",
            "就是神父的工作……\x02\x03",

            "但对艾丝蒂尔关心，\x01",
            "还有一半理由的是\x01",
            "出于爱意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#1004F#4P啊……？\x02\x03",

            "你说什么哪──\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xE, 180, 400)

    ChrTalk(    #165
        0xE,
        "#1063F#5P……稍等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#1015F#4P？？？\x02\x03",

            "你突然怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xE,
        (
            "#1067F#5P不，从湖那边\x01",
            "好像来了条小船……\x02\x03",

            "好像上面\x01",
            "躺着个人。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)

    ChrTalk(    #168
        0x101,
        "#1020F#4P啊！？\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    OP_72(0x3, 0x2)
    OP_71(0x3, 0x40)
    OP_A1(0x10, 0x3)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    SetChrFlags(0x12, 0x1)
    SetChrSubChip(0x12, 5)
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, -44030, -3000, 23480, 180)
    OP_48()
    OP_89(0x12, -43660, -3000, 24200, 0)

    def lambda_4504():
        OP_6D(-44650, -2000, 35970, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4504)

    def lambda_451C():
        OP_67(0, 7280, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_451C)

    def lambda_4534():
        OP_6C(229000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4534)
    Sleep(300)
    OP_8C(0x101, 180, 400)
    Sleep(1700)
    OP_43(0x10, 0x0, 0x0, 0x19)
    WaitChrThread(0x101, 0x1)
    Sleep(3000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    ChrTalk(    #169
        0x101,
        "#1020F#2P#3S克，克鲁茨前辈！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1501   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3860 end

    def Function_25_45E0(): pass

    label("Function_25_45E0")

    PlayEffect(0x0, 0x0, 0x10, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_461B():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x8B74, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_461B)
    Sleep(300)

    def lambda_463B():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x8B74, 0x640, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_463B)
    Sleep(300)

    def lambda_465B():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x8B75, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_465B)
    WaitChrThread(0x10, 0x1)
    OP_22(0x12E, 0x0, 0x4B)
    PlayEffect(0x1, 0xFF, 0x10, 0, -170, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    OP_82(0x0, 0x0)

    def lambda_46BD():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_46BD)
    Sleep(200)

    def lambda_46DD():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_46DD)
    Sleep(200)

    def lambda_46FD():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_46FD)

    def lambda_4718():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4718)
    Sleep(200)

    def lambda_4738():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4738)
    Sleep(200)

    def lambda_4758():
        OP_8F(0xFE, 0xFFFF53E4, 0xFFFFF448, 0x84D0, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4758)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_25_45E0 end

    def Function_26_4773(): pass

    label("Function_26_4773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47C9")
    EventBegin(0x1)

    ChrTalk(    #170
        0x101,
        (
            "#1015F哎呀，瞒着大家\x01",
            "出来似乎不太好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_47C9")

    Return()

    # Function_26_4773 end

    def Function_27_47CA(): pass

    label("Function_27_47CA")

    EventBegin(0x1)

    ChrTalk(    #171
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_47F6():
        OP_6D(-3550, -2000, 29080, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_47F6)

    def lambda_480E():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_480E)

    def lambda_481E():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_481E)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #172
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E9")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48AE")
    OP_C0(0xE, 0xC, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)
    Jump("loc_48D0")

    label("loc_48AE")

    OP_C0(0xE, 0xD, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)

    label("loc_48D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48E3")
    OP_A2(0x20E0)
    Call(0, 28)

    label("loc_48E3")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_48F8")

    label("loc_48E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48F8")
    EventEnd(0x1)

    label("loc_48F8")

    Return()

    # Function_27_47CA end

    def Function_28_48F9(): pass

    label("Function_28_48F9")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(-2850, -2000, 32880, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0xF7, 0x8)
    SetChrFlags(0xF8, 0x8)
    SetChrFlags(0xF9, 0x8)
    SetChrPos(0x101, -2950, -2000, 33410, 180)
    SetChrPos(0x16, 1930, -2000, 40500, 225)
    SetChrChipByIndex(0x16, 42)
    OP_4A(0x16, 255)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #173
        0x101,
        "#1020F#1P什，什么啊，这条鱼……！？\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #174
        0x16,
        (
            "#4P噢噢！！\x01",
            "这，这条鱼！？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_4A0E():

        label("loc_4A0E")

        TurnDirection(0xFE, 0x16, 400)
        OP_48()
        Jump("loc_4A0E")

    QueueWorkItem2(0x101, 1, lambda_4A0E)
    OP_6D(-840, -2000, 38510, 1500)

    ChrTalk(    #175
        0x101,
        "#1011F罗伊德大叔……！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_4A60():
        OP_6D(-2330, -2000, 34690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A60)
    OP_8E(0x16, 0xC8, 0xFFFFF830, 0x9772, 0x1388, 0x0)
    OP_8E(0x16, 0xFFFFF466, 0xFFFFF830, 0x9678, 0x1388, 0x0)
    OP_8E(0x16, 0xFFFFF498, 0xFFFFF830, 0x8818, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)

    ChrTalk(    #176
        0x16,
        (
            "#1P红……红褐色的鳞片、\x01",
            "像燃烧一般红色的眼睛……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x16,
        (
            "#1P不，不会错的！\x01",
            "就是那条……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x16,
        "#1P#4S『瓦雷利亚湖的湖之主』呀！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #179
        0x101,
        (
            "#1004F#4P啊！！\x02\x03",

            "这，这是传说的『湖之主』？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x16,
        (
            "#1P嗯，没想到被你\x01",
            "钓上来了呀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x16,
        (
            "#1P身为给你钓鱼手册的人，\x01",
            "现在真是半分高兴半分悔恨的复杂心情呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x16,
        "#1P但，这也是女神的旨意……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x16,
        (
            "#1P这次就坦白地承认你的实力，\x01",
            "请收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #184
        "\x07\x00得到了\x1F\x15\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x415, 1)
    Sleep(500)

    ChrTalk(    #185
        0x16,
        (
            "#1P现在你已经被\x01",
            "我们『钓公师团』公认\x01",
            "成为『特级钓师』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x16,
        (
            "#1P不过！不要满足于现状，\x01",
            "今后更要不断地向钓鱼之路迈进！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1016F#4P啊哈哈……谢谢……\x02\x03",

            "#1015F嗯，不管怎么说\x01",
            "还是谢谢你的礼物……\x02\x03",

            "……请问，这个认证书是什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x16,
        (
            "#1P嗯，这是用来证明\x01",
            "你身为钓师实力的身份证。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x16,
        (
            "#1P拿着去『钓公师团』本部\x01",
            "能得到很多好东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x16,
        (
            "#1P有事去王都的时候\x01",
            "请一定要过去一次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1000F#4P是这样啊。\x01",
            "虽然不是很明白但好像很棒。\x02\x03",

            "嗯，以后一定去看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x16,
        (
            "#1P呵呵，应该有喜欢钓鱼的人\x01",
            "做梦都想要的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x16,
        (
            "#1P哎哟，我也不能认输。\x01",
            "必须赶快制定下个目标。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x16,
        "#1P那么，再见了！\x02",
    )

    CloseMessageWindow()
    OP_8E(0x16, 0xFFFFF466, 0xFFFFF830, 0x9678, 0x1388, 0x0)
    OP_8E(0x16, 0xC8, 0xFFFFF830, 0x9772, 0x1388, 0x0)
    OP_8E(0x16, 0x78A, 0xFFFFF830, 0x9E34, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    SetChrPos(0x16, -8170, 500, 40910, 180)
    SetChrChipByIndex(0x16, 42)
    ClearChrFlags(0x16, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-2950, -2000, 33410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2950, -2000, 33410, 180)
    SetChrPos(0x1, -2950, -2000, 33410, 180)
    SetChrPos(0x2, -2950, -2000, 33410, 180)
    SetChrPos(0x3, -2950, -2000, 33410, 180)
    OP_30(0x0)
    ClearChrFlags(0xF7, 0x8)
    ClearChrFlags(0xF8, 0x8)
    ClearChrFlags(0xF9, 0x8)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_A2(0x8)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_28_48F9 end

    SaveToFile()

Try(main)
