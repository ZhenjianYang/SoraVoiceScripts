from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2120   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2120   ._SN',
            'ED6_DT21/T2120_1 ._SN',
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
        '嘉恩',                                 # 9
        '索姆茨',                               # 10
        '爱珐',                                 # 11
        '欧尼尔',                               # 12
        '奈尔',                                 # 13
        '朵洛希',                               # 14
        '普莱米奥',                             # 15
        '梅尔茨',                               # 16
        '目标用照相机',                         # 17
        '雪拉扎德',                             # 18
        '阿加特',                               # 19
        '提妲',                                 # 20
        '金',                                   # 21
        '森特',                                 # 22
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
        'ED6_DT07/CH02400 ._CH',             # 00
        'ED6_DT07/CH01020 ._CH',             # 01
        'ED6_DT07/CH01210 ._CH',             # 02
        'ED6_DT07/CH01100 ._CH',             # 03
        'ED6_DT07/CH02060 ._CH',             # 04
        'ED6_DT07/CH02070 ._CH',             # 05
        'ED6_DT07/CH01270 ._CH',             # 06
        'ED6_DT07/CH01760 ._CH',             # 07
        'ED6_DT07/CH00023 ._CH',             # 08
        'ED6_DT07/CH00053 ._CH',             # 09
        'ED6_DT07/CH00063 ._CH',             # 0A
        'ED6_DT07/CH00073 ._CH',             # 0B
        'ED6_DT07/CH01660 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH02400P._CP',             # 00
        'ED6_DT07/CH01020P._CP',             # 01
        'ED6_DT07/CH01210P._CP',             # 02
        'ED6_DT07/CH01100P._CP',             # 03
        'ED6_DT07/CH02060P._CP',             # 04
        'ED6_DT07/CH02070P._CP',             # 05
        'ED6_DT07/CH01270P._CP',             # 06
        'ED6_DT07/CH01760P._CP',             # 07
        'ED6_DT07/CH00023P._CP',             # 08
        'ED6_DT07/CH00053P._CP',             # 09
        'ED6_DT07/CH00063P._CP',             # 0A
        'ED6_DT07/CH00073P._CP',             # 0B
        'ED6_DT07/CH01660P._CP',             # 0C
    )

    DeclNpc(
        X                   = -5700,
        Z                   = 0,
        Y                   = 45100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -30000,
        Z                   = 0,
        Y                   = 4910,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 0,
        Y                   = 5000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 29900,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -36400,
        Z                   = 0,
        Y                   = 41430,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -1310,
        Y                   = 0,
        Z                   = 38500,
        Range               = 1450,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9B46,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )


    DeclActor(
        TriggerX            = 1070,
        TriggerZ            = 0,
        TriggerY            = 43260,
        TriggerRange        = 1400,
        ActorX              = 1070,
        ActorZ              = 2000,
        ActorY              = 43260,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30020,
        TriggerZ            = 0,
        TriggerY            = 3590,
        TriggerRange        = 400,
        ActorX              = -30000,
        ActorZ              = 1500,
        ActorY              = 4910,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1020,
        TriggerZ            = 0,
        TriggerY            = 3000,
        TriggerRange        = 400,
        ActorX              = 1200,
        ActorZ              = 1500,
        ActorY              = 5000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29980,
        TriggerZ            = 0,
        TriggerY            = 3310,
        TriggerRange        = 400,
        ActorX              = 29900,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4420,
        TriggerZ            = 0,
        TriggerY            = 45090,
        TriggerRange        = 600,
        ActorX              = -5700,
        ActorZ              = 1500,
        ActorY              = 45100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3A6",          # 00, 0
        "Function_1_54C",          # 01, 1
        "Function_2_57C",          # 02, 2
        "Function_3_581",          # 03, 3
        "Function_4_15F4",         # 04, 4
        "Function_5_15F9",         # 05, 5
        "Function_6_1DBA",         # 06, 6
        "Function_7_1DBF",         # 07, 7
        "Function_8_278A",         # 08, 8
        "Function_9_2ECA",         # 09, 9
        "Function_10_3515",        # 0A, 10
        "Function_11_357B",        # 0B, 11
        "Function_12_38FB",        # 0C, 12
        "Function_13_3AEB",        # 0D, 13
        "Function_14_3CBD",        # 0E, 14
        "Function_15_3FCE",        # 0F, 15
        "Function_16_41A3",        # 10, 16
        "Function_17_43E7",        # 11, 17
        "Function_18_6785",        # 12, 18
        "Function_19_75FC",        # 13, 19
        "Function_20_7618",        # 14, 20
        "Function_21_7639",        # 15, 21
        "Function_22_7679",        # 16, 22
        "Function_23_76D9",        # 17, 23
        "Function_24_959C",        # 18, 24
        "Function_25_A9AD",        # 19, 25
        "Function_26_C1DD",        # 1A, 26
        "Function_27_C1F9",        # 1B, 27
        "Function_28_C215",        # 1C, 28
        "Function_29_C231",        # 1D, 29
        "Function_30_C261",        # 1E, 30
        "Function_31_CAF3",        # 1F, 31
        "Function_32_CB19",        # 20, 32
        "Function_33_CB3F",        # 21, 33
        "Function_34_CB65",        # 22, 34
        "Function_35_CBB3",        # 23, 35
        "Function_36_CC4C",        # 24, 36
    )


    def Function_0_3A6(): pass

    label("Function_0_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3B0")
    Jump("loc_3CA")

    label("loc_3B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3CA")
    ClearChrFlags(0xF, 0x80)

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EC")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -2790, 0, 41750, 0)

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42E")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 8)
    SetChrPos(0x11, -33790, 250, 46120, 180)

    label("loc_42E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_45B")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 9)
    SetChrPos(0x12, -31990, 250, 46120, 180)

    label("loc_45B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_488")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 10)
    SetChrPos(0x13, -33850, 250, 43760, 0)

    label("loc_488")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B5")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 11)
    SetChrPos(0x14, -31980, 250, 43650, 0)

    label("loc_4B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_4CB")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_54B")

    label("loc_4CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_4E1")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_54B")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_4F7")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 1)
    Jump("loc_54B")

    label("loc_4F7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_503"),
        (SWITCH_DEFAULT, "loc_54B"),
    )


    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_51B")
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_548")

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_537")
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_548")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_548")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_548")

    Jump("loc_54B")

    label("loc_54B")

    Return()

    # Function_0_3A6 end

    def Function_1_54C(): pass

    label("Function_1_54C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_565")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)

    label("loc_57B")

    Return()

    # Function_1_54C end

    def Function_2_57C(): pass

    label("Function_2_57C")

    Call(0, 3)
    Return()

    # Function_2_57C end

    def Function_3_581(): pass

    label("Function_3_581")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D6")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C2")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5B7")
    OP_A9(0x77)
    Jump("loc_5B9")

    label("loc_5B7")

    OP_A9(0x64)

    label("loc_5B9")

    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_5C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D3")
    TalkEnd(0x9)
    Return()

    label("loc_5D3")

    Jump("loc_FFC")

    label("loc_5D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFC")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -29500, 0, 2800, 0)
    SetChrPos(0x102, -30300, 0, 2600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_63D")
    SetChrPos(0xF9, -29900, 0, 1600, 0)
    SetChrPos(0xF8, -30800, 0, 1400, 0)
    Jump("loc_65F")

    label("loc_63D")

    SetChrPos(0xF8, -29900, 0, 1600, 0)
    SetChrPos(0xF9, -30800, 0, 1400, 0)

    label("loc_65F")

    OP_8C(0x9, 180, 0)
    OP_6D(-30100, 0, 3960, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #0
        0x9,
        "不好意思工房现在停业了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "因为导力驱动的工具\x01",
            "全都不能动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "明明看起来都是好的……\x01",
            "到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_750")

    ChrTalk(    #3
        0x101,
        (
            "#1018F#4P啊，那个不用担心。\x02\x03",

            "我们带了好东西来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "噢，是什么？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA2")

    label("loc_750")


    ChrTalk(    #5
        0x101,
        (
            "#1026F#4P啊，是吗……\x02\x03",

            "#1015F嗯……不过真伤脑筋啊。\x02\x03",

            "结晶回路的合成和结晶孔的强化\x01",
            "都完全不能进行……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FF")

    ChrTalk(    #6
        0x103,
        (
            "#025F嗯嗯，难得有了这的发生器，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89A")

    label("loc_7FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_842")

    ChrTalk(    #7
        0x108,
        (
            "#072F唔，难得有了这的发生器，\x01",
            "真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89A")

    label("loc_842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89A")

    ChrTalk(    #8
        0x106,
        (
            "#552F啊啊，难得有了这的发生器，\x01",
            "恢复导力魔法了呢。\x02\x03",

            "这真是太可惜了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EF")

    ChrTalk(    #9
        0x107,
        (
            "#064F啊，不过姐姐……\x02\x03",

            "如果只是一小会儿，\x01",
            "那我或许有点办法喔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93D")

    label("loc_8EF")


    ChrTalk(    #10
        0x102,
        (
            "#1043F#1P确实如此……\x02\x03",

            "#1040F不过，如果只是一小会儿\x01",
            "那我或许有点办法喔。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93D")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BA")

    def lambda_96D():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_96D)
    Sleep(120)

    def lambda_980():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_980)

    def lambda_98E():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_98E)
    Sleep(120)

    def lambda_9A1():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_9A1)

    def lambda_9AF():
        TurnDirection(0x9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9AF)
    Jump("loc_9C1")

    label("loc_9BA")

    TurnDirection(0x101, 0x102, 400)

    label("loc_9C1")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #11
        0x101,
        "#1004F#4P啊……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A1E")

    ChrTalk(    #12
        0x106,
        "#052F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4C")

    ChrTalk(    #13
        0x103,
        "#023F能让工房运作起来？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A79")

    label("loc_A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A79")

    ChrTalk(    #14
        0x108,
        "#073F能让工房运作起来吗？\x02",
    )

    CloseMessageWindow()

    label("loc_A79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABB")

    ChrTalk(    #15
        0x107,
        (
            "#060F是，是，大概……\x02\x03",

            "用那个发生器的话……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B03")

    label("loc_ABB")


    ChrTalk(    #16
        0x102,
        (
            "#1040F#1P是，我想……\x02\x03",

            "如果使用那个发生器，\x01",
            "应该能在短时间内复原。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B03")


    ChrTalk(    #17
        0x101,
        "#1018F#4P啊，原来如此！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        "喂喂，你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        "那到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    def lambda_B52():
        TurnDirection(0x0, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B52)
    Sleep(120)

    def lambda_B65():
        TurnDirection(0x1, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B65)

    def lambda_B73():
        TurnDirection(0x2, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B73)
    Sleep(120)

    def lambda_B86():
        TurnDirection(0x3, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B86)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_BA2")


    ChrTalk(    #20
        0x102,
        "#1040F#1P那个，是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x05说明了使用『零力场发生器』\x01",
            "可暂时恢复工房机能的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #22
        0x9,
        "咦，真厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "工具的话这里有，\x01",
            "试试看吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1006F#4P嗯，这就照办。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA0")

    ChrTalk(    #25
        0x107,
        (
            "#560F那么～\x01",
            "请稍等。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CD0")

    label("loc_CA0")


    ChrTalk(    #26
        0x102,
        (
            "#1040F#1P那么，稍等片刻。\x01",
            "借用一下机械了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x9, 315, 0)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05使用『零力场发生器』将工房机能恢复了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #28
        0x9,
        (
            "喔喔，看起来很不错呢。\x01",
            "导力能源又回到机械里了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DB3")
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #29
        0x9,
        (
            "虽然只是做了应急维修，\x01",
            "要调整就趁现在了!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED5")

    label("loc_DB3")


    ChrTalk(    #30
        0x101,
        "#1000F#4P太好了……看来是成功了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E32")

    ChrTalk(    #31
        0x107,
        (
            "#063F嗯，不过这\x01",
            "只是暂时能动……\x02\x03",

            "#561F马上又会回到不动的状态的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E80")

    label("loc_E32")


    ChrTalk(    #32
        0x102,
        (
            "#1040F#1P嗯，确实很顺利……\x02\x03",

            "但并不是真的修好了。\x01",
            "过一段时间又会停止的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E80")

    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #33
        0x9,
        (
            "是吗……\x01",
            "仅仅是应急维修而已吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "呼，不管怎么说，\x01",
            "要调整就趁现在了!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    label("loc_ED5")

    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x77)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #35
        0x9,
        (
            "话虽如此……\x01",
            "真是个厉害的装置啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "可以的话，\x01",
            "能留下一个吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1015F#4P嗯～可以的话\x01",
            "是想这么做……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1040F#1P但是不好意思。\x01",
            "重要的任务还要使用它呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "呼，果然不行吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "嗯，来这里的时候\x01",
            "就带着那个好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "那样就可以像刚才一样\x01",
            "使用工房了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E3)
    EventEnd(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_109C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1050")

    ChrTalk(    #42
        0x9,
        (
            "唔～游击士\x01",
            "照相的技术也不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        "有什么特别的训练吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1099")

    label("loc_1050")


    ChrTalk(    #44
        0x9,
        "去哪里摄影了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "因为兴趣而开始使用相机的人\x01",
            "最近增加了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1099")

    Jump("loc_15F0")

    label("loc_109C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114D")

    ChrTalk(    #46
        0x9,
        (
            "城里的导力器\x01",
            "还是不能动啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "只要大桥动不了，\x01",
            "这状态就会持续啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "但是，使用导力的机械\x01",
            "居然全部不能动了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "真是的，利贝尔\x01",
            "以后会怎样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1191")

    label("loc_114D")


    ChrTalk(    #50
        0x9,
        (
            "城里的导力器\x01",
            "还是不能动啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "真是的，利贝尔\x01",
            "以后会怎样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1191")

    Jump("loc_15F0")

    label("loc_1194")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1209")

    ChrTalk(    #52
        0x9,
        (
            "只要有那个装置\x01",
            "就能再开始营业啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "也好，\x01",
            "不能强人所难嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "只好老老实实等待\x01",
            "这灾难过去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F0")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12A3")

    ChrTalk(    #55
        0x9,
        (
            "诺曼先生说得对，\x01",
            "旅游业确实有前途。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "但是，卢安这里和王都\x01",
            "都是连接海路的要地嘛。\x01",
            "港口设施也不能疏忽哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "呼，该给谁投票呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1325")

    label("loc_12A3")

    OP_A2(0x1)

    ChrTalk(    #58
        0x9,
        (
            "诺曼先生说得对，\x01",
            "旅游业确实有前途。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "但是，卢安这里和王都\x01",
            "都是连接海路的要地嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "整备港口设施\x01",
            "感觉还是很重要呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1325")

    Jump("loc_15F0")

    label("loc_1328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_138D")

    ChrTalk(    #61
        0x9,
        (
            "因为戴尔蒙市长的事\x01",
            "使得城市的形象变坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "要是再引起骚动\x01",
            "真的是受不了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_141F")

    label("loc_138D")

    OP_A2(0x1)

    ChrTalk(    #63
        0x9,
        (
            "真是头痛啊。\x01",
            "竟然发生那样的骚动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "本来就因为戴尔蒙市长的事\x01",
            "使得城市的形象变坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "如果再发生什么，\x01",
            "在别人心中坏印象就改变不了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_141F")

    Jump("loc_15F0")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_144D")

    ChrTalk(    #66
        0x9,
        (
            "哟，怎么了？\x01",
            "感觉很着急啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F0")

    label("loc_144D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_151A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14C6")

    ChrTalk(    #67
        0x9,
        (
            "最近有很多旅游的客人\x01",
            "拜托我冲洗感光结晶回路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "因为导力照相机普及，\x01",
            "拍摄照片的人也增多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1517")

    label("loc_14C6")

    OP_A2(0x1)

    ChrTalk(    #69
        0x9,
        (
            "该支持哪位候选人，\x01",
            "其实还没决定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "我们和游客、港口之间\x01",
            "都有交易。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1517")

    Jump("loc_15F0")

    label("loc_151A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_15F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_158F")

    ChrTalk(    #71
        0x9,
        (
            "新型导力器的普及活动\x01",
            "由爱普斯泰恩财团在推进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "像我们这样个人经营的工房，\x01",
            "也要配合这活动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F0")

    label("loc_158F")

    OP_A2(0x1)

    ChrTalk(    #73
        0x9,
        (
            "哟，新型导力器\x01",
            "使用感觉怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "为了更好掌握其性能，结晶孔\x01",
            "还是积极地强化了比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F0")

    TalkEnd(0x9)
    Return()

    # Function_3_581 end

    def Function_4_15F4(): pass

    label("Function_4_15F4")

    Call(0, 5)
    Return()

    # Function_4_15F4 end

    def Function_5_15F9(): pass

    label("Function_5_15F9")

    TalkBegin(0xA)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162A")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_161F")
    OP_A9(0x76)
    Jump("loc_1621")

    label("loc_161F")

    OP_A9(0x65)

    label("loc_1621")

    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_162A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_163B")
    TalkEnd(0xA)
    Return()

    label("loc_163B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_18A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1797")

    ChrTalk(    #75
        0xA,
        "哎呀，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "我听说了哦，学院的事件\x01",
            "好像平安解决了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1006F嗯，总算是吧。\x02\x03",

            "因为有卡露娜前辈他们\x01",
            "的帮助啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #78
        0xA,
        (
            "呵呵，我的收藏\x01",
            "好像也稍微派上点用场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1011F收藏……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        (
            "#1040F对了，卡露娜是\x01",
            "使用枪的啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x102, 400)

    ChrTalk(    #81
        0xA,
        (
            "嗯嗯，火药式枪械\x01",
            "的使用是非常难的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "不过，卡露娜\x01",
            "是没问题的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20B3)
    Jump("loc_18A1")

    label("loc_1797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_17EF")

    ChrTalk(    #83
        0xA,
        (
            "我妹妹妮吉塔\x01",
            "也在王立学院上学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        (
            "事件平安解决了，\x01",
            "我也衷心表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A1")

    label("loc_17EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1870")

    ChrTalk(    #85
        0xA,
        (
            "王立学院的事件\x01",
            "好像平安解决了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "我妹妹妮吉塔\x01",
            "也在那学院上学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "事件平安解决了，\x01",
            "我也衷心表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_18A1")

    label("loc_1870")


    ChrTalk(    #88
        0xA,
        (
            "事件解决真是谢谢你们了。\x01",
            "让我衷心表示感谢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A1")

    Jump("loc_1DB6")

    label("loc_18A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1944")

    ChrTalk(    #89
        0xA,
        (
            "使用导力的武器\x01",
            "好像都不起作用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "不过普通的武器还能使用，\x01",
            "如果有武术知识就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "呵呵，一到关键时刻\x01",
            "还是要看基本功哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_19A6")

    label("loc_1944")


    ChrTalk(    #92
        0xA,
        (
            "使用导力的武器\x01",
            "好像都不起作用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "不过普通的武器还能使用，\x01",
            "如果有武术知识就没问题了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A6")

    Jump("loc_1DB6")

    label("loc_19A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A0C")

    ChrTalk(    #94
        0xA,
        (
            "投票是肯定要投的，\x01",
            "不过我个人不太关心选举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "嗯，就看人品\x01",
            "决定投哪边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A75")

    label("loc_1A0C")

    OP_A2(0x0)

    ChrTalk(    #96
        0xA,
        (
            "投票是肯定要投的，\x01",
            "不过说实话我不太关心选举。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "倒是对自身工作有影响的人\x01",
            "十分热心地参与其中。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A75")

    Jump("loc_1DB6")

    label("loc_1A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1AE6")

    ChrTalk(    #98
        0xA,
        (
            "因为卢安是船员的城市，\x01",
            "所以性情刚烈的人就很多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "没有一定的骨气\x01",
            "是无法忍受长期海上生活的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB6")

    label("loc_1AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1B29")

    ChrTalk(    #100
        0xA,
        (
            "刚才的客人\x01",
            "从店里冲出去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        "发生什么事了呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DB6")

    label("loc_1B29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B8E")

    ChrTalk(    #102
        0xA,
        (
            "游击士的工作\x01",
            "要到处跑来跑去真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "至少待在卢安期间\x01",
            "请好好休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5C")

    label("loc_1B8E")

    OP_A2(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1C90")

    ChrTalk(    #104
        0xA,
        "欢迎，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "你们的工作\x01",
            "要到处跑来跑去真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "没有固定的休息时间，\x01",
            "相见的机会也少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "男人成家的时间\x01",
            "也有变晚的倾向哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #108
        0x101,
        "#1028F啊～原来如此啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #109
        0x106,
        (
            "#552F……………………………\x02\x03",

            "喂，为什么看我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D5C")

    label("loc_1C90")


    ChrTalk(    #110
        0xA,
        "欢迎，游击士们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "你们的工作\x01",
            "要到处跑来跑去真辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        (
            "没有固定的休息时间，\x01",
            "相见的机会也少……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "最后嫁不出去的\x01",
            "女性好像也不少呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        "#023F（……………………）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        "呵呵，开个小玩笑啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1D5C")

    Jump("loc_1DB6")

    label("loc_1D5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1DB6")

    ChrTalk(    #116
        0xA,
        (
            "哎呀，欢迎。\x01",
            "游击士们都到齐了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "现在卡露娜也不在，\x01",
            "就全拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB6")

    TalkEnd(0xA)
    Return()

    # Function_5_15F9 end

    def Function_6_1DBA(): pass

    label("Function_6_1DBA")

    Call(0, 7)
    Return()

    # Function_6_1DBA end

    def Function_7_1DBF(): pass

    label("Function_7_1DBF")

    TalkBegin(0xB)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF0")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE5")
    OP_A9(0x6D)
    Jump("loc_1DE7")

    label("loc_1DE5")

    OP_A9(0x66)

    label("loc_1DE7")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_1DF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E01")
    TalkEnd(0xB)
    Return()

    label("loc_1E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1F3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED3")

    ChrTalk(    #118
        0xB,
        (
            "灯油和食品\x01",
            "还有一些库存……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xB,
        (
            "如果这样的状态长久持续下去，\x01",
            "恐怕很快也会见底吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xB,
        (
            "中央工房制的新型眼镜\x01",
            "也陆续上市了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        (
            "特别是在灯灭了的地方使用，\x01",
            "非常方便。\x01",
            "来买几个好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1F38")

    label("loc_1ED3")


    ChrTalk(    #122
        0xB,
        (
            "中央工房制的新型眼镜\x01",
            "也陆续上市了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xB,
        (
            "特别是在灯灭了的地方使用，\x01",
            "非常方便。\x01",
            "来买几个好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F38")

    Jump("loc_2786")

    label("loc_1F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_209C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2028")

    ChrTalk(    #124
        0xB,
        (
            "唔，导力器停止\x01",
            "真是不得了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xB,
        (
            "这样的现象就连我\x01",
            "也从来没见过啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        (
            "对了，\x01",
            "说到前所未见……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        (
            "中央工房出产的\x01",
            "新型眼镜上市了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xB,
        (
            "特别是在灯灭了的地方使用，\x01",
            "非常方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        (
            "如果没有，\x01",
            "来买几个好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2099")

    label("loc_2028")


    ChrTalk(    #130
        0xB,
        (
            "中央工房出产的\x01",
            "新型眼镜上市了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "特别是在灯灭了的地方使用，\x01",
            "非常方便。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xB,
        (
            "如果没有，\x01",
            "来买几个好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2099")

    Jump("loc_2786")

    label("loc_209C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_21BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_211B")

    ChrTalk(    #133
        0xB,
        (
            "仅靠港口收入支撑城市的开销\x01",
            "是完全不行的，这是不争的事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        (
            "重视旅游也可以理解，\x01",
            "不过感觉真有点寂寞。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_211B")

    OP_A2(0x4)

    ChrTalk(    #135
        0xB,
        (
            "身为前船员还是希望\x01",
            "能想办法维持港口啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        (
            "仅靠港口收入支撑城市的开销\x01",
            "是完全不行的，这是不争的事实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        (
            "重视旅游也可以理解，\x01",
            "不过感觉真有点寂寞。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21BB")

    Jump("loc_2786")

    label("loc_21BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2399")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_21F4")

    ChrTalk(    #138
        0xB,
        (
            "怎么，想听更多\x01",
            "我的冒险故事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2396")

    label("loc_21F4")

    OP_A2(0x4)

    ChrTalk(    #139
        0xB,
        (
            "好像发生了什么骚乱,\x01",
            "呼…没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xB,
        (
            "我年轻的时候参加过的\x01",
            "某民族的选举，\x01",
            "要过激得多了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        (
            "那些家伙的选举很单纯。\x01",
            "大家打群架，最后\x01",
            "谁站着谁就是新的代表。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xB,
        (
            "当然我也被卷进去了。\x01",
            "但是话虽如此，我也是\x01",
            "身经百战的船长·欧尼尔啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        (
            "缓过神来的时候\x01",
            "才发现只有我一个人站着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        (
            "哎呀，差点被\x01",
            "他们选作新酋长，\x01",
            "拼尽全力才逃到船上跑回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xB,
        (
            "如果就那样当了酋长,\x01",
            "应该也会过得很开心吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        "哇哈哈！\x02",
    )

    CloseMessageWindow()

    label("loc_2396")

    Jump("loc_2786")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_23E3")

    ChrTalk(    #147
        0xB,
        (
            "唔～好像\x01",
            "桥那边很吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xB,
        (
            "又～是年轻人\x01",
            "在胡闹了吗～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2786")

    label("loc_23E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_246B")

    ChrTalk(    #149
        0xB,
        (
            "要说没有选举的国家\x01",
            "就是埃雷波尼亚帝国吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xB,
        (
            "以地方民主制度和王室\x01",
            "分担职能的利贝尔\x01",
            "可以说具有贤明的制度啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25B9")

    label("loc_246B")

    OP_A2(0x4)

    ChrTalk(    #151
        0xB,
        (
            "没有选举的代表国家\x01",
            "那就是埃雷波尼亚帝国吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xB,
        (
            "虽然在边境的自治区还有选举，\x01",
            "但帝国中枢是严格的等级社会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        (
            "不过这样的制度\x01",
            "运转顺利的时候还是挺好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xB,
        (
            "如果身份高贵的人中优秀的人很多，\x01",
            "这个制度就会好得令人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xB,
        (
            "当然反之\x01",
            "就会惨不忍睹了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xB,
        (
            "嗯，这样看来将王权和选举\x01",
            "完美分开使用的利贝尔\x01",
            "可以说具有贤明的制度啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B9")

    Jump("loc_2786")

    label("loc_25BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_263F")

    ChrTalk(    #157
        0xB,
        (
            "选举的做法也根据国家各自\x01",
            "价值观的不同而大相径庭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        (
            "和我们相反选出『讨厌的人』\x01",
            "然后赶出去的国家也存在哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2786")

    label("loc_263F")

    OP_A2(0x4)

    ChrTalk(    #159
        0xB,
        (
            "城市由于选举而热闹起来，\x01",
            "虽说是选举，但各国制度各不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        (
            "譬如利贝尔的市长选举制度\x01",
            "是以共和国为范本的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xB,
        (
            "那个国家民族众多，\x01",
            "因此需要公平的方法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xB,
        (
            "话说回来世界上和我们制度相反，\x01",
            "选『讨厌的人』的国家也存在哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xB,
        (
            "在那里得票最多的不受欢迎者\x01",
            "会从会议上被赶走。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xB,
        (
            "这个制度\x01",
            "说不定很有道理哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xB,
        "哇哈哈！\x02",
    )

    CloseMessageWindow()

    label("loc_2786")

    TalkEnd(0xB)
    Return()

    # Function_7_1DBF end

    def Function_8_278A(): pass

    label("Function_8_278A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C09")

    ChrTalk(    #166
        0x8,
        (
            "#650F呀，辛苦了。\x01",
            "学院刚刚发生的事真是不得了呢。\x02\x03",

            "不过，不愧是你们啊，\x01",
            "顺利解决了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1001F嘿嘿，没什么。\x02\x03",

            "这也多亏嘉恩哥哥\x01",
            "联络及时啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x102,
        (
            "#1040F嗯嗯，也多亏卡露娜他们\x01",
            "的突袭了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x8,
        (
            "#650F哈哈，这是我的工作嘛。\x02\x03",

            "不管怎样，没有出大事\x01",
            "就算放心了。\x02\x03",

            "#655F但是这个导力停止现象\x01",
            "还没有完全解决，\x01",
            "所以还不能完全放下心来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2942")

    ChrTalk(    #170
        0x108,
        (
            "#072F而且，结社的人\x01",
            "也不知道还会做出什么事。\x02\x03",

            "此后行事\x01",
            "也不能松懈吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_2942")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_299E")

    ChrTalk(    #171
        0x103,
        (
            "#022F而且，结社的人\x01",
            "也不知道还会做出什么事。\x02\x03",

            "此后也要\x01",
            "谨慎行事为妙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FD")

    label("loc_299E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FD")

    ChrTalk(    #172
        0x106,
        (
            "#050F而且，结社的人\x01",
            "也不知道还会做出什么事。\x02\x03",

            "嗯，此后也要\x01",
            "谨慎行事才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FD")


    ChrTalk(    #173
        0x101,
        "#1002F确实如此……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_2A25")
    OP_A2(0x8)
    Jump("loc_2A28")

    label("loc_2A25")

    OP_A3(0x8)

    label("loc_2A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE2")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇地方任务未报告（QF_REPORT不成立）】\x01",        # 0
            "【◇在其他支部报告完毕（QF_REPORT成立）】\x01",      # 1
            "【◇不变更】\x01",                                   # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2AD6"),
        (1, "loc_2ADC"),
        (SWITCH_DEFAULT, "loc_2AE2"),
    )


    label("loc_2AD6")

    OP_A3(0x8)
    Jump("loc_2AE2")

    label("loc_2ADC")

    OP_A2(0x8)
    Jump("loc_2AE2")

    label("loc_2AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA6")

    ChrTalk(    #174
        0x8,
        (
            "#652F嗯，此后也要小心。\x02\x03",

            "#650F啊，对了对了……\x02\x03",

            "学院事件的事，\x01",
            "核定已经完毕了。\x02\x03",

            "想领取报酬的时候\x01",
            "要重新报告一下哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1000F啊，嗯。\x01",
            "谢谢嘉恩哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        "#1040F那么，先告辞了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C02")

    label("loc_2BA6")


    ChrTalk(    #177
        0x8,
        "#652F嗯，此后也要小心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1000F啊，嗯。\x01",
            "谢谢嘉恩哥哥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x102,
        "#1040F那么，先告辞了。\x02",
    )

    CloseMessageWindow()

    label("loc_2C02")

    OP_A2(0x20B5)
    TalkEnd(0x8)
    Return()

    label("loc_2C09")

    Jump("loc_2C75")

    label("loc_2C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C75")

    ChrTalk(    #180
        0x8,
        (
            "#650F啊，对了……\x02\x03",

            "想找其他支部的\x01",
            "伙伴时就跟我说。\x02\x03",

            "我会跟他们联络\x01",
            "让他们过来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20B4)

    label("loc_2C75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CD9")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "报告\x01",          # 1
            "呼叫同伴\x01",      # 2
            "离开\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_2CDD")

    label("loc_2CD9")

    Call(6, 5)

    label("loc_2CDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DFE")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D57")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x67)

    ChrTalk(    #181
        0x8,
        (
            "#650F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF5")

    label("loc_2D57")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x67)"), scpexpr(EXPR_END)), "loc_2DAC")

    ChrTalk(    #182
        0x8,
        (
            "#650F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF5")

    label("loc_2DAC")


    ChrTalk(    #183
        0x8,
        (
            "#650F现在好像\x01",
            "没有可以报告的工作。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF5")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_2DFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EAD")

    ChrTalk(    #184
        0x8,
        (
            "#650F要找同伴过来吗？\x02\x03",

            "明白了，那么\x01",
            "我马上联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #185
        (
            "\x07\x05联络各支部，\x01",
            "集合了待命人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_2EAD")

    TalkEnd(0x8)
    Return()

    label("loc_2EB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EC5")
    TalkEnd(0x8)
    Return()

    label("loc_2EC5")

    Call(0, 9)
    Return()

    # Function_8_278A end

    def Function_9_2ECA(): pass

    label("Function_9_2ECA")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2F33")

    ChrTalk(    #186
        0x8,
        (
            "#650F学院刚刚发生的事真是不得了呢。\x02\x03",

            "此后结社的人\x01",
            "可能还会谋划什么事件。\x02\x03",

            "请多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3511")

    label("loc_2F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3119")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_END)), "loc_3044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FD8")

    ChrTalk(    #187
        0x8,
        (
            "#650F王都支部来了联络，\x01",
            "但似乎不是马上要你们去。\x02\x03",

            "要是以后路过王都附近的话，\x01",
            "顺便过去一趟就可以了。\x02\x03",

            "嗯，到时候\x01",
            "去艾南那里\x01",
            "一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3041")

    label("loc_2FD8")


    ChrTalk(    #188
        0x8,
        (
            "#650F王都支部来了联络，\x01",
            "但似乎不是马上要你们去。\x02\x03",

            "要是以后路过王都附近的话，\x01",
            "顺便过去一趟就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3041")

    Jump("loc_3116")

    label("loc_3044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C7")

    ChrTalk(    #189
        0x8,
        (
            "#650F对了，检查一下\x01",
            "公告板上的工作好吗？\x02\x03",

            "还有，如果能去确认一下\x01",
            "近郊居民的情况就再好不过了。\x02\x03",

            "那么，就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_3116")

    label("loc_30C7")


    ChrTalk(    #190
        0x8,
        (
            "#650F就麻烦你们检查一下\x01",
            "公告板还有去近郊巡视吧。\x02\x03",

            "现在要做的\x01",
            "也就这些了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3116")

    Jump("loc_3511")

    label("loc_3119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_321B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3191")

    ChrTalk(    #191
        0x8,
        (
            "#650F到了蔡斯\x01",
            "先拜访一下拉赛尔博士吧。\x02\x03",

            "有关新『福音』的事\x01",
            "最好借助博士的智慧。\x02\x03",

            "那么，多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3218")

    label("loc_3191")

    OP_A2(0x2)

    ChrTalk(    #192
        0x8,
        (
            "#650F到了蔡斯\x01",
            "先拜访一下拉赛尔博士吧。\x02\x03",

            "有关新『福音』的事\x01",
            "最好借助博士的智慧。\x02\x03",

            "这边就由梅尔茨\x01",
            "暂时撑着吧。\x02\x03",

            "那么，多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3218")

    Jump("loc_3511")

    label("loc_321B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_32A9")

    ChrTalk(    #193
        0x8,
        (
            "#650F要去王立学院就从城北门出去，\x01",
            "梅威海道向东拐后一直走就到了。\x02\x03",

            "记得学院祭的时候\x01",
            "去帮过忙吧？\x02\x03",

            "那么，调查\x01",
            "就麻烦你们处理了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3511")

    label("loc_32A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_3304")

    ChrTalk(    #194
        0x8,
        (
            "#652F不好意思，\x01",
            "桥上的骚动就拜托了。\x02\x03",

            "支持者之间要是打起来，\x01",
            "可就不得了了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3511")

    label("loc_3304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_341D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3364")

    ChrTalk(    #195
        0x8,
        (
            "#650F３处情报都确认后\x01",
            "就到这里来报告吧。\x02\x03",

            "然后再研究\x01",
            "收集的情报看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_341A")

    label("loc_3364")

    OP_A2(0x2)

    ChrTalk(    #196
        0x8,
        (
            "#650F呀，辛苦了。\x02\x03",

            "目击情报的\x01",
            "确认结束了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#1000F没，正在进行呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#650F３处情报都确认后\x01",
            "就到这里来报告吧。\x02\x03",

            "然后再研究\x01",
            "收集的情报看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        "#1006FＯＫ，明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_341A")

    Jump("loc_3511")

    label("loc_341D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_3511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3495")

    ChrTalk(    #200
        0x8,
        (
            "#650F首先去确认３处目击情报，\x01",
            "然后总结起来再过来报告吧。\x02\x03",

            "不是很紧急的工作，\x01",
            "稍微推迟点也没关系。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3511")

    label("loc_3495")

    OP_A2(0x2)

    ChrTalk(    #201
        0x8,
        (
            "#650F首先去确认３处目击情报，\x01",
            "然后总结起来再过来报告吧。\x02\x03",

            "不是很紧急的工作，\x01",
            "稍微推迟点也没关系。\x02\x03",

            "那么，就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3511")

    TalkEnd(0x8)
    Return()

    # Function_9_2ECA end

    def Function_10_3515(): pass

    label("Function_10_3515")

    TalkBegin(0xE)

    ChrTalk(    #202
        0xE,
        (
            "诺曼的支持者和\x01",
            "波尔多斯的支持者\x01",
            "在大桥争吵呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xE,
        (
            "这样下去会打起来的。\x01",
            "快想办法调停吧！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_10_3515 end

    def Function_11_357B(): pass

    label("Function_11_357B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_37AF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x4000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3613")

    ChrTalk(    #204
        0xFE,
        (
            "之前因为工作去了仓库区，\x01",
            "结果被问了好多奇怪的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "准游击士必要的资格啦，\x01",
            "招募的方法啦等等的问了好多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_3613")

    OP_A2(0x3)

    ChrTalk(    #206
        0xFE,
        (
            "之前因为工作去了仓库区，\x01",
            "碰到个问个不停的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "准游击士必要的资格啦，\x01",
            "招募的方法啦等等的问了好多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "说实话，这些事\x01",
            "去问嘉恩不就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A9")

    Jump("loc_37AC")

    label("loc_36AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_371C")

    ChrTalk(    #209
        0xFE,
        (
            "之前都是靠体力和毅力\x01",
            "撑过来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "看来游击士还是\x01",
            "需要才智和教养的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "真是吸取教训了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_37AC")

    label("loc_371C")

    OP_A2(0x3)

    ChrTalk(    #212
        0xFE,
        (
            "之前代替卡露娜小姐\x01",
            "当过主日学校的讲师……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "真是完全不行啊！\x01",
            "必须从协会规章开始从头学起！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "连修女也看不下去了，\x01",
            "实在是太丢人了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37AC")

    Jump("loc_38F7")

    label("loc_37AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_38F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_37FE")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #215
        0xFE,
        (
            "艾丝蒂尔！\x01",
            "恭喜你晋升！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        "我也要努力不输给你！\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F7")

    label("loc_37FE")

    OP_A2(0x3)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #217
        0xFE,
        "啊，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "好久不见了！\x01",
            "我是支部所属的梅尔茨准游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "恭喜你晋升！\x01",
            "我也会加油的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "卡露娜前辈也不在，\x01",
            "说实话真是很辛苦很辛苦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_38CF")
    TurnDirection(0xFE, 0x106, 0)

    ChrTalk(    #221
        0xFE,
        (
            "阿加特前辈\x01",
            "也请多多关照！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F7")

    label("loc_38CF")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #222
        0xFE,
        (
            "雪拉扎德前辈\x01",
            "也请多多关照！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38F7")

    TalkEnd(0xFE)
    Return()

    # Function_11_357B end

    def Function_12_38FB(): pass

    label("Function_12_38FB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_398B")
    Jump("loc_39CD")

    label("loc_398B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_39A7")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39CD")

    label("loc_39A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39C3")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_39CD")

    label("loc_39C3")

    OP_51(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_39CD")

    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)

    ChrTalk(    #223
        0x11,
        "#020F哎呀，有什么事？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A66"),
        (SWITCH_DEFAULT, "loc_3A93"),
    )


    label("loc_3A66")


    ChrTalk(    #224
        0x11,
        (
            "#020F嗯～是吗～？\x01",
            "要更换成员吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 16)
    Jump("loc_3AE2")

    label("loc_3A93")


    ChrTalk(    #225
        0x11,
        (
            "#026F难得来卢安\x01",
            "待在这里也没意思呢。\x02\x03",

            "#027F偷偷去娱乐场\x01",
            "看看如何呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE2")

    label("loc_3AE2")

    SetChrSubChip(0x11, 0)
    TalkEnd(0x11)
    Return()

    # Function_12_38FB end

    def Function_13_3AEB(): pass

    label("Function_13_3AEB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x12)
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x0, 0)
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B7B")
    Jump("loc_3BBD")

    label("loc_3B7B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B97")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BBD")

    label("loc_3B97")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BB3")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BBD")

    label("loc_3BB3")

    OP_51(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BBD")

    OP_51(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(    #226
        0x12,
        "#050F哟，怎么了？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3C52"),
        (SWITCH_DEFAULT, "loc_3C72"),
    )


    label("loc_3C52")


    ChrTalk(    #227
        0x12,
        "#052F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 16)
    Jump("loc_3CB4")

    label("loc_3C72")


    ChrTalk(    #228
        0x12,
        (
            "#050F是吗……\x01",
            "算了，随你高兴吧。\x02\x03",

            "我就在这里\x01",
            "休息休息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB4")

    label("loc_3CB4")

    SetChrSubChip(0x12, 0)
    TalkEnd(0x12)
    Return()

    # Function_13_3AEB end

    def Function_14_3CBD(): pass

    label("Function_14_3CBD")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x13)
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D4D")
    Jump("loc_3D8F")

    label("loc_3D4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D69")
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D8F")

    label("loc_3D69")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D85")
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D8F")

    label("loc_3D85")

    OP_51(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D8F")

    OP_51(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DF2")

    ChrTalk(    #229
        0x13,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E50")

    label("loc_3DF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E21")

    ChrTalk(    #230
        0x13,
        "#060F啊，怎么了？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E50")

    label("loc_3E21")


    ChrTalk(    #231
        0x13,
        (
            "#060F啊，姐姐是你们。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E50")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3EA9"),
        (SWITCH_DEFAULT, "loc_3F18"),
    )


    label("loc_3EA9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EEB")

    ChrTalk(    #232
        0x13,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F11")

    label("loc_3EEB")


    ChrTalk(    #233
        0x13,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F11")

    Call(0, 16)
    Jump("loc_3FC5")

    label("loc_3F18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F79")

    ChrTalk(    #234
        0x13,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我就在这里等，\x01",
            "有什么事就来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC2")

    label("loc_3F79")


    ChrTalk(    #235
        0x13,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我会在这里等的，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC2")

    Jump("loc_3FC5")

    label("loc_3FC5")

    SetChrSubChip(0x13, 0)
    TalkEnd(0x13)
    Return()

    # Function_14_3CBD end

    def Function_15_3FCE(): pass

    label("Function_15_3FCE")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x14)
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)
    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_405E")
    Jump("loc_40A0")

    label("loc_405E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_407A")
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A0")

    label("loc_407A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4096")
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40A0")

    label("loc_4096")

    OP_51(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40A0")

    OP_51(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)

    ChrTalk(    #236
        0x14,
        "#070F噢，有事吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4135"),
        (SWITCH_DEFAULT, "loc_4155"),
    )


    label("loc_4135")


    ChrTalk(    #237
        0x14,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Call(0, 16)
    Jump("loc_419A")

    label("loc_4155")


    ChrTalk(    #238
        0x14,
        (
            "#070F怎么，不调整了吗？\x02\x03",

            "唔，还想着能去\x01",
            "参观卢安呢，可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_419A")

    label("loc_419A")

    SetChrSubChip(0x14, 0)
    TalkEnd(0x14)
    Return()

    # Function_15_3FCE end

    def Function_16_41A3(): pass

    label("Function_16_41A3")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    OP_A3(0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4240")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 8)
    SetChrPos(0x11, -33790, 250, 46120, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4225")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_4225")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4240")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_4240")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_42A3")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 9)
    SetChrPos(0x12, -31990, 250, 46120, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4288")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_4288")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A3")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_42A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4306")
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 10)
    SetChrPos(0x13, -33850, 250, 43760, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42EB")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_42EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4306")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_4306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4369")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x4)
    SetChrChipByIndex(0x14, 11)
    SetChrPos(0x14, -31980, 250, 43650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434E")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_434E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4369")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x7)

    label("loc_4369")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_43E6")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #239
        (
            "\x07\x05※要待命的成员\x01",
            "　装备着『零力场发生器』。\x01",
            "　将其回收加入队伍的携带品。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_43E6")

    Return()

    # Function_16_41A3 end

    def Function_17_43E7(): pass

    label("Function_17_43E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43F8")
    Call(0, 35)

    label("loc_43F8")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, -3540, 0, 45230, 0)
    SetChrPos(0xF7, -3540, 0, 43990, 0)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0xF7, 0x8, 400)
    OP_4A(0x8, 255)
    OP_6D(-650, 0, 40270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_447B():
        OP_6D(-4590, 0, 45190, 2500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_447B)

    def lambda_4493():
        OP_67(0, 7240, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4493)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5634")

    ChrTalk(    #240
        0x8,
        (
            "#650F#5P呀～！\x01",
            "你们来的正是时候啊。\x02\x03",

            "因为卡露娜不在，\x01",
            "公告板的工作都堆积着呢。\x02\x03",

            "#651F马上精神抖擞、活力充沛地\x01",
            "去工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1016F#4P啊、啊哈哈……\x01",
            "还是这么有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x106,
        (
            "#053F公告板的工作\x01",
            "是打算慢慢整理完成的……\x02\x03",

            "#050F有没有其它紧急的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x8,
        (
            "#650F#5P这个，虽然工作都堆积着，\x01",
            "但没有什么紧急的委托。\x02\x03",

            "市长选举的管理是在军队的管辖之内……\x02\x03",

            "城市也正忙于市长选举，\x01",
            "游客也不多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        (
            "#1015F#4P哎呀～原来市长选举\x01",
            "那么热闹啊。\x02\x03",

            "有谁出来参选啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x8,
        (
            "#650F#5P推进旅游业的诺曼和\x01",
            "呼吁维持港湾业的波尔多斯。\x02\x03",

            "虽说只是卢安市长，\x01",
            "但其权限可是波及到全卢安地区的。\x02\x03",

            "所以玛诺利亚村的居民也会投票，\x01",
            "宣传媒体也相当关注。\x02\x03",

            "#651F这必然会成为左右\x01",
            "卢安地区未来的重要选举啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#1006F#4P啊～这样啊。\x02\x03",

            "我还未成年，不是居住民，\x01",
            "所以没有选举权……\x02\x03",

            "不过作为那个事件的相关人士，\x01",
            "还是挺在意其发展动向呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x8,
        (
            "#651F#5P这方面\x01",
            "利贝尔通讯有出特刊，\x01",
            "推荐看看哦。\x02\x03",

            "#653F啊……这么说来。\x02\x03",

            "#652F的确有一件事\x01",
            "想让你们调查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#1004F#4P想调查的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x8,
        (
            "#654F#5P嗯～怎么说呢……\x02\x03",

            "要怎么说明才好呢～？\x01",
            "实在是很困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x106,
        (
            "#555F怎么？\x01",
            "真是不干脆啊。\x02\x03",

            "就像平时一样厚着脸皮\x01",
            "一口气全说出来不就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        (
            "#651F#5P啊哈哈，好过分的话哟。\x02\x03",

            "#652F那我就说了……\x02\x03",

            "希望你们调查一下『亡灵』的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x106)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #252
        0x8,
        (
            "#654F#5P唉，我就知道\x01",
            "你们会摆出那种表情。\x02\x03",

            "所以才不想说的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        (
            "#1016F#4P……啊，不，嗯。\x01",
            "只是一下没明白过来。\x02\x03",

            "#1011F到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x8,
        (
            "#652F嗯……\x01",
            "最近１～２周呢。\x02\x03",

            "协会收到了好几起\x01",
            "关于『夜晚看见了白影』的报告。\x02\x03",

            "而且是从卢安各地发来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x101,
        "#1015F#4P夜晚看见了白影……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #256
        0x101,
        "#1020F#3S#4P然然然，然后呢！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #257
        0x106,
        (
            "#053F原来如此，然后就说是『亡灵』吗～？\x02\x03",

            "#050F要说是错觉，\x01",
            "但各地都出现就比较奇怪了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x8,
        (
            "#652F#5P嗯，是呢。\x02\x03",

            "完成公告板上的工作以外附带\x01",
            "打听一下行吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #259
        0x101,
        (
            "#1008F#4P啊，但是，那个，是吧……\x02\x03",

            "#1013F也不是那么容易的事，\x01",
            "就让我们考虑考虑吧，嗯～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    OP_63(0x8)

    ChrTalk(    #260
        0x8,
        "#653F#5P艾丝蒂尔，难不成……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 600)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x8, 600)
    Sleep(400)
    TurnDirection(0x101, 0x106, 600)

    ChrTalk(    #261
        0x101,
        (
            "#1008F#2P咦，讨厌，不是啦！？　\x01",
            "完全没有那种事哦！？\x02\x03",

            "小孩子看到我都会吓得不敢哭，这样的艾丝蒂尔\x01",
            "竟然会怕幽灵……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    ChrTalk(    #262
        0x101,
        (
            "#1007F#4P……对不起。\x01",
            "是有点害怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x8,
        (
            "#651F#5P啊哈哈。\x01",
            "好像不是有点吧。\x02\x03",

            "#650F不过，也没有造成什么实际伤害，\x01",
            "这事就当没提过吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x106,
        "#053F不……我们接受了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #265
        0x106,
        (
            "#057F……别忘了。\x01",
            "我们的任务是调查『结社』。\x02\x03",

            "就算稍微有些奇怪的征兆，\x01",
            "也该调查验证是否与『结社』有关。\x02\x03",

            "我说的没错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x101,
        "#1026F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x106,
        (
            "#053F人都有弱点的。\x02\x03",

            "偶尔示弱一下也没什么不好吧。\x02\x03",

            "#057F但是，可别什么都不做\x01",
            "就夹着尾巴逃跑哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        "#1003F#2P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x8,
        (
            "#654F#5P哎呀哎呀。\x01",
            "是不是太严格了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#1010F#2P……不，\x01",
            "阿加特说得对。\x02\x03",

            "#1002F我确实怕幽灵……\x02\x03",

            "但是和约修亚消失比起来\x01",
            "就一点也不可怕了……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #271
        0x8,
        "#653F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x106,
        "#051F嗯，这不是挺明白的吗～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #273
        0x101,
        (
            "#1006F#4P嘉恩哥哥，这个调查，\x01",
            "能交给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x8,
        (
            "#651F#5P你这么说就求之不得了。\x02\x03",

            "#652F已经收集了一些证言，\x01",
            "不过出现了３个新的目击者。\x02\x03",

            "首先是在艾尔·雷登的\x01",
            "关所工作的一名士兵。\x02\x03",

            "据说在夜巡时看到了幽灵，\x01",
            "当场吓得腰都直不起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x101,
        "#1007F#4P呜哎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x8,
        (
            "#655F#5P第二个好像是渡鸦帮的\x01",
            "成员之一。\x02\x03",

            "#650F这个有阿加特在\x01",
            "就很容易打听了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x106,
        (
            "#051F嗯，要是敢拒绝\x01",
            "就用武力撬开他的嘴。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #278
        0x101,
        (
            "#1007F#2P这就免了吧……\x02\x03",

            "#1025F武术大会时对战过，\x01",
            "好像很有洗心革面的样子哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x106,
        "#552F哼……谁知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x8,
        "#654F#5P好了好了，就拜托你了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #281
        0x8,
        (
            "#650F#5P而最后的目击者……\x01",
            "是玛西亚孤儿院的孩子们。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #282
        0x101,
        (
            "#1004F#4P咦……\x01",
            "孤儿院的孩子们！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x8,
        (
            "#650F#5P啊啊，特蕾莎院长\x01",
            "代替他们联络我的。\x02\x03",

            "顺带一提玛西亚孤儿院\x01",
            "前几天刚刚重建好。\x02\x03",

            "出于特蕾莎院长的希望，\x01",
            "据说大体和以前样式相同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        (
            "#1017F#4P是吗……太好了。\x02\x03",

            "正打算去和院长老师还有孩子们\x01",
            "打个招呼呢。\x02\x03",

            "顺便表示祝贺\x01",
            "就去问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x8,
        (
            "#651F#5P拜托了。\x02\x03",

            "#650F不过我刚才说了，这个调查并不紧急，\x01",
            "推迟点也完全没关系。\x02\x03",

            "公告板上还有其他工作，\x01",
            "就先检查一下那边好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_543F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_543F)

    def lambda_544D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_544D)
    OP_6D(-720, 0, 45530, 1500)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #286
        (
            "\x07\x05※能够自由接受的工作记载在公告板上。\x01",
            "　接近公告板会有！记号出现，\x01",
            "　右击显示工作列表。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #287
        (
            "\x07\x05※单击列表显示的各工作名，\x01",
            "　能确认工作的详细内容。\x01",
            "　确认了的内容会自动登记在手册上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_553B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_553B)

    def lambda_5549():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5549)
    OP_6D(-4590, 0, 45190, 1500)

    ChrTalk(    #288
        0x8,
        (
            "#650F#5P确认了３件目击情报就\x01",
            "再返回这里总结报告吧。\x02\x03",

            "一起研究一下搜集的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#1006F#4P嗯，明白了。\x02\x03",

            "不过，渡鸦帮在仓库区，\x01",
            "先去那里看看可能比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x106,
        (
            "#051F那么在出城之前\x01",
            "就先去港口仓库看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6749")

    label("loc_5634")


    ChrTalk(    #291
        0x8,
        (
            "#650F#5P呀～！\x01",
            "你们来的正是时候啊。\x02\x03",

            "因为卡露娜不在，\x01",
            "公告板的工作都堆积着呢。\x02\x03",

            "#651F马上精神抖擞、活力充沛地\x01",
            "去工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#1016F#4P啊、啊哈哈……\x01",
            "还是这么有精神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x103,
        (
            "#021F呵呵，心情可以理解。\x02\x03",

            "#020F那么请赶快介绍紧急的工作\x01",
            "给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#650F#5P这个，虽然工作都堆积着，\x01",
            "但没有什么紧急的委托。\x02\x03",

            "市长选举的管理是在军队的管辖之内……\x02\x03",

            "城市也正忙于市长选举，\x01",
            "游客也不多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x101,
        (
            "#1015F#4P哎呀～原来市长选举\x01",
            "那么热闹啊。\x02\x03",

            "有谁出来参选啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x8,
        (
            "#650F#5P推进旅游业的诺曼和\x01",
            "呼吁维持港湾业的波尔多斯。\x02\x03",

            "虽说只是卢安市长，\x01",
            "但其权限可是波及到全卢安地区的。\x02\x03",

            "所以玛诺利亚村的居民也会投票，\x01",
            "宣传媒体也相当关注。\x02\x03",

            "#651F这必然会成为左右\x01",
            "卢安地区未来的重要选举啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        (
            "#1006F#4P啊～这样啊。\x02\x03",

            "我还未成年，不是居住民，\x01",
            "所以没有选举权……\x02\x03",

            "不过作为那个事件的相关人士，\x01",
            "还是挺在意其发展动向呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x8,
        (
            "#651F#5P这方面\x01",
            "利贝尔通讯有出特刊，\x01",
            "推荐看看哦。\x02\x03",

            "#653F啊……这么说来。\x02\x03",

            "#652F的确有一件事\x01",
            "想让你们调查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        "#1004F#4P想调查的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x8,
        (
            "#655F#5P嗯～怎么说呢……\x02\x03",

            "要怎么说明才好呢～？\x01",
            "实在是很困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x103,
        (
            "#027F哎呀，真稀奇。\x01",
            "嘉恩居然会犹豫啊。\x02\x03",

            "平时不总是一下子就\x01",
            "给我们派一堆工作的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x8,
        (
            "#654F#5P雪拉，别这么说嘛～\x02\x03",

            "#652F那我就说了……\x02\x03",

            "希望你们调查一下『亡灵』的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    OP_63(0x103)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #303
        0x8,
        (
            "#654F#5P唉，我就知道\x01",
            "你们会摆出那种表情。\x02\x03",

            "所以才不想说的嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        (
            "#1016F#4P……啊，不，嗯。\x01",
            "只是一下没明白过来。\x02\x03",

            "#1011F到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x8,
        (
            "#652F#5P嗯……\x01",
            "最近１～２周呢。\x02\x03",

            "协会收到了好几起\x01",
            "关于『夜晚看见了白影』的报告。\x02\x03",

            "而且是从卢安各地发来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x101,
        "#1015F#4P夜晚看见了白影……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #307
        0x101,
        "#1020F#3S#4P然然然，然后呢！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #308
        0x103,
        (
            "#026F原来如此，所以才说是『亡灵』啊。\x02\x03",

            "#020F如果说是恶作剧的话，\x01",
            "但各地都出现就不符合逻辑了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x8,
        (
            "#652F#5P嗯，是呢。\x02\x03",

            "完成公告板上的工作以外附带\x01",
            "打听一下行吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #310
        0x101,
        (
            "#1008F#4P啊，但是，那个，是吧……\x02\x03",

            "#1013F也不是那么容易的事，\x01",
            "就让我们考虑考虑吧，嗯～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x103)
    OP_63(0x8)

    ChrTalk(    #311
        0x8,
        "#653F#5P艾丝蒂尔，难不成……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 600)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x8, 600)
    Sleep(400)
    TurnDirection(0x101, 0x103, 600)

    ChrTalk(    #312
        0x101,
        (
            "#1008F#2P咦，讨厌，不是啦！？　\x01",
            "完全没有那种事哦！？\x02\x03",

            "小孩子看到我都会吓得不敢哭，这样的艾丝蒂尔\x01",
            "竟然会怕幽灵……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #313
        0x101,
        (
            "#1007F#4P……对不起。\x01",
            "是有点害怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x8,
        (
            "#651F#5P啊哈哈。\x01",
            "好像不是有点吧。\x02\x03",

            "#650F不过，也没有造成什么实际伤害，\x01",
            "这事就当没提过吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x103,
        (
            "#026F等等，嘉恩。\x02\x03",

            "#020F艾丝蒂尔……\x01",
            "这件事，就接受下来吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #316
        0x103,
        (
            "#021F没问题，没问题。\x01",
            "有姐姐在嘛㈱\x02\x03",

            "#020F而且，调查这种事\x01",
            "对我们的任务也很有价值哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x101,
        "#1026F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x103,
        (
            "#026F巡回利贝尔各地\x01",
            "调查『结社』的动向……\x02\x03",

            "这正是要我们找出\x01",
            "不可见威胁的根源所在。\x02\x03",

            "#027F这和『亡灵』\x01",
            "不是很像吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#1004F#2P啊……\x02\x03",

            "#1011F是吗……\x01",
            "这么一说确实如此。\x02\x03",

            "#1007F对不起，雪拉姐。\x01",
            "说了些这么孩子气的话。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #320
        0x101,
        (
            "#1006F#4P嘉恩哥哥，这个调查\x01",
            "能交给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x8,
        (
            "#651F#5P你这么说就求之不得了。\x02\x03",

            "#652F已经收集了一些证言，\x01",
            "不过出现了３个新的目击者。\x02\x03",

            "首先是在艾尔·雷登\x01",
            "关所工作的一名士兵。\x02\x03",

            "据说在夜巡时看到了幽灵，\x01",
            "当场吓得腰都直不起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x101,
        "#1007F#4P呼哎～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x8,
        (
            "#655F#5P第二个好像是渡鸦帮的\x01",
            "成员之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x103,
        (
            "#022F渡鸦帮……\x01",
            "是卢安的不良少年集团吧。\x02\x03",

            "#522F嗯，希望能老老实实\x01",
            "配合调查就好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #325
        0x101,
        (
            "#1025F#2P嗯～我想没问题吧。\x02\x03",

            "武术大会的时候对战过，\x01",
            "好像很有洗心革面的样子哦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #326
        0x103,
        (
            "#023F哎呀。\x01",
            "有这样的事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x8,
        "#651F#5P嗯，他们的确有些自己的想法。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #328
        0x8,
        (
            "#650F#5P而最后的目击者……\x01",
            "是玛西亚孤儿院的孩子们。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #329
        0x101,
        (
            "#1004F#4P咦……\x01",
            "孤儿院的孩子们！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x8,
        (
            "#650F#5P啊啊，特蕾莎院长\x01",
            "代替他们联络我的。\x02\x03",

            "顺带一提玛西亚孤儿院\x01",
            "前几天刚刚重建好。\x02\x03",

            "出于特蕾莎院长的希望，\x01",
            "据说大体和以前样式相同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x101,
        (
            "#1017F#4P是吗……太好了。\x02\x03",

            "正打算去和院长老师还有孩子们\x01",
            "打个招呼呢。\x02\x03",

            "顺便表示祝贺\x01",
            "就去问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x8,
        (
            "#651F#5P拜托了。\x02\x03",

            "#650F不过我刚才说了，这个调查并不紧急，\x01",
            "所以推迟点也完全没关系。\x02\x03",

            "公告板上还有其他工作，\x01",
            "就先检查一下那边好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6557():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6557)

    def lambda_6565():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6565)
    OP_6D(-720, 0, 45530, 1500)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #333
        (
            "\x07\x05※能够自由接受的工作记载在公告板上。\x01",
            "　接近公告板会有！记号出现，\x01",
            "　右击显示工作列表。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #334
        (
            "\x07\x05※单击列表显示的各工作名，\x01",
            "　能确认工作的详细内容。\x01",
            "　确认了的内容会自动登记在手册上。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    def lambda_6653():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6653)

    def lambda_6661():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6661)
    OP_6D(-4590, 0, 45190, 1500)

    ChrTalk(    #335
        0x8,
        (
            "#650F#5P确认了３件目击情报之后\x01",
            "再返回这里总结报告吧。\x02\x03",

            "一起研究一下搜集的情报。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x101,
        (
            "#1006F#4P嗯，明白了。\x02\x03",

            "不过，渡鸦帮在仓库区，\x01",
            "先去那里看看可能比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x103,
        (
            "#020F那么，出城之前\x01",
            "先去港口仓库看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6749")

    OP_A2(0x1206)
    OP_28(0x81, 0x1, 0x80)
    OP_28(0x81, 0x4, 0x10)
    OP_28(0x81, 0x4, 0x20)
    OP_28(0x82, 0x4, 0x2)
    OP_28(0x82, 0x4, 0x8)
    OP_28(0x82, 0x1, 0x1)
    OP_28(0x82, 0x1, 0x2)
    OP_28(0x82, 0x1, 0x10)
    OP_28(0x82, 0x1, 0x80)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_17_43E7 end

    def Function_18_6785(): pass

    label("Function_18_6785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6796")
    Call(0, 35)

    label("loc_6796")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x101, 180, -500, 37430, 45)
    SetChrPos(0xF7, 180, -500, 37430, 45)
    SetChrPos(0xC, -3540, 0, 45230, 275)
    SetChrPos(0xD, -2540, 0, 46000, 275)
    SetChrPos(0xE, 530, 0, 38440, 0)
    OP_4A(0xE, 255)
    OP_4A(0x8, 255)
    OP_6D(-520, 0, 40270, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_686C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_686C)

    def lambda_687E():
        OP_8E(0xFE, 0xFFFFFD94, 0x0, 0x9B1E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_687E)
    Sleep(500)

    def lambda_689E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_689E)

    def lambda_68B0():
        OP_8E(0xFE, 0x226, 0x0, 0x9934, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_68B0)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xF7, 0x0)
    TurnDirection(0x101, 0xC, 400)
    TurnDirection(0xF7, 0xC, 400)

    ChrTalk(    #338
        0x101,
        "#1004F#5P啊……！\x02",
    )

    CloseMessageWindow()

    def lambda_691F():

        label("loc_691F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_691F")

    QueueWorkItem2(0xC, 1, lambda_691F)
    Sleep(200)

    def lambda_6935():

        label("loc_6935")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6935")

    QueueWorkItem2(0xD, 1, lambda_6935)
    Sleep(100)

    def lambda_694B():

        label("loc_694B")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_694B")

    QueueWorkItem2(0x8, 1, lambda_694B)

    ChrTalk(    #339
        0xC,
        "#141F#6P噢，回来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xD,
        (
            "#151F#4P小艾！\x01",
            "你回来啦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x13)

    def lambda_69A0():
        OP_6D(-3940, 0, 45120, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69A0)

    def lambda_69B8():
        OP_67(0, 6260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69B8)
    OP_43(0xF7, 0x1, 0x0, 0x14)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x8, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #341
        0x101,
        (
            "#1008F#6P奈尔、朵洛希！\x01",
            "你们怎么会在卢安？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xC,
        (
            "#141F#5P这个嘛，当然是为了采访\x01",
            "热门话题市长选举而来的嘛。\x02\x03",

            "对了，听说还发生了奇怪的事件，\x01",
            "所以就来协会问问情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x101,
        (
            "#1017F#6P奇怪的事件……\x01",
            "是那个『白影』的事吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    ChrTalk(    #344
        0x8,
        (
            "#654F其实，在你们调查期间，\x01",
            "市街发生了另外的目击事件。\x02\x03",

            "市民之间的不安\x01",
            "也在逐渐蔓延。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6B5D")

    ChrTalk(    #345
        0x106,
        (
            "#050F#6P是吗……\x01",
            "事情渐渐闹大了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B86")

    label("loc_6B5D")


    ChrTalk(    #346
        0x103,
        (
            "#022F#6P哎呀……\x01",
            "越发变得严重了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B86")


    ChrTalk(    #347
        0x8,
        (
            "#652F并且，可以断定的是……\x01",
            "这位小姐拍的照片。\x02\x03",

            "我想这是相当\x01",
            "有价值的情报……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x101,
        "#1015F#6P照片……\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #349
        0x101,
        "#1020F#6P不、不不、不会吧！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6C6E")

    ChrTalk(    #350
        0x106,
        "#052F#6P所谓的灵异照片？\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C8E")

    label("loc_6C6E")


    ChrTalk(    #351
        0x103,
        "#023F#6P所谓的灵异照片吗？\x02",
    )

    CloseMessageWindow()

    label("loc_6C8E")


    ChrTalk(    #352
        0xD,
        (
            "#150F#2P嗯～大概是吧。\x02\x03",

            "在酒店拍摄夜景的时候\x01",
            "偶然拍下来的，\x01",
            "我还搞不太清楚呢～\x02\x03",

            "先看看吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x240090, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #353
        "#1020F………………………（咕噜）\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6D90")
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #354
        (
            "#552F……什么～？\x01",
            "这样可以确定这次事件的真实性了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_6DD7")

    label("loc_6D90")

    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #355
        (
            "#025F……唉。\x01",
            "这样可以确定这次事件的真实性了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6DD7")

    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #356
        (
            "#1016F啊、啊哈哈……\x01",
            "要下结论也太早了点吧。\x02\x03",

            "也可能是导力照相机\x01",
            "出毛病了也不一定……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName("朵洛希")

    AnonymousTalk(    #357
        (
            "#150F嗯～故障～？\x01",
            "不可能是故障哦～\x02\x03",

            "#151F这是从中央工房买的最新机种，\x01",
            "维护得也很仔细呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #358
        "#1019F不是真的！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 200, -1, -1)
    SetChrName("朵洛希")

    AnonymousTalk(    #359
        "#154F小艾，好可怕……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #360
        0x8,
        (
            "#654F嗯，也就是说\x01",
            "事件变得\x01",
            "很真实化了……\x02\x03",

            "#652F这件事就算和媒体\x01",
            "配合应该也没什么坏处。\x02\x03",

            "现在就赶快把各地\x01",
            "调查的情况报告了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1015F#6P嗯、嗯……\x01",
            "３个地方都调查过了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xE, 200, -500, 37500, 0)

    NpcTalk(    #362
        0xE,
        "青年的声音",
        "#2P不、不好了～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_707E():

        label("loc_707E")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_707E")

    QueueWorkItem2(0x101, 1, lambda_707E)

    def lambda_708F():

        label("loc_708F")

        TurnDirection(0xF7, 0xE, 400)
        OP_48()
        Jump("loc_708F")

    QueueWorkItem2(0xF7, 1, lambda_708F)

    def lambda_70A0():

        label("loc_70A0")

        TurnDirection(0xC, 0xE, 400)
        OP_48()
        Jump("loc_70A0")

    QueueWorkItem2(0xC, 1, lambda_70A0)

    def lambda_70B1():

        label("loc_70B1")

        TurnDirection(0xD, 0xE, 400)
        OP_48()
        Jump("loc_70B1")

    QueueWorkItem2(0xD, 1, lambda_70B1)

    def lambda_70C2():

        label("loc_70C2")

        TurnDirection(0x8, 0xE, 400)
        OP_48()
        Jump("loc_70C2")

    QueueWorkItem2(0x8, 1, lambda_70C2)

    def lambda_70D3():
        OP_6D(-3020, 0, 43600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70D3)

    def lambda_70EB():
        OP_67(0, 6260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_70EB)
    Sleep(500)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)

    def lambda_7118():
        OP_8E(0xFE, 0x0, 0x0, 0x9916, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_7118)

    def lambda_7133():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_7133)
    WaitChrThread(0xE, 0x0)

    def lambda_714A():
        OP_8E(0xFE, 0xFFFFF51A, 0x0, 0xA316, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_714A)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xE, 0x1)
    TurnDirection(0xE, 0x101, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0x8, 0x1)

    ChrTalk(    #363
        0x101,
        (
            "#1004F#5P怎、怎么了！\x01",
            "那么慌张……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_71DA")

    ChrTalk(    #364
        0x106,
        "#054F#2P有抢劫吗！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_71FA")

    label("loc_71DA")


    ChrTalk(    #365
        0x103,
        "#024F#2P难道出现了魔兽！？\x02",
    )

    CloseMessageWindow()

    label("loc_71FA")


    ChrTalk(    #366
        0xE,
        "#6P不、不是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xE,
        (
            "#6P诺曼先生的支持者\x01",
            "波尔多斯的支持者\x01",
            "吵起来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xE,
        (
            "#6P现在正在伦格兰德大桥\x01",
            "相互对峙中！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #369
        0x101,
        "#1005F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_72F4")

    ChrTalk(    #370
        0x106,
        (
            "#057F#2P说到诺曼和波尔多斯，\x01",
            "两人都是市长选举的候选人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7333")

    label("loc_72F4")


    ChrTalk(    #371
        0x103,
        (
            "#022F#2P说到诺曼和波尔多斯，\x01",
            "两人都是市长选举的候选人吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7333")


    ChrTalk(    #372
        0xC,
        (
            "#141F#5P喔喔。\x01",
            "这可是相当不错的新闻。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #373
        0xC,
        "#144F#5P朵洛希，快走！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xD,
        "#151F#2P是，前辈！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 600)
    TurnDirection(0x101, 0xC, 600)
    TurnDirection(0xF7, 0xC, 600)

    ChrTalk(    #375
        0xD,
        "#150F#2P小艾，回头见哦。\x02",
    )

    CloseMessageWindow()

    def lambda_73D2():
        OP_6D(-1770, 0, 42260, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_73D2)

    def lambda_73EA():
        OP_67(0, 6260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_73EA)
    TurnDirection(0xC, 0x101, 600)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xC, 0x1, 0x0, 0x15)

    def lambda_7422():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7422)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_7454():
        OP_91(0xFE, 0x12C, 0x0, 0x12C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7454)

    def lambda_746F():

        label("loc_746F")

        TurnDirection(0x101, 0xC, 0)
        OP_48()
        Jump("loc_746F")

    QueueWorkItem2(0x101, 2, lambda_746F)

    def lambda_7480():

        label("loc_7480")

        TurnDirection(0xF7, 0xC, 0)
        OP_48()
        Jump("loc_7480")

    QueueWorkItem2(0xF7, 2, lambda_7480)
    OP_43(0xD, 0x1, 0x0, 0x16)
    WaitChrThread(0xD, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)

    def lambda_74A5():
        OP_6D(-3750, 0, 44170, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_74A5)

    def lambda_74BD():
        OP_67(0, 6260, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_74BD)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #376
        0x101,
        "#1019F#5P好、好快啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)

    def lambda_7503():
        OP_8F(0xFE, 0xFFFFF6DC, 0x0, 0xAAF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7503)
    WaitChrThread(0xF7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7564")

    ChrTalk(    #377
        0x106,
        (
            "#057F#4P以防万一我们也去吧。\x02\x03",

            "万一要打起来\x01",
            "得赶快调停。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_759D")

    label("loc_7564")


    ChrTalk(    #378
        0x103,
        (
            "#022F#4P我们也去吧。\x02\x03",

            "万一要打起来\x01",
            "得插手调停才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_759D")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #379
        0x101,
        "#1002F#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x8,
        (
            "#652F#5P抱歉。\x01",
            "就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 105, 400)
    OP_4B(0x8, 255)
    OP_4B(0xE, 255)
    OP_43(0xE, 0x0, 0x6, 0x2)
    OP_A2(0x121C)
    OP_28(0x82, 0x1, 0x800)
    EventEnd(0x0)
    Return()

    # Function_18_6785 end

    def Function_19_75FC(): pass

    label("Function_19_75FC")

    OP_8E(0xFE, 0xFFFFF434, 0x0, 0xAA50, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_19_75FC end

    def Function_20_7618(): pass

    label("Function_20_7618")

    Sleep(500)
    OP_8E(0xFE, 0xFFFFF8D0, 0x0, 0xAA50, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xC, 400)
    Return()

    # Function_20_7618 end

    def Function_21_7639(): pass

    label("Function_21_7639")

    OP_8F(0xFE, 0xFFFFFFEC, 0xFFFFFE0C, 0x95CE, 0x1388, 0x0)

    def lambda_7653():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7653)
    OP_8F(0xFE, 0x5A, 0xFFFFFE0C, 0x927C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_21_7639 end

    def Function_22_7679(): pass

    label("Function_22_7679")

    Sleep(500)
    OP_8C(0xFE, 180, 0)
    OP_8F(0xFE, 0xFFFFF63C, 0x0, 0xAD34, 0x1388, 0x0)
    OP_8F(0xFE, 0xFFFFFFEC, 0xFFFFFE0C, 0x95CE, 0x1388, 0x0)

    def lambda_76B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_76B3)
    OP_8F(0xFE, 0x5A, 0xFFFFFE0C, 0x927C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_22_7679 end

    def Function_23_76D9(): pass

    label("Function_23_76D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_76EA")
    Call(0, 35)

    label("loc_76EA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_4A(0x8, 255)
    SetChrPos(0x101, -3540, 0, 45030, 90)
    SetChrPos(0xF7, -3550, 0, 46010, 125)
    SetChrPos(0x104, -2090, 0, 45270, 268)
    SetChrPos(0xC, -3440, 0, 43970, 44)
    SetChrPos(0xD, -2380, 0, 44040, 10)
    OP_6D(460, 0, 37310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(2000)

    def lambda_77A6():
        OP_6D(-3150, 0, 45370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_77A6)

    def lambda_77BE():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77BE)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #381
        0x104,
        (
            "#034F多么薄情啊……\x02\x03",

            "面对久别重逢\x01",
            "的命运对象，\x01",
            "这样的行为实在太过分了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_789C")

    ChrTalk(    #382
        0x101,
        (
            "#1007F#5P什么命运的对象啊……\x02\x03",

            "#1019F那，奥利维尔\x01",
            "怎么会在卢安啊。\x02\x03",

            "不是在\x01",
            "亚尔摩的温泉吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_790D")

    label("loc_789C")


    ChrTalk(    #383
        0x101,
        (
            "#1007F#5P什么命运的对象啊……\x02\x03",

            "#1019F那，奥利维尔\x01",
            "怎么会在卢安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x103,
        (
            "#020F#5P记得是在亚尔摩温泉\x01",
            "才对啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_790D")


    ChrTalk(    #385
        0x104,
        (
            "#030F呵，其实穆拉\x01",
            "给红叶亭发来了联络。\x02\x03",

            "特地告诉我\x01",
            "艾丝蒂尔你回来了哦。\x02\x03",

            "#031F我想必须要来见你才行，\x01",
            "就拼了命赶过来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x101,
        (
            "#1007F#5P好、好意我心领了，\x01",
            "说实话还真没有高兴的感觉……\x02\x03",

            "#1017F不过，诞辰庆典之后\x01",
            "就再没见过面呢。\x02\x03",

            "谢谢，奥利维尔。\x01",
            "能再见到你真好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x104,
        (
            "#033F是、是吗……\x02\x03",

            "#032F唔～艾丝蒂尔\x01",
            "一坦率好像浑身不对劲了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #388
        0x104,
        (
            "#037F不多多挖苦我的话，\x01",
            "嗯……会欲求不满的哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #389
        0x101,
        (
            "#1014F#5P#3S不要红着脸\x01",
            "再说这种轻浮的话！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #390
        0x101,
        "#1019F#5P唉……算了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #391
        0x101,
        (
            "#1007F#6P嘉恩哥哥。\x01",
            "这是政变事件的时候\x01",
            "帮助过我们的奥利维尔。\x02\x03",

            "从埃雷波尼亚来的演奏家。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #392
        0x8,
        (
            "#650F啊……\x01",
            "真是厉害的人啊。\x02\x03",

            "既然如此，\x01",
            "就让他一起听报告\x01",
            "也没关系吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7CBE")
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #393
        0x106,
        (
            "#552F#2P本来正要把他当成是\x01",
            "外部人员赶出去的……\x02\x03",

            "想想他也不会乖乖出去的，\x01",
            "那就不用理他了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x104,
        (
            "#031F哈哈哈。\x01",
            "不愧是阿加特。\x02\x03",

            "关于我的事\x01",
            "非常了解呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #395
        0x106,
        (
            "#055F#5P完全是\x01",
            "两回事！\x02\x03",

            "那个时候只是一起作战过，\x01",
            "没怎么说过话！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D7D")

    label("loc_7CBE")

    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #396
        0x103,
        (
            "#020F#2P嗯，算了吧？\x02\x03",

            "反正就算不让他听，\x01",
            "他也死缠烂打跟着的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x104,
        (
            "#031F哈哈哈。\x01",
            "不愧是雪拉。\x02\x03",

            "关于我的事\x01",
            "非常了解呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #398
        0x103,
        (
            "#027F#5P背景是不大清楚，\x01",
            "性格方面还算大概了解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D7D")


    ChrTalk(    #399
        0x101,
        "#1019F#6P……嗯，随他吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x8,
        (
            "#651FＯＫ。\x01",
            "这样也比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 0, 300)

    ChrTalk(    #401
        0xC,
        (
            "#142F怎样都好，\x01",
            "赶快说来听听吧。\x02\x03",

            "我们可是在等着\x01",
            "收集市长选举的消息呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    def lambda_7E1D():
        TurnDirection(0xF7, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7E1D)

    def lambda_7E2B():
        TurnDirection(0x8, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7E2B)

    def lambda_7E39():
        TurnDirection(0x104, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E39)

    def lambda_7E47():
        TurnDirection(0xD, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7E47)

    ChrTalk(    #402
        0x101,
        (
            "#1007F#5P是是，知道啦。\x02\x03",

            "#1002F那么就按照询问的顺序\x01",
            "报告目击情报……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #403
        (
            "\x07\x05除了报告各地的目击情报之外\x01",
            "还说明了凯文神父的见解。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #404
        0x8,
        (
            "#650F原来如此……\x01",
            "收集得很具体呢。\x02\x03",

            "至少已经调查到\x01",
            "足够多的情报了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        "#1015F#5P嗯～是吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0xC,
        (
            "#141F不过，刚才骚动时民众说的\x01",
            "为了妨碍市长选举对手阵营\x01",
            "而搞的恶作剧应该是不可能的。\x02\x03",

            "且不说诺曼的儿子，\x01",
            "威胁孤儿院和关所的士兵\x01",
            "想不出有什么用。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_803C")

    ChrTalk(    #407
        0x106,
        (
            "#050F#2P亡灵确实在天上飞。\x02\x03",

            "这应该不是一般人\x01",
            "能简单做到的技巧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8083")

    label("loc_803C")


    ChrTalk(    #408
        0x103,
        (
            "#022F#2P亡灵确实在天上飞。\x02\x03",

            "这应该不是一般人\x01",
            "能简单做到的技巧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8083")

    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #409
        0xD,
        (
            "#151F#6P那么果然\x01",
            "是货真价实的幽灵吗～\x02\x03",

            "可能是被戴上面具，\x01",
            "在被幽禁中疯了的\x01",
            "太古贵族之类～\x02\x03",

            "经过数百年来到现代，\x01",
            "化为怨灵苏醒了～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #410
        0x101,
        (
            "#1019F#5P那、那么恐怖的事\x01",
            "不要说得那么开心啦。\x02\x03",

            "#1015F再说，所谓幽灵\x01",
            "好像都是被人或者地方所束缚。\x02\x03",

            "这好像有所不同吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #411
        0x104,
        (
            "#035F……不，\x01",
            "这可难说。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    def lambda_8213():
        TurnDirection(0xF7, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8213)

    def lambda_8221():
        TurnDirection(0x8, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8221)

    def lambda_822F():
        TurnDirection(0xC, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_822F)

    def lambda_823D():
        TurnDirection(0xD, 0x104, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_823D)

    ChrTalk(    #412
        0x101,
        "#1004F#5P怎、怎么了，奥利维尔。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8290")

    ChrTalk(    #413
        0x106,
        "#052F#5P想到什么了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_82AC")

    label("loc_8290")


    ChrTalk(    #414
        0x103,
        "#023F#5P想到什么了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_82AC")


    ChrTalk(    #415
        0x104,
        (
            "#030F不，是不是幽灵\x01",
            "我也无法判断……\x02\x03",

            "不过听了艾丝蒂尔的报告，\x01",
            "觉得有几个地方值得注意。\x02\x03",

            "对于那个白影，它不被人和地方\x01",
            "所束缚这样的说法，\x01",
            "我稍微有点疑问。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x8,
        (
            "#650F哎呀，真了不起。\x02\x03",

            "#651F我也正在考虑\x01",
            "同一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x104,
        (
            "#031F呵呵，果然是吗～？\x02\x03",

            "#030F作为旅行者，我最近\x01",
            "经常仔细观察王国地图……\x02\x03",

            "首先请关注\x01",
            "卢安地区吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS133._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS200._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS201._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS202._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS203._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #418
        (
            "#032F那么……\x01",
            "关于艾丝蒂尔等人调查的\x01",
            "３处目击地点。\x02\x03",

            "是这里，这里，和这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #419
        (
            "#1015F嗯……\x02\x03",

            "卢安南街区和\x01",
            "艾尔·雷登关所，\x01",
            "还有玛西亚孤儿院。\x02\x03",

            "是啊，这３处怎么了？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #420
        (
            "#035F这３处的证言\x01",
            "有着一条很明显不同的信息，\x01",
            "而事实就会从这信息中浮现出来。\x02\x03",

            "#030F艾丝蒂尔。\x01",
            "你觉得这个不同的信息是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #421
        (
            "#1002F３个证言\x01",
            "明显不同的信息……\x02\x03",

            "#1004F那、那是……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #422
        "\x18\x07\x05３处证言中有明显不同的地方是？\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "【白影出现的时间】\x01",      # 0
            "【白影离去的方向】\x01",      # 1
            "【白影采取的行动】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_877D"),
        (1, "loc_88B4"),
        (2, "loc_88FE"),
        (SWITCH_DEFAULT, "loc_8A45"),
    )


    label("loc_877D")

    OP_2B(0x82, 0x1)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #423
        (
            "\x07\x00#030F嗯，孤儿院的孩子\x01",
            "说是在晚饭后看见的幽灵，\x01",
            "而其它两人都是半夜……\x02\x03",

            "每个证言说的都是夜晚，\x01",
            "可以说其实是差不多的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #424
        "\x07\x00#1007F嗯～是吗……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 50, -1, -1)
    SetChrName("嘉恩")

    AnonymousTalk(    #425
        (
            "\x07\x00#651F那么我来\x01",
            "回答吧。\x02\x03",

            "#650F就是幽灵离去的方向吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #426
        "\x07\x00#1004F啊……！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_8A45")

    label("loc_88B4")

    OP_2B(0x82, 0x3)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #427
        (
            "\x07\x00#1018F明白了！\x01",
            "也就是白影离去的方向吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_8A45")

    label("loc_88FE")

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #428
        (
            "\x07\x00#030F不，３处证言\x01",
            "重合的部分很多。\x02\x03",

            "对孤儿院的孩子打了招呼\x01",
            "可称作例外……\x02\x03",

            "不过除此以外，转着圈跳着舞\x01",
            "向天空飞去这些\x01",
            "都是相当相似的行动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #429
        "\x07\x00#1007F嗯～是吗……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 50, -1, -1)
    SetChrName("嘉恩")

    AnonymousTalk(    #430
        (
            "\x07\x00#651F那么我来\x01",
            "回答吧。\x02\x03",

            "#650F就是幽灵离去的方向吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #431
        "\x07\x00#1004F啊……！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_8A45")

    label("loc_8A45")

    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #432
        (
            "\x07\x00#031F嗯，没错。\x02\x03",

            "#030F南街区不良少年的证言\x01",
            "是白影消失在『东北』……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #433
        (
            "\x07\x00#030F艾尔·雷登士兵的证言\x01",
            "是白影消失在『北』……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #434
        (
            "\x07\x00#035F而孤儿院孩子的证言\x01",
            "是白影消失在『东』……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #435
        "\x07\x00#1004F#4S啊啊啊！？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8C06")
    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("阿加特")

    AnonymousTalk(    #436
        "#051F呵，是那样的吗……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_8C34")

    label("loc_8C06")

    SetMessageWindowPos(75, 250, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #437
        "#020F的确很隐蔽啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_8C34")

    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("奈尔")

    AnonymousTalk(    #438
        (
            "#141F原来如此啊。\x02\x03",

            "就是说幽灵离去的地方\x01",
            "可以确定了，是吗～？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #439
        (
            "#031F呵呵～就是那样。\x02\x03",

            "#030F『杰尼丝王立学院』……\x01",
            "好像就在这附近。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 0, 0)
    OP_C6(0x4, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #440
        0x101,
        (
            "#1001F#5P奥利维尔……\x01",
            "你真够机灵的。\x02\x03",

            "#1006F既然如此，幽灵也好，\x01",
            "什么也好都无所谓了。\x02\x03",

            "赶紧去调查吧！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8DE7")
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #441
        0x106,
        (
            "#051F#2P呼……\x01",
            "嘉恩，你没疑问吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E1B")

    label("loc_8DE7")

    TurnDirection(0x103, 0x8, 400)

    ChrTalk(    #442
        0x103,
        (
            "#020F#2P嘉恩。\x01",
            "我们要去学院，没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E1B")


    ChrTalk(    #443
        0x8,
        (
            "#650F啊啊，请认真调查，\x01",
            "最好能成功解决问题。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 400)
    Sleep(500)

    ChrTalk(    #444
        0x8,
        (
            "#650F利贝尔通讯的同志\x01",
            "现在打算怎么做？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E8B():
        TurnDirection(0x101, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8E8B)

    def lambda_8E99():
        TurnDirection(0xF7, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8E99)

    def lambda_8EA7():
        TurnDirection(0x104, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8EA7)

    def lambda_8EB5():
        TurnDirection(0xD, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8EB5)

    ChrTalk(    #445
        0xC,
        (
            "#145F这个嘛，关键的市长选举\x01",
            "还得去采访……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xD, 400)
    Sleep(500)

    ChrTalk(    #446
        0xC,
        (
            "#141F#5P好吧，朵洛希。\x01",
            "这个事就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xD,
        (
            "#151F#6P好～明白了～\x02\x03",

            "我一定会努力\x01",
            "拍出好的灵异照片的～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xC,
        (
            "#144F#5P不是！\x01",
            "是要你去了解事件的真相。\x02\x03",

            "跟艾丝蒂尔他们去\x01",
            "做幽灵事件的采访!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0xD,
        (
            "#153F#6P啊，原来如此。\x02\x03",

            "#151F虽然还不大明白啦～\x01",
            "但我一定尽心尽力～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x101,
        (
            "#1019F#2P我、我说。\x01",
            "别说得那么轻松好不好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #451
        0x8,
        (
            "#651F好了好了。\x02\x03",

            "你们也提供了照片，\x01",
            "就算礼尚往来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_909B")

    ChrTalk(    #452
        0x106,
        "#552F#2P呼……没办法了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_90C2")

    label("loc_909B")


    ChrTalk(    #453
        0x103,
        (
            "#021F#2P嗯，就这点小事\x01",
            "没关系的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90C2")


    ChrTalk(    #454
        0x101,
        (
            "#1007F#2P嗯～感觉紧张感\x01",
            "越来越淡了。\x02\x03",

            "#1017F不过，这样倒也好。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #455
        0xC,
        (
            "#141F就这样了，\x01",
            "事件的调查就拜托了。\x02\x03",

            "我接着去采访\x01",
            "两位候选人。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 135, 400)

    def lambda_915F():

        label("loc_915F")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_915F")

    QueueWorkItem2(0x101, 1, lambda_915F)

    def lambda_9170():

        label("loc_9170")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9170")

    QueueWorkItem2(0xF7, 1, lambda_9170)

    def lambda_9181():

        label("loc_9181")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9181")

    QueueWorkItem2(0x104, 1, lambda_9181)

    def lambda_9192():

        label("loc_9192")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_9192")

    QueueWorkItem2(0xD, 1, lambda_9192)

    def lambda_91A3():

        label("loc_91A3")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_91A3")

    QueueWorkItem2(0x8, 1, lambda_91A3)

    def lambda_91B4():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xA0FA, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_91B4)
    Sleep(700)

    def lambda_91D4():
        OP_8E(0xFE, 0xFFFFFB1E, 0x0, 0xA0FA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_91D4)

    def lambda_91EF():
        OP_6D(-2280, 0, 44400, 1000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_91EF)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #456
        0xC,
        (
            "#143F……\x01",
            "对了，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)
    Sleep(500)

    ChrTalk(    #457
        0xC,
        (
            "#140F……关于约修亚，\x01",
            "我从你父亲那儿听说了一些事。\x02\x03",

            "谜之组织的确令人在意……\x02\x03",

            "如果有相关信息\x01",
            "我会马上联络协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x101,
        "#1004F#2P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0xC,
        (
            "#144F所以呢……\x01",
            "好了，你加油吧！\x02\x03",

            "那、那我走了！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 135, 600)

    def lambda_92FF():
        OP_6D(-1770, 0, 42260, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_92FF)

    def lambda_9317():
        OP_8E(0xFE, 0x96, 0x0, 0x9A1A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9317)
    WaitChrThread(0xC, 0x1)

    def lambda_9337():
        OP_8E(0xFE, 0x19A, 0xFFFFFE0C, 0x9114, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_9337)
    Sleep(200)

    def lambda_9357():
        OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9357)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xC, 0x1)
    Sleep(500)
    OP_6D(-3790, 0, 46180, 1500)
    SetChrFlags(0xC, 0x80)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x104, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0x8, 0xFF)

    ChrTalk(    #460
        0x101,
        "#1025F#5P奈尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0xD,
        (
            "#151F#5P啊哈哈。\x01",
            "前辈还害羞呢～\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #462
        0xD,
        (
            "#150F#6P前辈好像听了卡西乌斯先生的话之后\x01",
            "相当震惊呢。\x02\x03",

            "不知道自己能帮什么忙，\x01",
            "他好像一直很烦恼呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x101,
        (
            "#1008F#5P这、这样啊。\x02\x03",

            "#1016F真是的……\x01",
            "该说他是不坦率呢还是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xD,
        (
            "#150F#6P这么说我也一样，\x01",
            "如果在采访中发现值得注意的消息\x01",
            "也会马上联络协会的～\x02\x03",

            "#151F所以小艾。\x01",
            "要·加·油·哦～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x101,
        (
            "#1012F#5P嗯，谢谢。\x02\x03",

            "#1018F那么……\x01",
            "去王立学院吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #466
        0x8,
        (
            "#650F王立学院那边\x01",
            "我会去联络的。\x02\x03",

            "那么就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    OP_A2(0x121D)
    NewScene("ED6_DT21/T2100   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_23_76D9 end

    def Function_24_959C(): pass

    label("Function_24_959C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_95AD")
    Call(0, 35)

    label("loc_95AD")

    EventBegin(0x0)
    OP_1D(0xC)
    SetChrPos(0x101, -3540, 0, 46000, 270)
    SetChrPos(0xF7, -2470, 0, 45400, 270)
    SetChrPos(0x104, -2720, 0, 44400, 270)
    SetChrPos(0x105, -3540, 0, 43930, 315)
    OP_6D(-4410, 0, 45930, 0)
    OP_67(0, 6720, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()
    OP_28(0x84, 0x1, 0x40)
    OP_28(0x84, 0x1, 0x80)
    OP_28(0x84, 0x1, 0x100)
    OP_28(0x84, 0x1, 0x200)

    ChrTalk(    #467
        0x8,
        (
            "#652F#5P是吗……辛苦了。\x02\x03",

            "#655F『噬身之蛇』……\x02\x03",

            "听卡西乌斯先生说起的时候，\x01",
            "说实话，还半信半疑……\x02\x03",

            "#652F总而言之，\x01",
            "先给你们这次调查的报酬吧。\x02\x03",

            "虽然没想到\x01",
            "会变成这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x82, 0x4, 0x10)
    OP_AF(0x67, 0x82)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x83, 0x4, 0x10)
    OP_28(0x83, 0x4, 0x20)
    OP_28(0x84, 0x4, 0x10)
    OP_28(0x84, 0x4, 0x20)

    ChrTalk(    #468
        0x8,
        (
            "#652F调查结果\x01",
            "我马上向王国军报告。\x02\x03",

            "军队那边也相当\x01",
            "需要情报呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_97E6")

    ChrTalk(    #469
        0x106,
        (
            "#050F啊啊，拜托了。\x02\x03",

            "考虑到那个投影装置，\x01",
            "那个组织肯定不简单。\x02\x03",

            "而且居然连『福音』\x01",
            "都拿出来了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9857")

    label("loc_97E6")


    ChrTalk(    #470
        0x103,
        (
            "#022F嗯嗯，拜托了。\x02\x03",

            "考虑到那个投影装置，\x01",
            "那个组织肯定具有相当大的规模。\x02\x03",

            "而且居然连『福音』\x01",
            "都拿出来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9857")


    ChrTalk(    #471
        0x104,
        (
            "#030F看来结社的目的\x01",
            "似乎是使用新『福音』\x01",
            "做实验呢。\x02\x03",

            "幽灵骚动，似乎只是\x01",
            "凭兴趣的实验结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        (
            "#1002F#2P怪盗布卢布兰……\x02\x03",

            "那个家伙，称呼自己\x01",
            "为『执行者』对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x8,
        (
            "#652F#5P恐怕他是『结社』\x01",
            "精英吧。\x02\x03",

            "根据推察，那个洛伦斯少尉\x01",
            "应该也和他立场相似吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x101,
        "#1003F#2P………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #475
        0x105,
        "#043F#6P艾丝蒂尔，那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Sleep(400)

    ChrTalk(    #476
        0x101,
        (
            "#1007F#5P嗯，我知道……\x02\x03",

            "#1003F『漆黑之牙』……\x02\x03",

            "那天，约修亚是这样\x01",
            "称呼自己的……\x02\x03",

            "#1025F大概约修亚也是\x01",
            "那种『执行者』吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9ABF")

    ChrTalk(    #477
        0x106,
        (
            "#053F原来如此啊……\x02\x03",

            "和那个混帐怪盗同等级的话，\x01",
            "那家伙的专业技术也能理解了。\x02\x03",

            "#552F搞不好是隐藏实力\x01",
            "伪装了自己也不一定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B48")

    label("loc_9ABF")


    ChrTalk(    #478
        0x103,
        (
            "#025F第一次见面的时候\x01",
            "就觉得他不一般……\x02\x03",

            "没想到小小年纪，竟然\x01",
            "和那怪盗男同等级……\x02\x03",

            "#522F或许那孩子，是隐藏了\x01",
            "自己的实力也说不定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B48")


    ChrTalk(    #479
        0x101,
        "#1003F#5P嗯……可能吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #480
        0x101,
        "#1002F#2P……对了，嘉恩哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x8,
        "#653F#5P怎么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0x101,
        (
            "#1002F#2P那个怪盗男说\x01",
            "结社的计划才刚刚开始。\x02\x03",

            "大概还会在利贝尔各地\x01",
            "做各种事。\x02\x03",

            "其它的地方支部\x01",
            "没发来什么情报吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x8,
        (
            "#654F#5P嗯……\x01",
            "现在没有特别的情报呢。\x02\x03",

            "#652F不过，艾丝蒂尔说得对，\x01",
            "结社在各地开始暗中活动\x01",
            "的可能性极高。\x02\x03",

            "幽灵骚动也告一段落了，\x01",
            "你们转移到其它地区比较好。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_9CFE")

    ChrTalk(    #484
        0x106,
        (
            "#051F啊啊。\x01",
            "我也正在考虑这个。\x02\x03",

            "哪个支部比较缺人手？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D36")

    label("loc_9CFE")


    ChrTalk(    #485
        0x103,
        (
            "#020F是啊。\x01",
            "我也是这么想的。\x02\x03",

            "哪个支部比较缺人手？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D36")


    ChrTalk(    #486
        0x8,
        (
            "#650F#5P稍微缺乏人手的话\x01",
            "应该是蔡斯支部。\x02\x03",

            "原本应该在蔡斯的冈多夫\x01",
            "好像去了王都那里。\x02\x03",

            "看上去很吃力的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x101,
        (
            "#1006F#2P那么，我们\x01",
            "最好去帮忙呢。\x02\x03",

            "不过，卢安支部不要紧吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0x8,
        (
            "#651F#5P其实，柏斯支部的斯丁克\x01",
            "数日后会来这边。\x02\x03",

            "之前就让梅尔茨一个人\x01",
            "想办法撑着吧。\x02\x03",

            "#650F对了，到了蔡斯\x01",
            "最好去找一下拉赛尔博士。\x02\x03",

            "有关新『福音』的事\x01",
            "最好借助博士的智慧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0x101,
        (
            "#1006F#2P嗯，确实是呢。\x02\x03",

            "也想见见提妲了，\x01",
            "就立刻出发去中央工房吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0x104,
        (
            "#031F那么准备好之后\x01",
            "就马上去飞船坪吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 400)
    Sleep(500)

    ChrTalk(    #491
        0x104,
        (
            "#030F嘉恩先生。\x01",
            "麻烦你安排４张船票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x8,
        "#653F#5P咦……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #493
        0x101,
        (
            "#1019F#5P干嘛突然\x01",
            "做这种厚脸皮的总结性发言啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #494
        0x101,
        "#1004F#5P……啊，４张？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A08B")

    ChrTalk(    #495
        0x104,
        (
            "#035F呵，艾丝蒂尔和阿加特。\x02\x03",

            "#030F然后是我和\x01",
            "公主殿下的份，这还用说吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x101,
        "#1005F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #497
        0x106,
        (
            "#552F#2P就觉得是这样……\x01",
            "以后还打算跟着？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A138")

    label("loc_A08B")


    ChrTalk(    #498
        0x104,
        (
            "#035F呵，艾丝蒂尔和雪拉。\x02\x03",

            "#030F然后是我和\x01",
            "公主殿下的份，这还用说吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x101,
        "#1005F#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #500
        0x103,
        (
            "#020F#2P就觉得是这样……\x01",
            "以后还打算跟着来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A138")

    TurnDirection(0x104, 0xF7, 400)

    ChrTalk(    #501
        0x104,
        (
            "#031F寻找约修亚\x01",
            "是我作为爱之猎人的使命。\x02\x03",

            "并且还遇上了一个好对手，\x01",
            "同行的理由应该很充分了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #502
        0x101,
        (
            "#1019F#5P你、你那些\x01",
            "乱七八糟的理由先不提了……\x02\x03",

            "怎么连科洛丝\x01",
            "都一起卷进来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0x105,
        (
            "#542F#6P不……\x02\x03",

            "其实我也有\x01",
            "同样的请求。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #504
        0x101,
        "#1004F#5P咦～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x8, 400)

    ChrTalk(    #505
        0x105,
        (
            "#047F#6P在利贝尔暗中活跃的\x01",
            "神秘组织『结社』。\x02\x03",

            "身为拥有王位继承权的人\x01",
            "不能置之不理。\x02\x03",

            "#043F而且更重要的是……\x02\x03",

            "我想帮助\x01",
            "艾丝蒂尔和约修亚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0x101,
        (
            "#1008F#5P科洛丝……\x02\x03",

            "但、但是\x01",
            "学院的课程怎么办？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0x105,
        (
            "#542F#6P其实今天早上，我向科林兹校长\x01",
            "递交了休学申请。\x02\x03",

            "考试的成绩没有问题了，\x01",
            "晋级需要的学分也够了。\x02\x03",

            "#041F和乔儿、汉斯也商量过，\x01",
            "他们说『你就去吧』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0x101,
        "#1016F#5P什、什么时候……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A563")

    ChrTalk(    #509
        0x106,
        (
            "#051F#2P哎呀哎呀。\x01",
            "真是位做事干脆的公主啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x105,
        (
            "#540F#6P对、对不起……\x01",
            "先斩后奏确实不对。\x02\x03",

            "#043F那个……不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0x101,
        (
            "#1008F#5P呵呵……\x01",
            "怎么可能不行嘛！\x02\x03",

            "#1018F既然如此，\x01",
            "就不客气地劳你帮忙喽！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #512
        0x101,
        "#1006F#5P阿加特也没意见吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x106,
        (
            "#051F#2P嗯，好吧。\x02\x03",

            "无论是魔法还是那只隼，\x01",
            "公主在可真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x105,
        (
            "#045F#6P太好了……\x02\x03",

            "#048F谢谢你们。\x01",
            "艾丝蒂尔，阿加特。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6E6")

    label("loc_A563")


    ChrTalk(    #515
        0x103,
        (
            "#027F#2P呵呵。\x01",
            "真不愧是公主殿下，做事如此干脆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0x105,
        (
            "#540F#6P对、对不起……\x01",
            "先斩后奏确实不对。\x02\x03",

            "#043F那个……不行吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0x101,
        (
            "#1016F#5P呵呵……\x01",
            "怎么可能不行嘛！\x02\x03",

            "#1018F既然如此，\x01",
            "就不客气地劳你帮忙喽！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #518
        0x101,
        "#1006F#5P雪拉姐也没意见吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x103,
        (
            "#021F#2P嗯嗯，当然了。\x02\x03",

            "无论是魔法还是那只隼，\x01",
            "公主殿下在可真是帮大忙了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x105,
        (
            "#045F#6P太好了……\x02\x03",

            "#048F谢谢你们。\x01",
            "艾丝蒂尔，雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6E6")

    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #521
        0x101,
        (
            "#1017F#5P嘿嘿，怎么说都是\x01",
            "是红骑士和苍骑士的关系嘛。\x02\x03",

            "齐心协力，去寻找\x01",
            "失踪的公主吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x105,
        (
            "#542F#6P啊……\x02\x03",

            "#041F好，说得对呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0x104,
        (
            "#035F呼，那我就是\x01",
            "打算强行夺走黑发公主的\x01",
            "邻国王子……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #524
        0x101,
        "#1005F#5P不要随便增加角色！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0x8,
        (
            "#651F#5P啊哈哈……\x01",
            "你们意见相符就好了。\x02\x03",

            "#650F不过这样的话，\x01",
            "我就把两人当作『协力人员』\x01",
            "来处理比较好吧。\x02\x03",

            "这样，协会在经费方面\x01",
            "也好计算了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 400)

    def lambda_A872():
        TurnDirection(0xF7, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A872)

    def lambda_A880():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A880)

    ChrTalk(    #526
        0x105,
        "#040F#6P好的，那么就拜托您了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x104,
        (
            "#031F我会诚心诚意，满怀爱心地\x01",
            "来协力你们的。\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x3F3, 1)
    OP_3F(0x3F4, 1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_AD(0x2400AE, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1241)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x123), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A974")
    ShowSaveMenu()

    label("loc_A974")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_20(0xBB8)
    OP_AE(0xC8)
    Sleep(2000)
    OP_21()
    OP_A3(0x1241)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("ED6_DT21/T2105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_959C end

    def Function_25_A9AD(): pass

    label("Function_25_A9AD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9C4")
    Call(0, 35)
    Call(0, 36)

    label("loc_A9C4")

    OP_4A(0x8, 255)
    OP_6D(-5760, 0, 45080, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2200, 0)
    OP_6C(315000, 0)
    OP_6E(327, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x8, 135, 400)

    ChrTalk(    #528
        0x8,
        "#650F#5P呀，有什么困扰的事吗──\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #529
        0x8,
        "#653F#5P咦……！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -550, 0, 39990, 315)
    SetChrPos(0x102, 80, 0, 40550, 315)
    SetChrPos(0xF8, 180, 0, 39140, 315)
    SetChrPos(0xF9, 840, 0, 39800, 315)

    def lambda_AAC4():
        OP_6D(-5300, 0, 46380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AAC4)

    def lambda_AADC():
        OP_67(0, 5620, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_AADC)

    def lambda_AAF4():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AAF4)

    def lambda_AB04():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_AB04)

    def lambda_AB14():

        label("loc_AB14")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_AB14")

    QueueWorkItem2(0x8, 2, lambda_AB14)
    OP_43(0x102, 0x1, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x1D)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x1C)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_44(0x8, 0x2)

    ChrTalk(    #530
        0x101,
        "#1006F#6P你好，嘉恩哥哥。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x102,
        "#1035F……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x8,
        (
            "#653F#5P艾丝蒂尔……\x01",
            "还有约修亚……！\x02\x03",

            "#656F是吗……\x01",
            "大家都平安无事就好。\x02\x03",

            "你们去『塔』的时候\x01",
            "发生了那个现象，\x01",
            "真是令人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "让你担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC92")

    ChrTalk(    #534
        0x103,
        (
            "#021F我们这里还好呢。\x02\x03",

            "#524F但是卢安这边\x01",
            "似乎状况相当严峻呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACD7")

    label("loc_AC92")


    ChrTalk(    #535
        0x102,
        (
            "#1040F我们这里还算好。\x02\x03",

            "#1043F但是卢安地区的\x01",
            "状况好像很严峻呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACD7")


    ChrTalk(    #536
        0x8,
        (
            "#654F#5P啊啊……\x01",
            "真是相当混乱的时候啊。\x02\x03",

            "那个贝壳样的巨大物体\x01",
            "一在湖上面出现，\x01",
            "全部的导力器就不能动了。\x02\x03",

            "#652F就算是新市长诺曼，\x01",
            "终究也是难以应付啊。\x02\x03",

            "说实话，要是没有渡鸦帮成员\x01",
            "和七耀教会的人的话，\x01",
            "市内必然已经陷入恐慌了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE60")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇知道渡鸦帮改邪归正的事】\x01",        # 0
            "【◇不知道渡鸦帮改邪归正的事】\x01",      # 1
            "【◇不变更】\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AE54"),
        (1, "loc_AE5A"),
        (SWITCH_DEFAULT, "loc_AE60"),
    )


    label("loc_AE54")

    OP_A2(0x2080)
    Jump("loc_AE60")

    label("loc_AE5A")

    OP_A3(0x2080)
    Jump("loc_AE60")

    label("loc_AE60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 0)), scpexpr(EXPR_END)), "loc_AF13")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AED8")

    ChrTalk(    #537
        0x101,
        (
            "#1008F#6P是吗……\x02\x03",

            "渡鸦帮的成员\x01",
            "似乎真的很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0x106,
        (
            "#051F嘿……\x01",
            "稍微对他们有点改观了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF10")

    label("loc_AED8")


    ChrTalk(    #539
        0x101,
        (
            "#1008F#6P是吗……\x02\x03",

            "渡鸦帮的成员\x01",
            "似乎真的很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF10")

    Jump("loc_B084")

    label("loc_AF13")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF61")

    ChrTalk(    #540
        0x101,
        "#1019F#6P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0x106,
        (
            "#055F渡鸦帮的人～？\x01",
            "……你说什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF93")

    label("loc_AF61")


    ChrTalk(    #542
        0x101,
        (
            "#1004F#6P咦……\x02\x03",

            "#1015F渡鸦帮的成员\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF93")


    ChrTalk(    #543
        0x8,
        (
            "#650F#5P导力停止现象发生之后，\x01",
            "快要发生恐慌的时候\x01",
            "是他们带头帮忙阻止了混乱。\x02\x03",

            "#651F现在也举全帮之力\x01",
            "协助协会呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2080)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B05C")

    ChrTalk(    #544
        0x106,
        "#555F真的假的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0x101,
        (
            "#1006F#6P是吗……\x01",
            "终于有干劲了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B084")

    label("loc_B05C")


    ChrTalk(    #546
        0x101,
        (
            "#1006F#6P是吗……\x01",
            "终于有干劲了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B084")


    ChrTalk(    #547
        0x8,
        (
            "#654F#5P还有一件更麻烦的事。\x02\x03",

            "#652F真是巧合，偏偏\x01",
            "是在吊桥抬起的时候\x01",
            "发生了那个非常事件……\x02\x03",

            "结果现在只能靠手划的小船\x01",
            "在街区间往返了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1DA")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇从南街区来的】\x01",                 # 0
            "【◇从北街区来的&看到了小船】\x01",      # 1
            "【◇从北街区来的&没看到小船】\x01",      # 2
            "【◇不变更】\x01",                       # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B1BF"),
        (1, "loc_B1C8"),
        (2, "loc_B1D1"),
        (SWITCH_DEFAULT, "loc_B1DA"),
    )


    label("loc_B1BF")

    OP_A2(0x2035)
    OP_A2(0x2036)
    Jump("loc_B1DA")

    label("loc_B1C8")

    OP_A2(0x2035)
    OP_A3(0x2036)
    Jump("loc_B1DA")

    label("loc_B1D1")

    OP_A3(0x2035)
    OP_A3(0x2036)
    Jump("loc_B1DA")

    label("loc_B1DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_END)), "loc_B237")

    ChrTalk(    #548
        0x101,
        (
            "#1015F#6P嗯，我们\x01",
            "也是乘那个过来这边的……\x02\x03",

            "#1007F等待的时间\x01",
            "可真是够长的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2BB")

    label("loc_B237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 5)), scpexpr(EXPR_END)), "loc_B285")

    ChrTalk(    #549
        0x101,
        (
            "#1015F#6P嗯，来这里之前\x01",
            "看到了小船的渡口……\x02\x03",

            "好像要等很久呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B2BB")

    label("loc_B285")


    ChrTalk(    #550
        0x101,
        (
            "#1015F#6P这样啊……\x01",
            "的确没有除此以外的方法了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2BB")


    ChrTalk(    #551
        0x8,
        (
            "#652F#5P不过，总不能\x01",
            "一直保持这样吧。\x02\x03",

            "很想和各地的支部以及王国军配合\x01",
            "确定相应的对策……\x02\x03",

            "#654F但通信器也不能用，\x01",
            "联络无法进行了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0x101,
        (
            "#1006F#6P放心吧，嘉恩哥哥！\x02\x03",

            "我们带好东西\x01",
            "来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #553
        0x8,
        "#653F#5P好东西……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0x102,
        "#1040F是的，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #555
        (
            "\x07\x05艾丝蒂尔等人向嘉恩说明了\x01",
            "『浮游都市』出现的缘由，以及\x01",
            "关于『零力场发生器』的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #556
        0x8,
        (
            "#652F#5P是吗……\x01",
            "那个巨大的物体\x01",
            "果然是『结社』干的好事啊。\x02\x03",

            "#650F不过，通信器能够使用\x01",
            "可真是帮大忙了！\x02\x03",

            "#651F赶快进行设置吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B5CC")

    ChrTalk(    #557
        0x107,
        "#560F好，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 3)
    SetChrPos(0x107, -6250, 0, 46860, 270)
    TurnDirection(0x8, 0x107, 0)
    TurnDirection(0x101, 0x107, 0)
    TurnDirection(0x102, 0x107, 0)
    TurnDirection(0xF8, 0x107, 0)
    TurnDirection(0xF9, 0x107, 0)
    OP_6D(-6670, 0, 46850, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(315000, 0)
    OP_6E(321, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #558
        0x107,
        "#061F……嗯，这样就行了吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #559
        "\x07\x05提妲打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_B6DE")

    label("loc_B5CC")


    ChrTalk(    #560
        0x102,
        "#1040F好的，那么……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 3)
    SetChrPos(0x102, -6250, 0, 46860, 270)
    TurnDirection(0x8, 0x102, 0)
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0xF8, 0x102, 0)
    TurnDirection(0xF9, 0x102, 0)
    OP_6D(-6670, 0, 46850, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(315000, 0)
    OP_6E(321, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #561
        0x102,
        "#1035F……这样就设置完毕了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #562
        "\x07\x05约修亚打开了通讯器的开关。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_B6DE")

    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #563
        0x8,
        "#653F#6P喔喔～！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7E0")
    OP_8C(0x107, 180, 400)

    ChrTalk(    #564
        0x107,
        (
            "#560F#2P这下这个通信器\x01",
            "应该能够使用了。\x02\x03",

            "不过，如果对方的通讯器没修好\x01",
            "还是不能发送的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B846")

    label("loc_B7E0")

    OP_8C(0x102, 180, 400)

    ChrTalk(    #565
        0x102,
        (
            "#1040F#2P这下通信器\x01",
            "能够使用了。\x02\x03",

            "但这必须是在对方的通讯器\x01",
            "也已经修好，可以使用的前提下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B846")


    ChrTalk(    #566
        0x8,
        (
            "#656F#6P呀～话说回来真是帮大忙了！\x02\x03",

            "这个状况下，能恢复联络\x01",
            "真是太好了！\x02\x03",

            "#651F真想给拉赛尔博士和你们\x01",
            "感谢之吻啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B927")
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #567
        0x107,
        "#067F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #568
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "心领了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B950")

    label("loc_B927")

    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #569
        0x101,
        (
            "#1016F#6P啊哈哈……\x01",
            "心领了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B9EE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇恢复全部的通讯器】\x01",        # 0
            "【◇只恢复这里的通讯器】\x01",      # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B9DC"),
        (1, "loc_B9E5"),
        (SWITCH_DEFAULT, "loc_B9EE"),
    )


    label("loc_B9DC")

    OP_A2(0x2003)
    OP_A2(0x2005)
    Jump("loc_B9EE")

    label("loc_B9E5")

    OP_A3(0x2003)
    OP_A3(0x2005)
    Jump("loc_B9EE")

    label("loc_B9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD1B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA95")
    TurnDirection(0x108, 0x8, 400)

    def lambda_BA14():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA14)
    Sleep(100)

    def lambda_BA27():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BA27)

    ChrTalk(    #570
        0x108,
        (
            "#070F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，配合各地的状况\x01",
            "进行执行任务的报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBCA")

    label("loc_BA95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB31")
    TurnDirection(0x103, 0x8, 400)

    def lambda_BAB0():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BAB0)
    Sleep(100)

    def lambda_BAC3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAC3)

    ChrTalk(    #571
        0x103,
        (
            "#020F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，结合各地的状况\x01",
            "一起进行任务的报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BBCA")

    label("loc_BB31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBCA")
    TurnDirection(0x106, 0x8, 400)

    def lambda_BB4C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BB4C)
    Sleep(100)

    def lambda_BB5F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BB5F)

    ChrTalk(    #572
        0x106,
        (
            "#051F好了，这下子\x01",
            "地方支部所有的通讯器都修好了。\x02\x03",

            "那么，结合各地的状况\x01",
            "一起进行任务的报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBCA")

    OP_59()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC39")
    OP_8C(0x8, 90, 400)

    ChrTalk(    #573
        0x8,
        (
            "#651F#5P呀～真是辛苦了。\x02\x03",

            "这下终于\x01",
            "可以迅速应对了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC7B")

    label("loc_BC39")

    OP_8C(0x8, 90, 400)

    ChrTalk(    #574
        0x8,
        (
            "#651F#5P各位，真是辛苦了。\x02\x03",

            "这下终于\x01",
            "可以迅速应对了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCB1")

    ChrTalk(    #575
        0x108,
        "#070F还有其它什么事要帮忙的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD18")

    label("loc_BCB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCEB")

    ChrTalk(    #576
        0x103,
        "#020F是否还有其它什么事要帮忙的吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD18")

    label("loc_BCEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD18")

    ChrTalk(    #577
        0x106,
        "#051F还有什么要帮忙的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_BD18")

    Jump("loc_BED3")

    label("loc_BD1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDAE")
    TurnDirection(0x108, 0x8, 400)

    def lambda_BD36():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BD36)
    Sleep(100)

    def lambda_BD49():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BD49)

    ChrTalk(    #578
        0x108,
        (
            "#070F#4P嗯，准备继续去把\x01",
            "其它协会的通讯器也修好，\x01",
            "不过……\x02\x03",

            "这边还有什么要帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BED3")

    label("loc_BDAE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE41")
    TurnDirection(0x103, 0x8, 400)

    def lambda_BDC9():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BDC9)
    Sleep(100)

    def lambda_BDDC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BDDC)

    ChrTalk(    #579
        0x103,
        (
            "#020F#4P嗯，准备继续去把\x01",
            "其它协会的通讯器也修好，\x01",
            "不过……\x02\x03",

            "这边还有要帮忙的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BED3")

    label("loc_BE41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BED3")
    TurnDirection(0x106, 0x8, 400)

    def lambda_BE5C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE5C)
    Sleep(100)

    def lambda_BE6F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE6F)

    ChrTalk(    #580
        0x106,
        (
            "#051F#4P嗯，准备继续去把\x01",
            "其它协会的通讯器也修好，\x01",
            "不过……\x02\x03",

            "这边没有要帮忙的事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BED3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF7B")
    OP_8C(0x8, 90, 400)

    ChrTalk(    #581
        0x8,
        (
            "#655F#5P这个嘛……\x02\x03",

            "#650F有空的话请\x01",
            "检查一下留言板上的工作吧。\x02\x03",

            "另外，可以的话，请去确认一下\x01",
            "卢安近郊中有市民居住的场所，\x01",
            "那就帮了大忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C016")

    label("loc_BF7B")

    OP_8C(0x8, 90, 400)

    ChrTalk(    #582
        0x8,
        (
            "#655F#5P这个嘛……\x02\x03",

            "#650F有空的话请\x01",
            "检查一下留言板上的工作吧。\x02\x03",

            "另外，可以的话，请去确认一下\x01",
            "卢安近郊中有市民居住的场所，\x01",
            "那就算是帮了大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C016")


    ChrTalk(    #583
        0x101,
        (
            "#1015F#6P的确，在这种状况下\x01",
            "也有必要进行巡逻的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #584
        0x102,
        (
            "#1040F尽量小心地\x01",
            "四处转转吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0x8,
        "#651F#5P啊啊，拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #586
        (
            "\x07\x05※因为通讯器已经修好了，可以呼叫在其他支部待命的同伴，\x01",
            "  将他们召集来卢安支部。\x01",
            "　想呼叫的时候请在接待处选择『呼叫同伴』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_4B(0x8, 255)
    OP_A2(0x2001)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C13C")
    OP_A2(0x2091)
    Jump("loc_C13F")

    label("loc_C13C")

    OP_A3(0x2091)

    label("loc_C13F")

    OP_28(0x9B, 0x2, 0x4)
    OP_28(0x9B, 0x1, 0x8)
    OP_6D(-2150, 0, 43020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2150, 0, 43020, 135)
    SetChrPos(0x1, -2150, 0, 43020, 135)
    SetChrPos(0x2, -2150, 0, 43020, 135)
    SetChrPos(0x3, -2150, 0, 43020, 135)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_25_A9AD end

    def Function_26_C1DD(): pass

    label("Function_26_C1DD")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xACA8, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_26_C1DD end

    def Function_27_C1F9(): pass

    label("Function_27_C1F9")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xB0F4, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_27_C1F9 end

    def Function_28_C215(): pass

    label("Function_28_C215")

    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0xACA8, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_28_C215 end

    def Function_29_C231(): pass

    label("Function_29_C231")

    OP_8E(0xFE, 0xFFFFF876, 0x0, 0xAA8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF6A0, 0x0, 0xB0F4, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_C231 end

    def Function_30_C261(): pass

    label("Function_30_C261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C27B")
    Return()

    label("loc_C27B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C29B")
    Call(0, 35)
    Call(0, 36)
    FadeToBright(0, 0)

    label("loc_C29B")

    OP_22(0xC3, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)

    ChrTalk(    #587
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_C319():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C319)

    def lambda_C327():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_C327)
    Sleep(100)

    def lambda_C33A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C33A)
    OP_8C(0x3, 315, 400)

    ChrTalk(    #588
        0x8,
        (
            "#653F#6P喔，这么快就\x01",
            "来联络了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-6390, 0, 46350, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(315000, 0)
    OP_6E(313, 0)
    SetChrPos(0x101, -550, 0, 39990, 315)
    SetChrPos(0x102, 80, 0, 40550, 315)
    SetChrPos(0xF8, 180, 0, 39140, 315)
    SetChrPos(0xF9, 840, 0, 39800, 315)
    OP_8E(0x8, 0xFFFFE796, 0x0, 0xB70C, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(700)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -6670, 1900, 46840, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_43(0x102, 0x1, 0x0, 0x1B)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x1D)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x1C)

    ChrTalk(    #589
        0x8,
        (
            "#652F#4P是，这里是游击士协会\x01",
            "卢安支部……\x02\x03",

            "#650F……啊啊，是你啊！\x02\x03",

            "#651F呀～这边也\x01",
            "正想联络你呢。\x02\x03",

            "啊，就在刚才\x01",
            "通信器修好了。\x02\x03",

            "#653F……艾丝蒂尔他们吗？\x01",
            "他们现在就在这里。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    def lambda_C54E():
        OP_6D(-5690, 0, 46380, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C54E)

    def lambda_C566():
        OP_67(0, 6020, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C566)
    OP_6E(330, 1200)

    ChrTalk(    #590
        0x101,
        "#1004F#6P（找我们的……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #591
        0x102,
        "#1044F（好像有话要说呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0x8,
        (
            "#652F#4P……嗯……嗯。\x02\x03",

            "……………………………………\x02\x03",

            "#650F啊啊，明白了。\x01",
            "我会转达给他们的。\x02\x03",

            "关于这边的状况\x01",
            "整理好了再联络。\x02\x03",

            "#651F……啊啊，彼此都加油吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6A7")

    ChrTalk(    #593
        0x106,
        (
            "#052F#4P嘉恩。\x01",
            "是哪里来的联络？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C6D1")

    label("loc_C6A7")


    ChrTalk(    #594
        0x101,
        (
            "#1015F#6P嘉恩哥哥。\x01",
            "是哪里来的联络？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6D1")

    OP_8E(0x8, 0xFFFFE9BC, 0x0, 0xB02C, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #595
        0x8,
        (
            "#650F#5P是王都支部的艾南。\x02\x03",

            "好像是女王陛下\x01",
            "有话要对你们说。\x02\x03",

            "让我转告你们，等到\x01",
            "路过格兰赛尔时，\x01",
            "能不能来王城一趟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #596
        0x101,
        "#1004F#6P女王陛下！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C7C2")

    ChrTalk(    #597
        0x106,
        (
            "#052F#4P这真令人吃惊……\x01",
            "到底有什么事呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C849")

    label("loc_C7C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C808")

    ChrTalk(    #598
        0x103,
        (
            "#023F#4P这真令人吃惊呢……\x01",
            "究竟有什么事情呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C849")

    label("loc_C808")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C849")

    ChrTalk(    #599
        0x108,
        (
            "#073F#4P这真令人吃惊啊。\x01",
            "究竟有什么事情呢～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C8A2")

    ChrTalk(    #600
        0x8,
        (
            "#656F#5P虽然没仔细问……\x02\x03",

            "但好像是通信\x01",
            "难以传达的事呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C8ED")

    label("loc_C8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C8ED")

    ChrTalk(    #601
        0x8,
        (
            "#656F#5P虽然没仔细问……\x02\x03",

            "但好像是通信\x01",
            "难以传达的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C8ED")


    ChrTalk(    #602
        0x101,
        (
            "#1015F#6P不能在通讯中传达……\x02\x03",

            "#1026F是吗，导力通讯\x01",
            "存在被人监听的危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0x102,
        (
            "#1042F看来是有什么\x01",
            "比较机密的话要说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #604
        0x8,
        (
            "#650F#5P不过，好像没说一定\x01",
            "要马上过去。\x02\x03",

            "就等路过王都的时候，\x01",
            "顺便过去就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0x101,
        "#1006F#6P这样啊……知道了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA0E")

    ChrTalk(    #606
        0x106,
        "#051F#4P有空就去一趟吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CA2C")

    label("loc_CA0E")


    ChrTalk(    #607
        0x102,
        "#1040F有空就去一趟看看。\x02",
    )

    CloseMessageWindow()

    label("loc_CA2C")

    OP_A2(0x2002)
    OP_28(0x9B, 0x1, 0x200)
    OP_28(0x9B, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_44(0x101, 0x2)
    OP_44(0x102, 0x2)
    OP_44(0xF8, 0x2)
    OP_44(0xF9, 0x2)
    OP_6D(-2150, 0, 43020, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2150, 0, 43020, 135)
    SetChrPos(0x1, -2150, 0, 43020, 135)
    SetChrPos(0x2, -2150, 0, 43020, 135)
    SetChrPos(0x3, -2150, 0, 43020, 135)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_30_C261 end

    def Function_31_CAF3(): pass

    label("Function_31_CAF3")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xAE2E, 0x7D0, 0x0)

    def lambda_CB0D():

        label("loc_CB0D")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_CB0D")

    QueueWorkItem2(0xFE, 2, lambda_CB0D)
    Return()

    # Function_31_CAF3 end

    def Function_32_CB19(): pass

    label("Function_32_CB19")

    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xB0FE, 0x7D0, 0x0)

    def lambda_CB33():

        label("loc_CB33")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_CB33")

    QueueWorkItem2(0xFE, 2, lambda_CB33)
    Return()

    # Function_32_CB19 end

    def Function_33_CB3F(): pass

    label("Function_33_CB3F")

    OP_8E(0xFE, 0xFFFFF222, 0x0, 0xAB36, 0x7D0, 0x0)

    def lambda_CB59():

        label("loc_CB59")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_CB59")

    QueueWorkItem2(0xFE, 2, lambda_CB59)
    Return()

    # Function_33_CB3F end

    def Function_34_CB65(): pass

    label("Function_34_CB65")

    OP_8E(0xFE, 0xFFFFF876, 0x0, 0xAA8C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF4DE, 0x0, 0xB3D8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF22C, 0x0, 0xB3E2, 0x7D0, 0x0)

    def lambda_CBA7():

        label("loc_CBA7")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_CBA7")

    QueueWorkItem2(0xFE, 2, lambda_CBA7)
    Return()

    # Function_34_CB65 end

    def Function_35_CBB3(): pass

    label("Function_35_CBB3")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CC2D"),
        (1, "loc_CC33"),
        (SWITCH_DEFAULT, "loc_CC39"),
    )


    label("loc_CC2D")

    OP_A2(0x1200)
    Jump("loc_CC39")

    label("loc_CC33")

    OP_A2(0x1201)
    Jump("loc_CC39")

    label("loc_CC39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CC47")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_CC4B")

    label("loc_CC47")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_CC4B")

    Return()

    # Function_35_CBB3 end

    def Function_36_CC4C(): pass

    label("Function_36_CC4C")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_36_CC4C end

    SaveToFile()

Try(main)
