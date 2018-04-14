from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1210   ._SN',
        MapName             = 'Bose',
        Location            = 'T1210.x',
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
        '阿加特',                               # 9
        '提妲',                                 # 10
        '莱森村长',                             # 11
        '摩尔根将军',                           # 12
        '王国军士官',                           # 13
        '奥兰橘婆婆',                           # 14
        '梅洛涅',                               # 15
        '碧尔奈婆婆',                           # 16
        '巴德斯',                               # 17
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
        'ED6_DT26/CH20365 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH02080 ._CH',             # 03
        'ED6_DT07/CH01600 ._CH',             # 04
        'ED6_DT27/CH03003 ._CH',             # 05
        'ED6_DT07/CH00023 ._CH',             # 06
        'ED6_DT07/CH00033 ._CH',             # 07
        'ED6_DT07/CH00043 ._CH',             # 08
        'ED6_DT07/CH00073 ._CH',             # 09
        'ED6_DT07/CH01493 ._CH',             # 0A
        'ED6_DT07/CH02083 ._CH',             # 0B
        'ED6_DT07/CH01010 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01180 ._CH',             # 0E
        'ED6_DT26/CH20365 ._CH',             # 0F
        'ED6_DT07/CH01060 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT26/CH20365P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH02080P._CP',             # 03
        'ED6_DT07/CH01600P._CP',             # 04
        'ED6_DT27/CH03003P._CP',             # 05
        'ED6_DT07/CH00023P._CP',             # 06
        'ED6_DT07/CH00033P._CP',             # 07
        'ED6_DT07/CH00043P._CP',             # 08
        'ED6_DT07/CH00073P._CP',             # 09
        'ED6_DT07/CH01493P._CP',             # 0A
        'ED6_DT07/CH02083P._CP',             # 0B
        'ED6_DT07/CH01010P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01180P._CP',             # 0E
        'ED6_DT26/CH20365P._CP',             # 0F
        'ED6_DT07/CH01060P._CP',             # 10
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
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
        X                   = -25500,
        Z                   = 0,
        Y                   = 5060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -3080,
        Z                   = 0,
        Y                   = 3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 5920,
        Z                   = 0,
        Y                   = 49500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -25900,
        Z                   = 0,
        Y                   = 8660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -26120,
        TriggerZ            = 0,
        TriggerY            = 47750,
        TriggerRange        = 1000,
        ActorX              = -26120,
        ActorZ              = 1000,
        ActorY              = 47750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_276",          # 00, 0
        "Function_1_3A6",          # 01, 1
        "Function_2_440",          # 02, 2
        "Function_3_5BD",          # 03, 3
        "Function_4_6A2",          # 04, 4
        "Function_5_C69",          # 05, 5
        "Function_6_11CF",         # 06, 6
        "Function_7_1736",         # 07, 7
        "Function_8_1EB5",         # 08, 8
        "Function_9_1F05",         # 09, 9
        "Function_10_3629",        # 0A, 10
        "Function_11_3699",        # 0B, 11
        "Function_12_36F7",        # 0C, 12
        "Function_13_4643",        # 0D, 13
        "Function_14_465F",        # 0E, 14
        "Function_15_468F",        # 0F, 15
        "Function_16_46AB",        # 10, 16
        "Function_17_46C7",        # 11, 17
        "Function_18_46E3",        # 12, 18
        "Function_19_47DE",        # 13, 19
    )


    def Function_0_276(): pass

    label("Function_0_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    SetChrFlags(0xF, 0x80)

    label("loc_2A0")

    Jump("loc_36B")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2F1")
    SetChrPos(0xF, 7570, 0, 46210, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    SetChrPos(0xD, -31510, 0, 2960, 197)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrFlags(0xA, 0x80)

    label("loc_2EE")

    Jump("loc_36B")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_36B")
    SetChrPos(0x8, -24200, 400, 47000, 0)
    SetChrPos(0x9, -25480, 0, 46660, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xF, 7570, 0, 46210, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xD, -31510, 0, 2960, 197)

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_381")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_3A5")

    label("loc_381")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_38D"),
        (SWITCH_DEFAULT, "loc_3A5"),
    )


    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A2")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_3A2")

    Jump("loc_3A5")

    label("loc_3A5")

    Return()

    # Function_0_276 end

    def Function_1_3A6(): pass

    label("Function_1_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3B9")
    OP_B1("T1210_n")
    Jump("loc_3D5")

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 3)), scpexpr(EXPR_END)), "loc_3CC")
    OP_B1("T1210_y")
    Jump("loc_3D5")

    label("loc_3CC")

    OP_B1("T1210_n")

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3F0")
    Jump("loc_3FE")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_3FE")
    OP_6F(0x1, 10)

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_420")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    OP_10(0xA, 0x1)
    OP_10(0xB, 0x1)
    Jump("loc_43F")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_43F")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x1)
    OP_10(0x5, 0x1)
    OP_10(0x6, 0x1)
    OP_10(0x7, 0x1)

    label("loc_43F")

    Return()

    # Function_1_3A6 end

    def Function_2_440(): pass

    label("Function_2_440")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5A7")

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5A7")

    label("loc_47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5A7")

    label("loc_497")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5A7")

    label("loc_4B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5A7")

    label("loc_4C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5A7")

    label("loc_4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FB")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5A7")

    label("loc_4FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5A7")

    label("loc_514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5A7")

    label("loc_52D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5A7")

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5A7")

    label("loc_55F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5A7")

    label("loc_578")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5A7")

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A7")

    label("loc_5BC")

    Return()

    # Function_2_440 end

    def Function_3_5BD(): pass

    label("Function_3_5BD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_61A")

    ChrTalk(    #0
        0xFE,
        (
            "以前传说中的龙\x01",
            "大部分都是很善良的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "应该没有像这次这样\x01",
            "粗暴的龙吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69E")

    label("loc_61A")


    ChrTalk(    #2
        0xFE,
        (
            "龙原来真的存在啊。\x01",
            "还以为只是传说呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "不过，以前传说中的龙\x01",
            "大部分都是很善良的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "应该没有像这次这样\x01",
            "粗暴的龙吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_69E")

    TalkEnd(0x10)
    Return()

    # Function_3_5BD end

    def Function_4_6A2(): pass

    label("Function_4_6A2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_755")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B")

    ChrTalk(    #5
        0xFE,
        (
            "话说回来导力器\x01",
            "为什么会停呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "和孩子们在眺望的\x01",
            "那个奇怪的岛一样的东西，\x01",
            "有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_752")

    label("loc_71B")


    ChrTalk(    #7
        0xFE,
        (
            "还是第一次遇到\x01",
            "导力器停止呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "是什么原因呢。\x02",
    )

    CloseMessageWindow()

    label("loc_752")

    Jump("loc_C65")

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_801")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B4")

    ChrTalk(    #9
        0xFE,
        (
            "老头子他\x01",
            "今天也去看果树园了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "导力器不能动\x01",
            "他好像也完全不在意。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7FE")

    label("loc_7B4")


    ChrTalk(    #11
        0xFE,
        (
            "老头子他\x01",
            "今天也去看果树园了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "这种时候\x01",
            "真希望他在家里帮帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE")

    Jump("loc_C65")

    label("loc_801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_85E")

    ChrTalk(    #13
        0xFE,
        (
            "老头子他\x01",
            "好像和年轻人一起工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "不知道为什么，\x01",
            "总算关系变好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AB")

    label("loc_85E")


    ChrTalk(    #15
        0xFE,
        (
            "老头子他\x01",
            "好像和年轻人一起工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "嗯，那个老顽固总算\x01",
            "接受了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8AB")

    Jump("loc_C65")

    label("loc_8AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 2)), scpexpr(EXPR_END)), "loc_8F7")

    ChrTalk(    #17
        0xFE,
        (
            "愿女神\x01",
            "保佑你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "我也会在这里\x01",
            "为你们祈祷的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A50")

    label("loc_8F7")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #19
        0xFE,
        (
            "还以为是谁呢，\x01",
            "这不是阿加特吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "你不是受了伤\x01",
            "躺在床上吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#053F啊啊，刚刚下床。\x02\x03",

            "#050F婆婆这里\x01",
            "没受到龙的伤害吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "嗯嗯，所幸没事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "这些还都\x01",
            "都是多亏了女神啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#552F女神保佑啊……\x02\x03",

            "确实这次\x01",
            "真需要她保佑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "嗯，你倒是\x01",
            "难得这么诚心嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "我会为你祈祷，\x01",
            "让女神也保佑保佑你的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4A)

    label("loc_A50")

    Jump("loc_C65")

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AF3")

    ChrTalk(    #27
        0xFE,
        (
            "在战争中房子几乎\x01",
            "都被燃烧弹烧掉了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "虽然炮击目标似乎是\x01",
            "以森林为阵地的王国军……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "……但无论是什么目的，\x01",
            "这都是惨无人道的事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B81")

    label("loc_AF3")


    ChrTalk(    #30
        0xFE,
        (
            "在战争中房子几乎\x01",
            "都被燃烧弹烧掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "特别是阿加特家那边，\x01",
            "几乎被烧得一干二净……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "实在是太惨了，\x01",
            "所以大家一起帮忙重建了房子。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B81")

    Jump("loc_C65")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BDF")

    ChrTalk(    #33
        0xFE,
        (
            "真是的……\x01",
            "巴德斯去哪儿了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "再三叮嘱他\x01",
            "外面太危险不要出去……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C65")

    label("loc_BDF")


    ChrTalk(    #35
        0xFE,
        (
            "真是的……\x01",
            "巴德斯去哪儿了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "再三叮嘱他\x01",
            "外面太危险不要出去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "唉，不愧是爷爷和孙子啊。\x01",
            "不听劝告这点真是一模一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C65")

    TalkEnd(0xD)
    Return()

    # Function_4_6A2 end

    def Function_5_C69(): pass

    label("Function_5_C69")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFC")

    ChrTalk(    #38
        0xFE,
        (
            "城里似乎飞船和搬运车\x01",
            "都动不了了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "现在村子倒还\x01",
            "没什么问题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "如果这情况继续下去，\x01",
            "不知道会变成怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_D4E")

    label("loc_CFC")


    ChrTalk(    #41
        0xFE,
        (
            "城里似乎飞船和搬运车\x01",
            "都动不了了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "……考虑到将后的事\x01",
            "真觉得有些不安。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4E")

    Jump("loc_11CB")

    label("loc_D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEE")

    ChrTalk(    #43
        0xFE,
        (
            "本以为果树园的事告一段落了，\x01",
            "但怎么导力器又出问题了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "……真是屋漏偏逢连夜雨啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "唉，什么时候\x01",
            "才能安安稳稳过日子啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E4D")

    label("loc_DEE")


    ChrTalk(    #46
        0xFE,
        (
            "本以为果树园的事告一段落了，\x01",
            "但怎么导力器又出问题了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "……真是屋漏偏逢连夜雨啊。\x02",
    )

    CloseMessageWindow()

    label("loc_E4D")

    Jump("loc_11CB")

    label("loc_E50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_F5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(    #48
        0xFE,
        (
            "我老公他们在很努力\x01",
            "的种植新树苗呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "对我们夫妇来说\x01",
            "这也是新的起点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F5A")

    label("loc_EAF")


    ChrTalk(    #50
        0xFE,
        (
            "我老公他们在很努力\x01",
            "的种植新树苗呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "最近一周，\x01",
            "每天都在不安中度过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "靠大家的捐款，\x01",
            "当前的生活应该能撑过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "唉，总算松了口气……\x01",
            "现在真是这感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F5A")

    Jump("loc_11CB")

    label("loc_F5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1036")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_FC2")

    ChrTalk(    #54
        0xFE,
        (
            "果树园的事\x01",
            "好像谈妥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "不知是不是我多心，老公的表情\x01",
            "好像变得明朗了许多。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1033")

    label("loc_FC2")


    ChrTalk(    #56
        0xFE,
        (
            "果树园的事\x01",
            "好像谈妥了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "不知是不是我多心，老公的表情\x01",
            "好像变得明朗了许多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "是不是有什么好事呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1033")

    Jump("loc_11CB")

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1096")

    ChrTalk(    #59
        0xFE,
        (
            "老公还没从果树园\x01",
            "回来呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "他是个很认真的人，\x01",
            "但希望不要太钻牛角尖就好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CB")

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_11CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10F9")

    ChrTalk(    #61
        0xFE,
        (
            "我老公贝斯卡对果树栽培的\x01",
            "研究可是满腔热情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "但是……\x01",
            "却发生这种事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11CB")

    label("loc_10F9")


    ChrTalk(    #63
        0xFE,
        (
            "我老公贝斯卡对果树栽培的\x01",
            "研究可是满腔热情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "一边购买种植用机械，\x01",
            "一边又选择树木的品种……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "为了果园的发展\x01",
            "花尽了心血呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "唉，尽管如此……\x01",
            "却发生这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "……该怎么\x01",
            "安慰他才好呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11CB")

    TalkEnd(0xE)
    Return()

    # Function_5_C69 end

    def Function_6_11CF(): pass

    label("Function_6_11CF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1239")

    ChrTalk(    #68
        0xFE,
        (
            "每次发生什么事件\x01",
            "就会联想到帝国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "虽说是１０年前的事\x01",
            "但实在是令人悲哀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1260")

    label("loc_1239")


    ChrTalk(    #70
        0xFE,
        (
            "每次发生什么事件\x01",
            "就会联想到帝国。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1260")

    Jump("loc_1732")

    label("loc_1263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_137F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_12DB")

    ChrTalk(    #71
        0xFE,
        (
            "终于恢复到\x01",
            "平常的生活中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "我家的人也好久没\x01",
            "去扫墓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "一定有许多\x01",
            "想对故人报告的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137C")

    label("loc_12DB")


    ChrTalk(    #74
        0xFE,
        (
            "终于恢复到\x01",
            "平常的生活中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "重建果树园\x01",
            "应该要花不少时间……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "但全村人齐心合力的话，\x01",
            "一定能克服困难的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "就像度过\x01",
            "百日战役后的混乱时期一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_137C")

    Jump("loc_1732")

    label("loc_137F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_150A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 4)), scpexpr(EXPR_END)), "loc_13D4")

    ChrTalk(    #78
        0xFE,
        (
            "今后似乎\x01",
            "还会有很多很多困难的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "你们也请\x01",
            "多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1507")

    label("loc_13D4")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #80
        0xFE,
        "啊，阿加特。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "太好了……\x01",
            "看来恢复精神了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x106,
        (
            "#053F啊啊，抱歉。\x01",
            "还让婆婆也担心了。\x02\x03",

            "#051F不过，已经没事了。\x02\x03",

            "#051F虽然不算完全恢复，\x01",
            "不过马上开始工作是没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "是吗，那就好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "今后似乎\x01",
            "还会有很多很多困难的工作呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "所以无论如何\x01",
            "自己要多多保重。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4C)

    label("loc_1507")

    Jump("loc_1732")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1659")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_157F")

    ChrTalk(    #86
        0xFE,
        (
            "米夏有着可爱的笑容，\x01",
            "是个为哥哥着想的好妹妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "从那以后就过了１０年啊……\x01",
            "时间过得真快啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1656")

    label("loc_157F")


    ChrTalk(    #88
        0xFE,
        (
            "米夏有着可爱的笑容，\x01",
            "是个为哥哥着想的好妹妹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "不过，也有像哥哥一样\x01",
            "坚强的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "是一个一旦决定的事\x01",
            "就一定会贯彻到底的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "如果她没事，现在应该\x01",
            "在果园独当一面了吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "我这样想过呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1656")

    Jump("loc_1732")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_16B8")

    ChrTalk(    #93
        0xFE,
        (
            "孩子们的哭叫，\x01",
            "树木燃烧的气味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "……让人联想起\x01",
            "１０年前的战争啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1732")

    label("loc_16B8")


    ChrTalk(    #95
        0xFE,
        (
            "孩子们的哭叫，\x01",
            "树木燃烧的气味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "……让人联想起\x01",
            "１０年前的战争啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "那时候也是，一瞬间\x01",
            "失去了所有东西。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1732")

    TalkEnd(0xF)
    Return()

    # Function_6_11CF end

    def Function_7_1736(): pass

    label("Function_7_1736")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D5")

    ChrTalk(    #98
        0xFE,
        "噢，是阿加特和大家啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "难不成是来\x01",
            "看看村子的情况的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#051F嗯，差不多吧。\x02\x03",

            "看起来好像\x01",
            "没什么特别的……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_1842")

    label("loc_17D5")


    ChrTalk(    #101
        0xFE,
        "噢，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1000F你好，村长先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#1041F前阵子承蒙照顾了。\x02\x03",

            "……村子的情况怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    label("loc_1842")


    ChrTalk(    #104
        0xFE,
        "呼，现在还很平静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "原本我们村子\x01",
            "就没太多的导力机械嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "这回倒是多亏这个了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1011F啊，原来如此……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18F6")

    ChrTalk(    #108
        0x108,
        (
            "#070F的确，城市那边\x01",
            "比村子这混乱多了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1971")

    label("loc_18F6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1935")

    ChrTalk(    #109
        0x103,
        (
            "#020F的确，城市那边\x01",
            "比村子这混乱多了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1971")

    label("loc_1935")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1971")

    ChrTalk(    #110
        0x106,
        (
            "#050F的确，城市那边\x01",
            "比村子这混乱多了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1971")


    ChrTalk(    #111
        0x102,
        (
            "#1043F可以使平常生活变得便利，\x01",
            "但是失去之后完全不知所措……\x02\x03",

            "……算是导力文明的利弊吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #112
        0xFE,
        "水能载舟亦能覆舟。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "任何技术\x01",
            "都隐藏着危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "其实问题还是出在\x01",
            "我们自己身上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x2093)
    Jump("loc_1BDD")

    label("loc_1A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1BA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A84")

    ChrTalk(    #115
        0xFE,
        "现在村子还很平静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "多亏了没有大力\x01",
            "推进导力化。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA1")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2A")

    ChrTalk(    #117
        0xFE,
        (
            "导力器不能使用\x01",
            "对王国军来说是很严重的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "虽说缔结了互不侵犯条约，\x01",
            "但在我看来\x01",
            "帝国军的动向还是很可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "唔，希望是我\x01",
            "杞人忧天吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1BA1")

    label("loc_1B2A")


    ChrTalk(    #120
        0xFE,
        (
            "导力器不能使用\x01",
            "对王国军来说是很严重的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "虽说缔结了互不侵犯条约，\x01",
            "但在我看来\x01",
            "帝国军的动向还是很可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA1")

    Jump("loc_1BDD")

    label("loc_1BA4")


    ChrTalk(    #122
        0xFE,
        "现在村子还很平静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "多亏了没有大力\x01",
            "推进导力化。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    Jump("loc_1EB1")

    label("loc_1BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 3)), scpexpr(EXPR_END)), "loc_1C39")

    ChrTalk(    #124
        0xFE,
        (
            "虽然很期待\x01",
            "你们的活跃表现……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "不过，什么事情\x01",
            "都不要太勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E67")

    label("loc_1C39")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #126
        0xFE,
        "噢，是你们啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "捕获作战那边\x01",
            "有什么进展吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1015F嗯，龙失控的原因\x01",
            "差不多知道了。\x02\x03",

            "#1006F下次作战如果顺利，\x01",
            "说不定就可以阻止它的失控。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #129
        0xFE,
        "是吗，真是好消息。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "不过，还是不能\x01",
            "太勉强哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #131
        0xFE,
        "特别是阿加特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "你要是有个三长两短\x01",
            "我可不答应啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        (
            "#552F嗯，不用担心。\x02\x03",

            "这里有个\x01",
            "监督我的小鬼呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #134
        0x107,
        "#067F啊，嘿嘿……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "唔，那就好……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "总之，什么事情\x01",
            "都要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "龙是种超过人类智慧想象的生物。\x01",
            "不知道会发生什么事哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x106,
        (
            "#053F啊啊，我会\x01",
            "牢牢记住的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4B)

    label("loc_1E67")

    Jump("loc_1EB1")

    label("loc_1E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1EB1")

    ChrTalk(    #139
        0xFE,
        (
            "阿加特的事\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "那么\x01",
            "去柏斯的路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB1")

    TalkEnd(0xA)
    Return()

    # Function_7_1736 end

    def Function_8_1EB5(): pass

    label("Function_8_1EB5")

    TalkBegin(0x9)

    ChrTalk(    #141
        0x9,
        (
            "#060F我会在这里\x01",
            "好好照顾阿加特哥哥的……\x02\x03",

            "姐姐你们\x01",
            "也一定要小心哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_8_1EB5 end

    def Function_9_1F05(): pass

    label("Function_9_1F05")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrPos(0x0, -27360, 0, 44980, 305)
    OP_6D(-27230, 0, 39560, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -24200, 400, 47000, 0)
    SetChrPos(0x9, -25480, 0, 46660, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    OP_6F(0x1, 10)
    OP_4A(0x9, 255)

    def lambda_1FAB():
        OP_6D(-24990, 0, 47100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FAB)

    def lambda_1FC3():
        OP_67(0, 6150, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FC3)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FFE")
    Call(0, 18)

    label("loc_1FFE")

    OP_6D(4120, 200, 47460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3250, 200, 45650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_207E")
    SetChrPos(0xF7, 4580, 200, 45570, 0)
    SetChrPos(0xF8, 2310, 200, 46950, 90)
    Jump("loc_20A0")

    label("loc_207E")

    SetChrPos(0xF8, 4580, 200, 45570, 0)
    SetChrPos(0xF7, 2310, 200, 46950, 90)

    label("loc_20A0")

    SetChrPos(0xB, 3300, 250, 48050, 180)
    SetChrPos(0xA, 4600, 200, 48050, 180)
    SetChrPos(0xC, 2350, 0, 48960, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0xF7, 0x40)
    SetChrFlags(0xF8, 0x40)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF7, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0xF7, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrFlags(0xF, 0x80)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_216D")
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 6)

    label("loc_216D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2185")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 7)

    label("loc_2185")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_219D")
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 8)

    label("loc_219D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B5")
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 9)

    label("loc_21B5")

    OP_4A(0xA, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #142
        0xA,
        (
            "原来如此……\x01",
            "竟然是这样的啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "艾丝蒂尔小姐，将军阁下。\x01",
            "给你们添了不少麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1003F哪里……\x02\x03",

            "结果我们还是没能\x01",
            "阻止龙的失控……\x02\x03",

            "#1007F没派上什么用场，\x01",
            "实在抱歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xB,
        (
            "#163F#5P嗯，别泄气。\x02\x03",

            "#160F无论结果如何，你们的\x01",
            "快速行动就已经帮了大忙了。\x02\x03",

            "超市的救援行动，\x01",
            "还有果树园的灭火行动等等。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1016F啊、啊哈哈……\x01",
            "将军大人这样夸奖\x01",
            "真让人愧不敢当呢。\x02\x03",

            "#1026F先不说这个……\x01",
            "关于阿加特的事。\x02\x03",

            "他妹妹米夏\x01",
            "真的在１０年前的战争中……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        "唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "帝国军和王国军的战斗\x01",
            "就发生在村子近郊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        (
            "当时，帝国军的燃烧弾\x01",
            "击中了几处民宅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        (
            "结果不但烧毁了房屋，\x01",
            "还出现了牺牲者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        "米夏就是其中之一。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1003F………………………………\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2509")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_247C")
    SetChrSubChip(0xF7, 2)
    Sleep(300)
    Jump("loc_24A1")

    label("loc_247C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2497")
    SetChrSubChip(0xF8, 2)
    Sleep(300)
    Jump("loc_24A1")

    label("loc_2497")

    SetChrSubChip(0xF8, 1)
    Sleep(300)

    label("loc_24A1")


    ChrTalk(    #153
        0x103,
        (
            "#524F其实我也知道\x01",
            "一点内情……\x02\x03",

            "但看阿加特不太想说的\x01",
            "样子就没开口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1026F原来是这样……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)

    label("loc_2509")


    ChrTalk(    #155
        0xB,
        (
            "#163F#5P……从某种意义上来说，\x01",
            "这是我们王国军的失败。\x02\x03",

            "#160F设置在村子周围的防线\x01",
            "招来了帝国军的猛烈攻击……\x02\x03",

            "结果造成了\x01",
            "巨大的损害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1026F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xB,
        (
            "#163F#5P而负责这个防线部署\x01",
            "的人正是我。\x02\x03",

            "可以说一切都是我的责任。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #158
        0xA,
        (
            "#2P……将军阁下。\x01",
            "请不必太过自责。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "#2P当时王国军只是\x01",
            "履行了使命而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        (
            "#2P结果只是几个巧合的重叠\x01",
            "造成了这悲剧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(300)

    ChrTalk(    #161
        0xB,
        (
            "#160F#5P不，请不要包庇我。\x02\x03",

            "对失去亲人的人来说\x01",
            "这种理由是行不通的。\x02\x03",

            "就像那红头发的年轻人一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        "#2P……那是……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(300)

    ChrTalk(    #163
        0xB,
        (
            "#163F#5P村里举行牺牲者的葬礼时，\x01",
            "我作为军方代表出席了……\x02\x03",

            "当时看到的那红头发少年的眼神，\x01",
            "我现在还历历在目。\x02\x03",

            "仿佛是将无尽的哀伤\x01",
            "硬生生用愤怒压制住……\x01",
            "那样令人心痛的眼神。\x02\x03",

            "#160F让他带有这种眼神……\x01",
            "一切都是我造成的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "#2P……不，\x01",
            "不是这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "#2P阿加特真正痛责的\x01",
            "不是帝国军，更不是阁下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        "#2P其实是他自己。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(300)

    ChrTalk(    #167
        0xB,
        "#161F#5P……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#1015F怎，怎么说？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(50)

    ChrTalk(    #169
        0xA,
        "我也不知道该怎么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "不过阿加特似乎认为，米夏的死\x01",
            "是自己的责任。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "虽然绝对不是这样，\x01",
            "但他就是一直认为都是自己的错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        (
            "而对于自己的强烈自责，\x01",
            "他离开了村子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xA,
        (
            "带着如何才能补偿米夏的疑问，\x01",
            "四处寻找心中的答案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        (
            "恐怕在卢安度过那些\x01",
            "颓废的日子，就是因为\x01",
            "还没有找到答案吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1003F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "之后，虽然\x01",
            "走上了游击士的道路……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "但看来，他还是\x01",
            "没有找到答案。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "和１０年前一样，\x01",
            "还被困在深深的哀伤\x01",
            "和对自己的愤怒之中吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xB,
        "#163F#5P……真令人心痛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1002F……对了，将军……\x02\x03",

            "还是让我们\x01",
            "也帮忙对付龙吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(50)

    ChrTalk(    #181
        0xB,
        "#161F#5P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1000F我们游击士\x01",
            "有军方没有的优势。\x02\x03",

            "行动迅速、\x01",
            "亲近市民等等……\x02\x03",

            "军人们平时进不去的\x01",
            "隐秘之地我们也可以深入。\x02\x03",

            "一定能派上用场的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xB,
        "#163F#5P但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#1010F我想阿加特他\x01",
            "或许就是感到\x01",
            "这方面的可能性呢。\x02\x03",

            "如何才能补偿妹妹，\x01",
            "为了找到答案而参加游击士……\x02\x03",

            "#1003F……所以，阿加特\x01",
            "会被老爸劝导成为游击士的理由，\x01",
            "现在终于理解了。\x02\x03",

            "因为老爸也是因妈妈的去世\x01",
            "才毅然决定走上游击士的道路的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xB,
        "#160F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1002F为了再一次确认\x01",
            "游击士的意义所在……\x02\x03",

            "更重要的是，为了帮助\x01",
            "眼前遇到困难的人们……\x02\x03",

            "我希望能尽现在自己\x01",
            "最大的努力。\x02\x03",

            "所以……\x01",
            "请让我们协助作战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D6F")

    ChrTalk(    #187
        0x105,
        "#542F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x103,
        "#027F呵呵，说得好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF6")

    label("loc_2D6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DC3")

    ChrTalk(    #189
        0x104,
        "#035F呼，不愧是艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x103,
        "#027F嗯嗯，说得好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF6")

    label("loc_2DC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E11")

    ChrTalk(    #191
        0x103,
        "#524F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x108,
        "#070F呵呵，说得好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF6")

    label("loc_2E11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E5D")

    ChrTalk(    #193
        0x105,
        "#542F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x104,
        "#035F呼，真厉害啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF6")

    label("loc_2E5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EAB")

    ChrTalk(    #195
        0x105,
        "#542F艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x108,
        "#070F呵呵，说得好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EF6")

    label("loc_2EAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EF6")

    ChrTalk(    #197
        0x104,
        "#035F呼，真厉害啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x108,
        "#070F啊啊，说得好。\x02",
    )

    CloseMessageWindow()

    label("loc_2EF6")


    ChrTalk(    #199
        0xB,
        (
            "#160F#5P……………………………\x02\x03",

            "#163F１０年前，如果柏斯地区\x01",
            "也有游击士，或许……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        "#1015F啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        (
            "#163F#5P不……没什么。\x02\x03",

            "#160F我代替繁忙的卡西乌斯\x01",
            "负责担任\x01",
            "这次对龙作战的指挥。\x02\x03",

            "差不多该回哈肯大门了，\x01",
            "军事会议就要开始。\x02\x03",

            "你的提案\x01",
            "到时再做讨论。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        "#1018F这，这么说……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xB,
        (
            "#163F#5P别高兴得太早。\x01",
            "单纯只是讨论而已。\x02\x03",

            "#160F今晚会把军事会议的结果\x01",
            "传达给柏斯支部。\x02\x03",

            "我能保证的就只有这些了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1006F……嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30CE")

    ChrTalk(    #205
        0x103,
        "#027F恭候您的联络。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3123")

    label("loc_30CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30FA")

    ChrTalk(    #206
        0x108,
        "#071F恭候您的联络了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3123")

    label("loc_30FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3123")

    ChrTalk(    #207
        0x104,
        "#031F恭候您的联络啦。\x02",
    )

    CloseMessageWindow()

    label("loc_3123")


    ChrTalk(    #208
        0xB,
        (
            "#160F#5P那么我\x01",
            "就此告辞了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(300)

    ChrTalk(    #209
        0xB,
        "#160F#5P村长，打扰了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #210
        0xA,
        (
            "#2P哪里哪里。\x01",
            "请再来啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrFlags(0xB, 0x1)
    SetChrPos(0xB, 2480, 0, 48000, 270)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    OP_0D()

    def lambda_31C3():
        OP_6D(1500, 0, 44410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_31C3)
    OP_43(0xB, 0x1, 0x0, 0xA)
    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0xB)
    SetChrSubChip(0x101, 1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3216")
    SetChrSubChip(0xF7, 1)
    Sleep(50)
    SetChrSubChip(0xF8, 2)
    Sleep(300)
    Jump("loc_322A")

    label("loc_3216")

    SetChrSubChip(0xF7, 2)
    Sleep(50)
    SetChrSubChip(0xF8, 1)
    Sleep(300)

    label("loc_322A")

    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_6D(4370, 0, 47120, 3000)
    WaitChrThread(0xC, 0x1)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #211
        0x101,
        (
            "#1006F好了，我们\x01",
            "差不多也该回柏斯了。\x02\x03",

            "#1015F阿加特……\x01",
            "还是不要动的好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3305")

    ChrTalk(    #212
        0x105,
        (
            "#047F他那个伤势还是静养２、３日\x01",
            "会比较好。\x02\x03",

            "#542F今晚就让他好好\x01",
            "睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C8")

    label("loc_3305")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3368")

    ChrTalk(    #213
        0x108,
        (
            "#074F他那个伤势还是静养２、３日\x01",
            "会比较好吧。\x02\x03",

            "#070F今晚就让他好好\x01",
            "睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33C8")

    label("loc_3368")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33C8")

    ChrTalk(    #214
        0x104,
        (
            "#035F他那个伤势还是静养２、３日\x01",
            "会比较好吧。\x02\x03",

            "#030F今晚就让他好好\x01",
            "睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33C8")


    ChrTalk(    #215
        0x101,
        (
            "#1006F嗯，是啊。\x02\x03",

            "那就去看看他，\x01",
            "顺便和提妲说说。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF8, 0)
    Sleep(50)
    SetChrSubChip(0xF7, 0)
    Sleep(300)

    ChrTalk(    #216
        0x101,
        (
            "#1015F……村长先生。\x02\x03",

            "这种状况下还麻烦您实在抱歉。\x01",
            "阿加特的事，就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "#5P呵呵，那家伙\x01",
            "就是我们的亲人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xA,
        (
            "#5P虽说事态比较严重，\x01",
            "但和１０年前相比还算好的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xA,
        (
            "#5P没有出现牺牲者\x01",
            "就该感谢女神了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1820, 0, 44890, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1820, 0, 44890, 225)
    SetChrPos(0x1, 1820, 0, 44890, 225)
    SetChrPos(0x2, 1820, 0, 44890, 225)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0xF8, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xF7, 0x4)
    ClearChrFlags(0xF8, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0xF7, 0x40)
    ClearChrFlags(0xF8, 0x40)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0xF7, 0x1)
    SetChrFlags(0xF8, 0x1)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 7570, 0, 46210, 90)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 2)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_A2(0x1A1A)
    OP_28(0x94, 0x1, 0x80)
    OP_28(0x94, 0x1, 0x100)
    OP_28(0x94, 0x1, 0x200)
    OP_28(0x94, 0x1, 0x400)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_1F05 end

    def Function_10_3629(): pass

    label("Function_10_3629")

    OP_8E(0xFE, 0x35C, 0x0, 0xBA9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9E3E, 0x7D0, 0x0)
    OP_4A(0xC, 255)
    SetChrSubChip(0xC, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4B(0xC, 255)

    def lambda_366E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_366E)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9542, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_3629 end

    def Function_11_3699(): pass

    label("Function_11_3699")

    OP_8E(0xFE, 0x35C, 0x0, 0xBA9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9E3E, 0x7D0, 0x0)

    def lambda_36C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36C7)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9542, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_11_3699 end

    def Function_12_36F7(): pass

    label("Function_12_36F7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_370A")
    Call(0, 18)

    label("loc_370A")

    OP_6D(-24530, 0, 47200, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -25870, -500, 37510, 0)
    SetChrPos(0xF7, -25870, -500, 37510, 0)
    SetChrPos(0xF8, -25870, -500, 37510, 0)
    OP_4A(0x9, 255)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_37B4():

        label("loc_37B4")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_37B4")

    QueueWorkItem2(0x9, 1, lambda_37B4)
    OP_22(0x6, 0x0, 0x64)

    def lambda_37CA():
        OP_6D(-25990, 0, 46100, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_37CA)

    def lambda_37E2():

        label("loc_37E2")

        TurnDirection(0x9, 0x101, 400)
        OP_48()
        Jump("loc_37E2")

    QueueWorkItem2(0x9, 1, lambda_37E2)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #220
        0x9,
        "#560F啊，姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1006F#6P提妲，辛苦了。\x02\x03",

            "阿加特的情况怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x9,
        (
            "#561F嗯……\x01",
            "好像睡得很熟。\x02\x03",

            "#066F不过，脸色变得好起来了，\x01",
            "好好休息应该没问题吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1025F#6P是吗。\x02\x03",

            "#1006F话说……\x01",
            "这里就是阿加特的家啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_394E")

    ChrTalk(    #224
        0x104,
        (
            "#031F#6P唔，狭小而温暖…\x01",
            "令人感觉很舒服呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D1")

    label("loc_394E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3990")

    ChrTalk(    #225
        0x105,
        (
            "#048F#6P狭小而温暖…\x01",
            "令人感觉很舒服的家呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39D1")

    label("loc_3990")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39D1")

    ChrTalk(    #226
        0x103,
        (
            "#021F#6P嗯～狭小而温暖…\x01",
            "令人感觉很舒服的家。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A11")

    ChrTalk(    #227
        0x108,
        (
            "#070F#6P他就在这里和妹妹两人\x01",
            "相依为命啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A53")

    ChrTalk(    #228
        0x103,
        (
            "#027F#6P他就在这里和妹妹两人\x01",
            "相依为命啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A90")

    label("loc_3A53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A90")

    ChrTalk(    #229
        0x105,
        (
            "#048F#6P他就在这里和妹妹两人\x01",
            "相依为命啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A90")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #230
        0x101,
        "#1004F#6P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_3AD0():
        OP_6D(-26280, 0, 46950, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AD0)

    def lambda_3AE8():
        OP_8E(0xFE, 0xFFFF98AE, 0x0, 0xB6EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3AE8)
    WaitChrThread(0x101, 0x2)
    OP_44(0x9, 0x1)

    ChrTalk(    #231
        0x101,
        "#1011F#6P这照片……\x02",
    )

    CloseMessageWindow()
    OP_43(0xF7, 0x1, 0x0, 0x10)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x11)
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240082, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #232
        (
            "\x07\x00#1006F这是阿加特\x01",
            "小时候的照片吧。\x02\x03",

            "那么，这个女孩子……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(300, 310, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #233
        (
            "\x07\x00#066F嗯……\x01",
            "应该是米夏吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C4A")
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #234
        (
            "\x07\x00#023F哎呀呀……\x01",
            "#021F好可爱的女孩啊。\x02\x03",

            "应该和阿加特\x01",
            "关系相当亲密吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jump("loc_3D17")

    label("loc_3C4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CB9")
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("奥利维尔")

    AnonymousTalk(    #235
        (
            "\x07\x00#031F唔……\x01",
            "真是个可爱女孩啊。\x02\x03",

            "#030F应该和阿加特\x01",
            "关系相当亲密吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jump("loc_3D17")

    label("loc_3CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D17")
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("科洛丝")

    AnonymousTalk(    #236
        (
            "\x07\x00#048F好可爱的女孩子……\x02\x03",

            "应该和阿加特\x01",
            "关系相当亲密吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()

    label("loc_3D17")

    SetMessageWindowPos(300, 310, -1, -1)
    SetChrName("提妲")

    AnonymousTalk(    #237
        (
            "\x07\x00#067F嘿嘿，我想是吧。\x02\x03",

            "阿加特和米夏\x01",
            "都笑得好开心……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #238
        (
            "\x07\x00#1006F嗯……真的是呢。\x02\x03",

            "年龄的话，阿加特是１４岁左右，\x01",
            "米夏是１２岁的样子吧？\x02\x03",

            "阿加特…啊哈\x01",
            "那时还是个毛头小子呢。\x02\x03",

            "#1001F呵呵，真好玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E93")
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("金")

    AnonymousTalk(    #239
        (
            "\x07\x00#070F嗯，男人过去的照片\x01",
            "不要太认真考究。\x02\x03",

            "很难为情的。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #240
        "\x07\x00#1016F啊哈哈……是吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()

    label("loc_3E93")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x101, 180, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #241
        0x101,
        (
            "#1015F#5P话说回来……\x02\x03",

            "为什么阿加特\x01",
            "要隐瞒妹妹的事呢？\x02\x03",

            "一直说的好像\x01",
            "她还活着一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x9,
        (
            "#063F嗯……不过呢。\x02\x03",

            "#561F仔细一想阿加特哥哥\x01",
            "好像从来没说过\x01",
            "米夏还活着呢。\x02\x03",

            "『偶尔回去露个脸』\x01",
            "原来是说扫墓……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(300)

    ChrTalk(    #243
        0x101,
        (
            "#1026F这么说来也是……\x02\x03",

            "#1015F不过，我们\x01",
            "都误会了这事\x01",
            "阿加特应该也知道吧。\x02\x03",

            "为什么从来不纠正呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x9,
        (
            "#063F这我也不大清楚……\x02\x03",

            "#067F不过，阿加特哥哥\x01",
            "说过工作告一段落之后\x01",
            "会介绍给我的……\x02\x03",

            "我想他是打算在那时\x01",
            "好好解释的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        (
            "#1006F是吗……也是啊。\x02\x03",

            "#1007F嗯，他到底是怎么想的\x01",
            "以后再问吧……\x02\x03",

            "#1015F对了，提妲。\x02\x03",

            "我们差不多\x01",
            "该回柏斯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        "#064F啊……？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #247
        (
            "\x07\x05说明了必须去协会\x01",
            "等候王国军联络的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #248
        0x9,
        (
            "#063F这样啊……\x02\x03",

            "……………………………\x02\x03",

            "#561F那、那个，姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        (
            "#1006F恩，我们了解，你不用多说。\x02\x03",

            "为了照顾阿加特\x01",
            "你想说要留在这里吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #250
        0x9,
        "#065F啊啊啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        (
            "#1028F哼哼，可别小看\x01",
            "姐姐我哦。\x02\x03",

            "妹妹在想什么\x01",
            "我全～都知道啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x9,
        "#562F啊、啊呜～……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42A5")

    ChrTalk(    #253
        0x103,
        (
            "#021F#6P呵呵，这边的事\x01",
            "就不必担心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4316")

    label("loc_42A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42DF")

    ChrTalk(    #254
        0x104,
        (
            "#031F#6P呼，这边的事\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4316")

    label("loc_42DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4316")

    ChrTalk(    #255
        0x105,
        (
            "#041F#6P呵呵，这边的事\x01",
            "请不必担心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4316")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4363")

    ChrTalk(    #256
        0x108,
        (
            "#070F#6P你啊，\x01",
            "就专心照顾阿加特吧，\x01",
            "让他早日恢复健康。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4406")

    label("loc_4363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43B4")

    ChrTalk(    #257
        0x105,
        (
            "#048F#6P提妲啊，\x01",
            "你就专心照顾阿加特吧，\x01",
            "让他早日恢复健康。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4406")

    label("loc_43B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4406")

    ChrTalk(    #258
        0x104,
        (
            "#035F#6P呼，提妲\x01",
            "就用你的爱来照顾阿加特，\x01",
            "让他早日恢复原样吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4406")

    OP_44(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    Sleep(300)

    ChrTalk(    #259
        0x9,
        (
            "#560F#2P姐姐……大家……\x02\x03",

            "#067F那个那个……\x01",
            "感激不尽！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1016F哎呀～不需要\x01",
            "特别道谢啦。\x02\x03",

            "#1006F阿加特要是醒了，\x01",
            "能把刚才的事转告他吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)

    ChrTalk(    #261
        0x9,
        (
            "#064F啊，可能要协助王国军\x01",
            "作战的事对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1006F嗯，还有阿加特\x01",
            "要是再勉强乱来的话，\x01",
            "就算用身子挡也要挡住他。\x02\x03",

            "在没有完全恢复之前，\x01",
            "绝对不许他起床哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "#067F嗯……我会努力的！\x02\x03",

            "#560F姐姐你们……\x01",
            "也要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-25860, 0, 43830, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -25790, 0, 43940, 180)
    SetChrPos(0x1, -25790, 0, 43940, 180)
    SetChrPos(0x2, -25790, 0, 43940, 180)
    ClearChrFlags(0xF7, 0x4)
    ClearChrFlags(0xF8, 0x4)
    OP_69(0x0, 0x0)
    OP_8C(0x9, 90, 0)
    OP_4B(0x9, 255)
    OP_A2(0x1A1B)
    OP_28(0x94, 0x1, 0x800)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_12_36F7 end

    def Function_13_4643(): pass

    label("Function_13_4643")

    OP_8E(0xFE, 0xFFFF9B10, 0x0, 0xAFBE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_4643 end

    def Function_14_465F(): pass

    label("Function_14_465F")

    OP_8E(0xFE, 0xFFFF98F4, 0x0, 0xA726, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF9DFE, 0x0, 0xA9E2, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_465F end

    def Function_15_468F(): pass

    label("Function_15_468F")

    OP_8E(0xFE, 0xFFFF98CC, 0x0, 0xAAC8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_468F end

    def Function_16_46AB(): pass

    label("Function_16_46AB")

    OP_8E(0xFE, 0xFFFF9CDC, 0x0, 0xB108, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_46AB end

    def Function_17_46C7(): pass

    label("Function_17_46C7")

    OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0xAFB4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_46C7 end

    def Function_18_46E3(): pass

    label("Function_18_46E3")

    FadeToDark(0, 0, -1)
    OP_6D(-15500, 30, 64410, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
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
        (0, "loc_479A"),
        (1, "loc_47A0"),
        (SWITCH_DEFAULT, "loc_47A6"),
    )


    label("loc_479A")

    OP_A2(0x1200)
    Jump("loc_47A6")

    label("loc_47A0")

    OP_A2(0x1201)
    Jump("loc_47A6")

    label("loc_47A6")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_18_46E3 end

    def Function_19_47DE(): pass

    label("Function_19_47DE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240082, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_19_47DE end

    SaveToFile()

Try(main)
