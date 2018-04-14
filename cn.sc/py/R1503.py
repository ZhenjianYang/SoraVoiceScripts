from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1503   ._SN',
        MapName             = 'Bose',
        Location            = 'R1503.x',
        MapIndex            = 59,
        MapDefaultBGM       = "ed60022",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/R1503_1 ._SN',
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
        '王国军士官',                           # 9
        '王国军士兵',                           # 10
        '王国军士兵',                           # 11
        '拉文努山道方向',                       # 12
        '拉文努山道方向',                       # 13
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
        'ED6_DT07/CH00064 ._CH',             # 00
        'ED6_DT07/CH01600 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH00064P._CP',             # 00
        'ED6_DT07/CH01600P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
    )

    DeclNpc(
        X                   = 1280,
        Z                   = 10,
        Y                   = 19450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 2300,
        Z                   = 20,
        Y                   = 19450,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -120,
        Z                   = 50,
        Y                   = 21740,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -111060,
        Z                   = -20,
        Y                   = -19200,
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

    DeclNpc(
        X                   = 1140,
        Z                   = 10,
        Y                   = -19200,
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
        X                   = -118500,
        Y                   = -2000,
        Z                   = 3200,
        Range               = -103000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x17D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -114320,
        TriggerZ            = 0,
        TriggerY            = 6860,
        TriggerRange        = 1500,
        ActorX              = -114320,
        ActorZ              = 50,
        ActorY              = 6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2180,
        TriggerZ            = 0,
        TriggerY            = 6860,
        TriggerRange        = 1500,
        ActorX              = -2180,
        ActorZ              = 50,
        ActorY              = 6860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6240,
        TriggerZ            = 0,
        TriggerY            = 17780,
        TriggerRange        = 1000,
        ActorX              = 6240,
        ActorZ              = 1000,
        ActorY              = 17780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -105760,
        TriggerZ            = 0,
        TriggerY            = 17780,
        TriggerRange        = 1000,
        ActorX              = -105760,
        ActorZ              = 1000,
        ActorY              = 17780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_2EE",          # 01, 1
        "Function_2_424",          # 02, 2
        "Function_3_5A1",          # 03, 3
        "Function_4_70D",          # 04, 4
        "Function_5_7FB",          # 05, 5
        "Function_6_949",          # 06, 6
        "Function_7_D72",          # 07, 7
        "Function_8_E6F",          # 08, 8
        "Function_9_EAC",          # 09, 9
        "Function_10_10BC",        # 0A, 10
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21C")
    Jump("loc_2CE")

    label("loc_21C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29B")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_72(0x0, 0x2)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x2)
    OP_72(0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_28E")
    SetChrPos(0x8, -107510, 0, 18670, 270)
    SetChrPos(0x9, -108310, 10, 21740, 180)
    SetChrPos(0xA, -112120, -20, 21740, 180)
    Jump("loc_298")

    label("loc_28E")

    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_298")

    Jump("loc_2CE")

    label("loc_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_2CE")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 4130, 10, 21680, 180)
    SetChrPos(0xA, 0, 10, 21680, 180)

    label("loc_2CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ED")
    Event(1, 3)

    label("loc_2ED")

    Return()

    # Function_0_212 end

    def Function_1_2EE(): pass

    label("Function_1_2EE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_302"),
        (101, "loc_31C"),
        (102, "loc_31C"),
        (SWITCH_DEFAULT, "loc_336"),
    )


    label("loc_302")

    OP_16(0x2, 0xFA0, 0xFFFE0FE8, 0xFFFE2758, 0x23006B)
    ClearChrFlags(0xB, 0x4)
    Jump("loc_336")

    label("loc_31C")

    OP_16(0x2, 0xFA0, 0xFFFC5A68, 0xFFFE2758, 0x230022)
    ClearChrFlags(0xC, 0x4)
    Jump("loc_336")

    label("loc_336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34E")
    OP_B1("R1503_y")
    Jump("loc_357")

    label("loc_34E")

    OP_B1("R1503_n")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41B")
    OP_72(0x0, 0x2)
    OP_72(0x0, 0x4)
    OP_72(0x1, 0x2)
    OP_72(0x1, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_418")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 6240, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    LoadEffect(0x2, "map\\\\mp027_00.eff")
    PlayEffect(0x2, 0x2, 0xFF, -105760, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_418")

    Jump("loc_423")

    label("loc_41B")

    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)

    label("loc_423")

    Return()

    # Function_1_2EE end

    def Function_2_424(): pass

    label("Function_2_424")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_58B")

    label("loc_449")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_462")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_58B")

    label("loc_462")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47B")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_58B")

    label("loc_47B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_494")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_58B")

    label("loc_494")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AD")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_58B")

    label("loc_4AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C6")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_58B")

    label("loc_4C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_58B")

    label("loc_4DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F8")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_58B")

    label("loc_4F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_511")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_58B")

    label("loc_511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_58B")

    label("loc_52A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_58B")

    label("loc_543")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55C")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_58B")

    label("loc_55C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_575")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_58B")

    label("loc_575")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58B")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_58B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_58B")

    label("loc_5A0")

    Return()

    # Function_2_424 end

    def Function_3_5A1(): pass

    label("Function_3_5A1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_709")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_600")

    ChrTalk(    #0
        0xFE,
        (
            "后面的事情就\x01",
            "交给我们王国军吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "那么，接下来也请小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_658")

    label("loc_600")


    ChrTalk(    #2
        0xFE,
        "诸位，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "后面的事情就\x01",
            "交给我们王国军吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "那么，接下来也请小心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_658")

    Jump("loc_709")

    label("loc_65B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_6F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6B7")

    ChrTalk(    #5
        0xFE,
        (
            "那边的回复装置\x01",
            "可以自由使用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "那么就拜托你们\x01",
            "继续扫荡魔兽了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F0")

    label("loc_6B7")


    ChrTalk(    #7
        0xFE,
        "哦，回来了吗?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "那边的回复装置\x01",
            "可以自由使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_6F0")

    Jump("loc_709")

    label("loc_6F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_705")
    Call(1, 1)
    Jump("loc_709")

    label("loc_705")

    Call(1, 0)

    label("loc_709")

    TalkEnd(0x8)
    Return()

    # Function_3_5A1 end

    def Function_4_70D(): pass

    label("Function_4_70D")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_7C1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_75B")

    ChrTalk(    #9
        0xFE,
        "这次真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "这下我们\x01",
            "可以专心警备了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE")

    label("loc_75B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_7A8")

    ChrTalk(    #11
        0xFE,
        (
            "要注意\x01",
            "颜色不一样的家伙哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "对方会使用\x01",
            "没见过的魔法。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BE")

    label("loc_7A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_7BA")
    Call(1, 1)
    Jump("loc_7BE")

    label("loc_7BA")

    Call(1, 0)

    label("loc_7BE")

    Jump("loc_7F7")

    label("loc_7C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_7F7")

    ChrTalk(    #13
        0xFE,
        (
            "辛苦了。\x01",
            "后边的警备就交给我们国境师团吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F7")

    TalkEnd(0x9)
    Return()

    # Function_4_70D end

    def Function_5_7FB(): pass

    label("Function_5_7FB")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_859")

    ChrTalk(    #14
        0xFE,
        "各位，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "呀，到底是游击士啊。\x01",
            "消灭魔兽真是手到擒来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EF")

    label("loc_859")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7D, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_8AB")

    ChrTalk(    #16
        0xFE,
        "里、里面的情况怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "如果没不断出现\x01",
            "那个奇怪的魔兽就好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EF")

    label("loc_8AB")


    ChrTalk(    #18
        0xFE,
        (
            "这个时候\x01",
            "前面是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "至于原因……\x01",
            "请问我的上司吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EF")

    Jump("loc_945")

    label("loc_8F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_945")

    ChrTalk(    #20
        0xFE,
        (
            "这个时候\x01",
            "前面是禁止进入的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "毕竟算是事件的现场嘛。\x01",
            "需要保持原样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_945")

    TalkEnd(0xA)
    Return()

    # Function_5_7FB end

    def Function_6_949(): pass

    label("Function_6_949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 6)), scpexpr(EXPR_END)), "loc_951")
    Return()

    label("loc_951")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_969")
    Call(0, 7)
    Sleep(200)

    label("loc_969")

    Fade(1000)
    OP_6D(-110460, -10, 4260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -110960, -10, 4750, 0)
    SetChrPos(0x107, -109990, 0, 4740, 0)
    SetChrPos(0xF8, -111260, 0, 3400, 0)
    SetChrPos(0xF9, -110120, 0, 3250, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #22
        0x101,
        "#1004F#6P啊……！\x02",
    )

    CloseMessageWindow()
    OP_6D(-108610, 10, 24070, 3000)
    Sleep(1500)

    def lambda_A28():
        OP_6D(-109220, -30, 22140, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A28)

    def lambda_A40():
        OP_8E(0xFE, 0xFFFE4FA8, 0x0, 0x50BE, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A40)
    Sleep(100)

    def lambda_A60():
        OP_8E(0xFE, 0xFFFE548A, 0x1E, 0x4FD8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_A60)
    Sleep(100)

    def lambda_A80():
        OP_8E(0xFE, 0xFFFE4D82, 0x14, 0x4B82, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A80)
    Sleep(100)

    def lambda_AA0():
        OP_8E(0xFE, 0xFFFE5390, 0x28, 0x4A6A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_AA0)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #23
        0x101,
        (
            "#1020F这里……\x01",
            "是废坑的入口吧。\x02\x03",

            "门开着就是说\x01",
            "难道…\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8E(0x107, 0xFFFE5322, 0xFFFFFFE2, 0x57C6, 0x7D0, 0x0)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 0)
    OP_0D()
    Sleep(1000)
    Fade(250)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #24
        0x107,
        (
            "#065F#5P姐、姐姐！\x02\x03",

            "这个掉下来的锁……\x01",
            "好像是刚刚取下的！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #25
        0x101,
        "#1002F果然……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C10")

    ChrTalk(    #26
        0x108,
        (
            "#072F#4P是他干的吧。\x01",
            "看来似乎跑进去了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C91")

    label("loc_C10")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C52")

    ChrTalk(    #27
        0x103,
        (
            "#022F#4P是阿加特干的吧。\x01",
            "是不是跑进去了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C91")

    label("loc_C52")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C91")

    ChrTalk(    #28
        0x104,
        (
            "#032F#4P阿加特干的吧。\x01",
            "看来似乎跑进去了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC6")

    ChrTalk(    #29
        0x105,
        "#043F#4P要赶快追上去才行……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D2F")

    label("loc_CC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFC")

    ChrTalk(    #30
        0x104,
        (
            "#032F#4P唔……\x01",
            "似乎要抓紧才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D2F")

    label("loc_CFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2F")

    ChrTalk(    #31
        0x103,
        (
            "#022F#4P这……\x01",
            "看来要抓紧才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2F")

    OP_8C(0x101, 180, 500)

    ChrTalk(    #32
        0x101,
        "#1005F#5PＯＫ～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 500)

    ChrTalk(    #33
        0x107,
        "#062F#5P好！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A16)
    OP_28(0x94, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_6_949 end

    def Function_7_D72(): pass

    label("Function_7_D72")

    FadeToDark(0, 0, -1)
    OP_6D(-153930, -10, 11410, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_E29"),
        (1, "loc_E2F"),
        (SWITCH_DEFAULT, "loc_E35"),
    )


    label("loc_E29")

    OP_A2(0x1200)
    Jump("loc_E35")

    label("loc_E2F")

    OP_A2(0x1201)
    Jump("loc_E35")

    label("loc_E35")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_7_D72 end

    def Function_8_E6F(): pass

    label("Function_8_E6F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #34
        "\x07\x05拉文努矿山\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_E6F end

    def Function_9_EAC(): pass

    label("Function_9_EAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFD")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_10BB")

    label("loc_EFD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #36
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A0")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 6240, 1000, 17780, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x32)
    OP_73(0x0)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 6240, 1000, 17780, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 6240, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_10A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_10BA")

    Return()

    label("loc_10BB")

    Return()

    # Function_9_EAC end

    def Function_10_10BC(): pass

    label("Function_10_10BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_12CB")

    label("loc_110D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B0")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, -105760, 1000, 17780, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x32)
    OP_73(0x1)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x3, "map\\\\mp027_01.eff")
    PlayEffect(0x3, 0x3, 0xFF, -105760, 1000, 17780, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x3, 0x2)
    PlayEffect(0x2, 0x2, 0xFF, -105760, 1000, 17780, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_12B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12CA")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_12CA")

    Return()

    label("loc_12CB")

    Return()

    # Function_10_10BC end

    SaveToFile()

Try(main)
