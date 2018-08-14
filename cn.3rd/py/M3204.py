from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3204   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        '卡西乌斯',                             # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
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


    AddCharChip(
        'ED6_DT27/CH03670 ._CH',             # 00
        'ED6_DT27/CH04670 ._CH',             # 01
        'ED6_DT27/CH04679 ._CH',             # 02
        'ED6_DT26/CH20307 ._CH',             # 03
        'ED6_DT26/CH20715 ._CH',             # 04
        'ED6_DT07/CH00330 ._CH',             # 05
        'ED6_DT07/CH00331 ._CH',             # 06
        'ED6_DT07/CH00430 ._CH',             # 07
        'ED6_DT07/CH00431 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT27/CH03670P._CP',             # 00
        'ED6_DT27/CH04670P._CP',             # 01
        'ED6_DT27/CH04679P._CP',             # 02
        'ED6_DT26/CH20307P._CP',             # 03
        'ED6_DT26/CH20715P._CP',             # 04
        'ED6_DT07/CH00330P._CP',             # 05
        'ED6_DT07/CH00331P._CP',             # 06
        'ED6_DT07/CH00430P._CP',             # 07
        'ED6_DT07/CH00431P._CP',             # 08
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


    DeclMonster(
        X                   = -63160,
        Z                   = 0,
        Y                   = 88730,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -20280,
        Z                   = 0,
        Y                   = 50020,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 900,
        Z                   = 0,
        Y                   = 24970,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15950,
        Z                   = 0,
        Y                   = -68010,
        Unknown_0C          = 180,
        Unknown_0E          = 7,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 61880,
        TriggerZ            = 0,
        TriggerY            = 26870,
        TriggerRange        = 1000,
        ActorX              = 61880,
        ActorZ              = 2000,
        ActorY              = 26870,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15240,
        TriggerZ            = 1000,
        TriggerY            = -34250,
        TriggerRange        = 1000,
        ActorX              = -15240,
        ActorZ              = 1000,
        ActorY              = -34250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53910,
        TriggerZ            = 1000,
        TriggerY            = -68930,
        TriggerRange        = 1000,
        ActorX              = 53910,
        ActorZ              = 1000,
        ActorY              = -68930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2800,
        TriggerZ            = 1000,
        TriggerY            = 25020,
        TriggerRange        = 1000,
        ActorX              = 2800,
        ActorZ              = 1000,
        ActorY              = 25020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_212",          # 00, 0
        "Function_1_24D",          # 01, 1
        "Function_2_2AA",          # 02, 2
        "Function_3_3D0",          # 03, 3
        "Function_4_4F6",          # 04, 4
        "Function_5_61C",          # 05, 5
        "Function_6_625",          # 06, 6
        "Function_7_28B4",         # 07, 7
        "Function_8_39E0",         # 08, 8
        "Function_9_3A9F",         # 09, 9
        "Function_10_3B78",        # 0A, 10
        "Function_11_42A3",        # 0B, 11
    )


    def Function_0_212(): pass

    label("Function_0_212")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22E")
    Event(0, 5)

    label("loc_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24C")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_24C")

    Return()

    # Function_0_212 end

    def Function_1_24D(): pass

    label("Function_1_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270")
    OP_6F(0x33, 0)
    Jump("loc_277")

    label("loc_270")

    OP_6F(0x33, 60)

    label("loc_277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_289")
    OP_6F(0x34, 0)
    Jump("loc_290")

    label("loc_289")

    OP_6F(0x34, 60)

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A2")
    OP_6F(0x35, 0)
    Jump("loc_2A9")

    label("loc_2A2")

    OP_6F(0x35, 60)

    label("loc_2A9")

    Return()

    # Function_1_24D end

    def Function_2_2AA(): pass

    label("Function_2_2AA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x33, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_31E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    Jump("loc_303")

    label("loc_303")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B98)
    Jump("loc_38C")

    label("loc_31E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x05\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_36D")

    label("loc_36D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x33, 60)
    OP_70(0x33, 0x0)

    label("loc_38C")

    Jump("loc_3C2")

    label("loc_38F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_2AA end

    def Function_3_3D0(): pass

    label("Function_3_3D0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x34, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A7, 1)"), scpexpr(EXPR_END)), "loc_444")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA7\x02\x07\x00。\x02",
    )

    Jump("loc_429")

    label("loc_429")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B99)
    Jump("loc_4B2")

    label("loc_444")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA7\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA7\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_493")

    label("loc_493")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x34, 60)
    OP_70(0x34, 0x0)

    label("loc_4B2")

    Jump("loc_4E8")

    label("loc_4B5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4E8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3D0 end

    def Function_4_4F6(): pass

    label("Function_4_4F6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x573, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x35, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_56A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_54F")

    label("loc_54F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B9A)
    Jump("loc_5D8")

    label("loc_56A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_5B9")

    label("loc_5B9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x35, 60)
    OP_70(0x35, 0x0)

    label("loc_5D8")

    Jump("loc_60E")

    label("loc_5DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_60E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4F6 end

    def Function_5_61C(): pass

    label("Function_5_61C")

    Call(0, 6)
    Call(0, 7)
    Return()

    # Function_5_61C end

    def Function_6_625(): pass

    label("Function_6_625")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    OP_E0(238, 0x49, 0x2)
    OP_E0(238, 0x4A, 0x3)
    OP_E0(239, 0x4B, 0x2)
    OP_E0(239, 0x4C, 0x3)
    OP_E0(240, 0x4D, 0x2)
    OP_E0(240, 0x4E, 0x3)
    OP_E0(241, 0x4F, 0x2)
    OP_E0(241, 0x50, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 58980, 0, 73020, 180)
    SetChrSubChip(0x10, 0)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 58240, 0, 60860, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705")
    SetChrPos(0xEF, 59750, 0, 60760, 0)
    SetChrPos(0xF0, 57750, 0, 58900, 0)
    SetChrPos(0xF1, 59800, 0, 59090, 0)
    Jump("loc_78A")

    label("loc_705")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_749")
    SetChrPos(0xF0, 59750, 0, 60760, 0)
    SetChrPos(0xEF, 57750, 0, 58900, 0)
    SetChrPos(0xF1, 59800, 0, 59090, 0)
    Jump("loc_78A")

    label("loc_749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78A")
    SetChrPos(0xF1, 59750, 0, 60760, 0)
    SetChrPos(0xEF, 57750, 0, 58900, 0)
    SetChrPos(0xF0, 59800, 0, 59090, 0)

    label("loc_78A")

    OP_6D(60100, 0, 61450, 0)
    OP_67(0, 5590, -10000, 0)
    OP_6B(2380, 0)
    OP_6C(45000, 0)
    OP_6E(302, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #9
        0x10,
        "男性的声音",
        "#4P……来了吗。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_841")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8A8")

    label("loc_841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_869")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8A8")

    label("loc_869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_891")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8A8")

    label("loc_891")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8A8")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D5")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_93C")

    label("loc_8D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_93C")

    label("loc_8FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_93C")

    label("loc_925")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_93C")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D0")

    label("loc_969")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D0")

    label("loc_991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D0")

    label("loc_9B9")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9D0")

    Sleep(1000)

    def lambda_9DB():
        OP_6D(60220, 0, 74050, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_9DB)

    def lambda_9F3():
        OP_67(0, 4660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9F3)

    def lambda_A0B():
        OP_6B(2550, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_A0B)

    def lambda_A1B():
        OP_6E(285, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_A1B)
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #10
        0x10C,
        "#112F#1P卡西乌斯准将……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7B")

    ChrTalk(    #11
        0x101,
        "#1025F#1P老爸……\x02",
    )

    CloseMessageWindow()

    label("loc_A7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAD")

    ChrTalk(    #12
        0x102,
        "#1514F#1P……父亲………\x02",
    )

    CloseMessageWindow()

    label("loc_AAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AD9")

    ChrTalk(    #13
        0x103,
        "#1534F#1P老师……\x02",
    )

    CloseMessageWindow()

    label("loc_AD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0D")

    ChrTalk(    #14
        0x106,
        (
            "#556F#1P哼……\x01",
            "果然是你。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B40")

    ChrTalk(    #15
        0x108,
        "#573F#1P果然是大人您……\x02",
    )

    CloseMessageWindow()

    label("loc_B40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6B")

    ChrTalk(    #16
        0x10E,
        "#179F#1P果然……\x02",
    )

    CloseMessageWindow()

    label("loc_B6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9F")

    ChrTalk(    #17
        0x105,
        "#1382F#1P卡西乌斯先生……\x02",
    )

    CloseMessageWindow()

    label("loc_B9F")

    Sleep(300)
    Fade(1000)
    OP_6D(60510, 0, 70550, 0)
    OP_67(0, 4470, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(307, 0)

    def lambda_BEC():
        OP_8F(0xFE, 0xE362, 0x0, 0x10536, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BEC)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C72")

    def lambda_C1A():
        OP_8F(0xFE, 0xE934, 0x0, 0x105B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_C1A)
    Sleep(100)

    def lambda_C3A():
        OP_8F(0xFE, 0xE13C, 0x0, 0xFDF2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C3A)
    Sleep(100)

    def lambda_C5A():
        OP_8F(0xFE, 0xE8E4, 0x0, 0xFE4B, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_C5A)
    Jump("loc_D47")

    label("loc_C72")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDE")

    def lambda_C86():
        OP_8F(0xFE, 0xE934, 0x0, 0x105B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_C86)
    Sleep(100)

    def lambda_CA6():
        OP_8F(0xFE, 0xE13C, 0x0, 0xFDF2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_CA6)
    Sleep(100)

    def lambda_CC6():
        OP_8F(0xFE, 0xE8E4, 0x0, 0xFE4B, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_CC6)
    Jump("loc_D47")

    label("loc_CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D47")

    def lambda_CF2():
        OP_8F(0xFE, 0xE934, 0x0, 0x105B8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_CF2)
    Sleep(100)

    def lambda_D12():
        OP_8F(0xFE, 0xE13C, 0x0, 0xFDF2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D12)
    Sleep(100)

    def lambda_D32():
        OP_8F(0xFE, 0xE8E4, 0x0, 0xFE4B, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_D32)

    label("loc_D47")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "#1125F#5P呵呵……\x01",
            "我以为围绕『辉之环』的试练\x01",
            "已经全部结束了呢……\x02\x03",

            "没想到还会发生\x01",
            "这样的事情啊。\x02\x03",

            "#1122F恐怕连雷格纳特\x01",
            "都无法预见吧……\x02\x03",

            "凯文神父。\x01",
            "你们骑士团那边怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1065F#6P不……\x01",
            "我们也是完全一头雾水啊。\x02\x03",

            "#1840F虽然还不知道\x01",
            "封圣省的大人物\x01",
            "会对这样的事件了解多少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#1128F#5P嗯，是吗……\x02\x03",

            "#1123F算了，\x01",
            "现在讨论这件事也没什么用。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x42E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 2)
    OP_0D()
    Sleep(500)
    Fade(500)

    def lambda_F58():
        OP_6D(60510, 0, 71000, 500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_F58)

    def lambda_F70():
        OP_6B(2800, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_F70)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)

    ChrTalk(    #21
        0x10,
        (
            "#1125F#5P那么，开门见山地说，\x01",
            "我就是第三『守护者』。\x02\x03",

            "#1122F如果不打倒我，\x01",
            "前方的路就会永远封闭……\x02\x03",

            "你们能理解吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10C,
        (
            "#110F#12P嗯……\x01",
            "我们已经做好觉悟\x01",
            "才来到这里的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 9)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 11)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 13)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 15)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(600)

    ChrTalk(    #23
        0x10C,
        (
            "#115F#12P为了前进，\x01",
            "要亲手断绝留恋……\x02\x03",

            "#112F我会舍身忘己\x01",
            "全力应战。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#1120F#5P是吗……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13E9")
    Sleep(500)

    ChrTalk(    #25
        0x10,
        (
            "#1123F#5P不过……\x01",
            "竟然把还在旅途中的你们\x01",
            "也给卷了进来。\x02\x03",

            "#1120F你们的信我都看过了，\x01",
            "身体还好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_123B")

    ChrTalk(    #26
        0x101,
        "#1016F#12P嘿嘿……还好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#1501F#12P父亲才是……\x01",
            "看你这么精神，我就安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_123B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AD")

    ChrTalk(    #28
        0x101,
        (
            "#1012F#12P嗯……约修亚也很好。\x02\x03",

            "#1008F老爸才是……\x01",
            "看你这么精神，我就安心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1320")

    label("loc_12AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1320")

    ChrTalk(    #29
        0x102,
        (
            "#1513F#12P嗯……艾丝蒂尔也很好。\x02\x03",

            "#1501F父亲才是……\x01",
            "看到您这么健康，我就放心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1320")


    ChrTalk(    #30
        0x10,
        (
            "#1125F#5P呵呵……\x01",
            "我还不能输给年轻人啊。\x02\x03",

            "#1120F今天是个好机会。\x01",
            "让我看看你们修行的成果。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13BA")

    ChrTalk(    #31
        0x101,
        "#1017F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_13BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E9")

    ChrTalk(    #32
        0x102,
        "#1514F#12P明白……！\x02",
    )

    CloseMessageWindow()

    label("loc_13E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1529")
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#1124F#5P话说回来，雪拉扎德……\x01",
            "你完全变了个样子嘛。\x02\x03",

            "#1120F什么时候剪的头发？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x103,
        (
            "#1521F#12P呵呵，一个月之前吧。\x02\x03",

            "#1527F自从改变造型之后，\x01",
            "还没有让您见过呢。\x02\x03",

            "这一次……\x01",
            "我想重新让您见识一下\x01",
            "我作为游击士的成长！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#1120F#5P呵呵……\x01",
            "真是非常期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1618")
    Sleep(500)

    ChrTalk(    #36
        0x106,
        (
            "#051F#12P好了，大叔……\x01",
            "在这里让我逮到也算是你的末日啦。\x02\x03",

            "#053F刚见到你的时候，\x01",
            "我还一点也不理解\x01",
            "挥舞这把重剑的意义。\x02\x03",

            "#054F这份重量……\x01",
            "就让你重新体会一下！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        "#1125F#5P哼……可以啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1618")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1742")
    Sleep(500)

    ChrTalk(    #38
        0x10E,
        (
            "#179F#12P准将……\x01",
            "请恕我不自量力。\x02\x03",

            "#170F这次希望让您见识一下\x01",
            "和上次练习时相比\x01",
            "更厉害的剑法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1125F#5P呵呵，非常期待。\x02\x03",

            "#1120F你已经超越了\x01",
            "我所教授的基础，\x01",
            "开始确立自己的剑法了。\x02\x03",

            "请相信自己的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10E,
        "#171F#12P不胜惶恐……\x02",
    )

    CloseMessageWindow()

    label("loc_1742")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18BD")
    Sleep(500)

    ChrTalk(    #41
        0x10,
        (
            "#1120F#5P金……\x01",
            "又给你添麻烦了。\x02\x03",

            "#1123F但是，没想到\x01",
            "连回国的雾香都被利用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x108,
        (
            "#573F#12P没什么，\x01",
            "这也算是一种缘分吧。\x02\x03",

            "#070F话说回来，大人……\x01",
            "我会全力向您挑战的。\x02\x03",

            "我的拳法……\x01",
            "在『理』之达人面前\x01",
            "能够起到多大作用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#1125F#5P呵呵，彼此彼此。\x02\x03",

            "#1120F著名『泰斗』的至极招数……\x01",
            "请让我见识一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BA")
    Sleep(500)

    ChrTalk(    #44
        0x10A,
        (
            "#819F#12P啊哈哈，\x01",
            "没想到会变成这样……\x02\x03",

            "#816F那个……\x01",
            "总之拜托您了!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1125F#5P呵呵……\x01",
            "真想在弃剑之前\x01",
            "和你切磋一下呢。\x02\x03",

            "#1120F云老师直传的技术……\x01",
            "就让我亲眼见识一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10A,
        "#1310F#12P是！\x02",
    )

    CloseMessageWindow()

    label("loc_19BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD3")
    Sleep(500)

    ChrTalk(    #47
        0x10,
        (
            "#1125F#5P科洛蒂娅殿下。\x02\x03",

            "#1122F如果可以的话，\x01",
            "我觉得这里还是\x01",
            "交给其他人比较好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#1383F#12P不，那可不行。\x02\x03",

            "#1160F剑法暂且不提，\x01",
            "导力魔法我有足够的自信。\x02\x03",

            "请让我……\x01",
            "直接向您挑战吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        "#1125F#5P……知道了。\x02",
    )

    CloseMessageWindow()

    label("loc_1AD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE7")
    Sleep(500)

    ChrTalk(    #50
        0x10,
        (
            "#1123F#5P可是，奥利维特皇子……\x02\x03",

            "您也没有必要\x01",
            "亲自来这个地方吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x104,
        (
            "#1541F#12P呵，这也算是积累经验吧。\x02\x03",

            "#1540F和您的这场比试……\x01",
            "将成为我和那个怪物\x01",
            "交手时的宝贵经验。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#1120F#5P是这样啊……\x01",
            "那我可不能掉以轻心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D06")
    Sleep(500)

    ChrTalk(    #53
        0x10D,
        (
            "#278F#12P卡西乌斯·布莱特准将。\x02\x03",

            "#277F请恕我不自量力，\x01",
            "希望能见识一下著名『剑圣』的功夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#1125F#5P没什么，\x01",
            "范德尔家的小狮子。\x02\x03",

            "#1120F埃雷波尼亚帝国首屈一指的武术世家，\x01",
            "就让我期待一下你的表现吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10D,
        "#275F#12P……明白了。\x02",
    )

    CloseMessageWindow()

    label("loc_1D06")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E63")
    Sleep(500)

    ChrTalk(    #56
        0x10,
        (
            "#1120F#5P对了，提妲。\x02\x03",

            "丹和艾莉卡博士\x01",
            "好像已经回来了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x107,
        (
            "#067F#12P啊，是的……\x01",
            "就在不久之前。\x02\x03",

            "#560F咦，卡西乌斯叔叔\x01",
            "也认识他们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1125F#5P啊啊，\x01",
            "我刚当上游击士的时候，\x01",
            "尤其受到了丹的多方照顾呢。\x02\x03",

            "#1120F就算是为了他们……\x01",
            "你也要平安回去哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x107,
        "#066F#12P……是！\x02",
    )

    CloseMessageWindow()

    label("loc_1E63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F97")
    Sleep(500)

    ChrTalk(    #60
        0x10,
        (
            "#1123F#5P话说回来，\x01",
            "连你也被卷进来了啊。\x02\x03",

            "#1120F运输公司的生意怎么样呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10B,
        (
            "#210F#12P托您的福，\x01",
            "生意非常好。\x02\x03",

            "照这样下去，\x01",
            "向女王陛下借的钱\x01",
            "也能马上还清了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#1120F#5P呵呵，这样的话\x01",
            "就更得安全回去了对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10B,
        "#413F#12P啊……没错呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1F97")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2170")
    Sleep(500)

    ChrTalk(    #64
        0x110,
        "#262F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1124F#5P嗯？\x01",
            "怎么了，小丫头。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x110,
        (
            "#268F#12P大叔，你不是个普通人啊。\x02\x03",

            "#1302F玲无法把握你的实力……\x01",
            "到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#1120F#5P呵呵……\x01",
            "我的力量是无定形的螺旋……\x02\x03",

            "就算是天才，\x01",
            "也不可能简单地把握呢。\x02\x03",

            "#1121F这个暂且不说……\x01",
            "以后你就和艾丝蒂尔他们一起\x01",
            "来我洛连特的家里玩吧。\x02\x03",

            "我可是非常期待啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x110,
        (
            "#1308F#12P真、真是傻瓜……\x01",
            "那怎么可能！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2498")
    Sleep(500)

    ChrTalk(    #69
        0x10F,
        (
            "#1447F#12P……初次见面，剑圣大人。\x02\x03",

            "#1448F我是星杯的随从骑士，\x01",
            "莉丝·亚尔珍特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "#1124F#5P……亚尔珍特……\x02\x03",

            "#1125F原来如此。\x01",
            "你是露菲娜·亚尔珍特\x01",
            "小姐的妹妹吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10F,
        (
            "#1444F#12P咦……\x02\x03",

            "您认识我姐姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#1120F#5P没有直接见过面。\x02\x03",

            "但是，游击士协会的\x01",
            "很多地方都流传着她的名字。\x02\x03",

            "#1125F『千之腕』露菲娜·亚尔珍特。\x02\x03",

            "虽然年纪轻轻，\x01",
            "却是七耀教会首屈一指的交涉人、\x01",
            "解决难题的专家……\x02\x03",

            "#1122F这种作风应该说\x01",
            "更为接近游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x109,
        (
            "#1065F#12P嗯……确实如此啊。\x02\x03",

            "#1840F据说以前\x01",
            "游击士协会还曾经想\x01",
            "把姐姐拉拢过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#1120F#5P呵呵，如果她不是守护骑士的话\x01",
            "还是有交涉的余地的。\x02\x03",

            "#1125F而且听说在进行交涉前\x01",
            "她就去世了。\x02\x03",

            "真是可惜了这样的人才啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10F,
        "#1806F#12P……谢谢。\x02",
    )

    CloseMessageWindow()

    label("loc_2498")


    def lambda_249E():
        OP_6B(2700, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_249E)
    OP_1D(0x77)
    Sleep(1500)

    ChrTalk(    #76
        0x10,
        (
            "#1125F#5P那么……\x01",
            "现在就开始吧。\x02\x03",

            "#1122F虽然我想你们应该已经明白了，\x01",
            "不过我还是要提醒你们，我不会手下留情的。\x02\x03",

            "所以，理查德。\x01",
            "我要说的只有一句。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10C,
        "#112F#12P……请说。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_44(0xEE, 0x0)
    Fade(500)
    OP_6D(59010, 0, 75600, 0)
    OP_67(0, 2890, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(0, 0)
    OP_6E(352, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_25D0():

        label("loc_25D0")

        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_25D0")

    QueueWorkItem2(0x109, 0, lambda_25D0)

    def lambda_25EB():
        OP_6D(59010, 0, 74600, 4000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_25EB)

    def lambda_2603():
        OP_67(0, 2600, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2603)

    def lambda_261B():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_261B)

    def lambda_262B():
        OP_6E(345, 4000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_262B)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 52)
    SetChrFlags(0x10, 0x800)
    SetChrFlags(0x10, 0x2)
    SetChrPos(0x10, 58980, 0, 73020, 180)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x109, 58270, 0, 66820, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26EB")
    SetChrPos(0xEF, 59820, 0, 66810, 0)
    SetChrPos(0xF0, 57690, 0, 64819, 0)
    SetChrPos(0xF1, 60270, 0, 64819, 0)
    Jump("loc_2770")

    label("loc_26EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_272F")
    SetChrPos(0xF0, 59820, 0, 66810, 0)
    SetChrPos(0xEF, 57690, 0, 64819, 0)
    SetChrPos(0xF1, 60270, 0, 64819, 0)
    Jump("loc_2770")

    label("loc_272F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2770")
    SetChrPos(0xF1, 59820, 0, 66810, 0)
    SetChrPos(0xEF, 57690, 0, 64819, 0)
    SetChrPos(0xF0, 60270, 0, 64819, 0)

    label("loc_2770")

    OP_0D()
    Sleep(500)
    OP_22(0x7E, 0x1, 0x64)

    def lambda_2781():

        label("loc_2781")

        OP_99(0xFE, 0x38, 0x3B, 0x5DC)
        OP_48()
        Jump("loc_2781")

    QueueWorkItem2(0x10, 2, lambda_2781)
    WaitChrThread(0xEE, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_23(0x85)

    def lambda_27AA():
        OP_6D(59010, 0, 74460, 100)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_27AA)

    def lambda_27C2():
        OP_67(0, 2600, -10000, 100)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_27C2)

    def lambda_27DA():
        OP_6B(2850, 100)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_27DA)

    def lambda_27EA():
        OP_6E(341, 100)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_27EA)
    OP_23(0x7E)
    OP_44(0x10, 0x2)

    def lambda_2801():
        OP_99(0xFE, 0x40, 0x46, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2801)
    OP_22(0x1F4, 0x0, 0x64)
    Sleep(100)
    OP_22(0xF3, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x10, 0x3)
    OP_44(0x109, 0x0)
    Sleep(1000)

    ChrTalk(    #78
        0x10,
        (
            "#1125F#5P试着打赢我吧。#2100W #20W \x01",
            "#1122F──就这样。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #79
        0x10C,
        "#114F#6P#3S是……！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(100)
    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_6_625 end

    def Function_7_28B4(): pass

    label("Function_7_28B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_1D(0xAD)
    SetMapFlags(0x2000000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E0(238, 0x49, 0x2)
    OP_E0(238, 0x4A, 0x5)
    OP_E0(239, 0x4B, 0x2)
    OP_E0(239, 0x4C, 0x5)
    OP_E0(240, 0x4D, 0x2)
    OP_E0(240, 0x4E, 0x5)
    OP_E0(241, 0x4F, 0x2)
    OP_E0(241, 0x50, 0x5)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 58980, 0, 73020, 180)
    SetChrChipByIndex(0x10, 4)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x10, 0x800)
    ClearChrFlags(0x10, 0x2)
    OP_51(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x406), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x10, 0x3, 0x0, 0x8)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    PlayEffect(0x0, 0x0, 0x10, 100, 800, 100, 0, 0, 0, 2200, 3500, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x3C)
    SetChrPos(0x109, 57980, 0, 68490, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A1F")
    SetChrPos(0xEF, 59450, 0, 68450, 0)
    SetChrPos(0xF0, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66350, 0)
    Jump("loc_2AA4")

    label("loc_2A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A63")
    SetChrPos(0xF0, 59450, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66350, 0)
    Jump("loc_2AA4")

    label("loc_2A63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AA4")
    SetChrPos(0xF1, 59450, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF0, 59260, 0, 66350, 0)

    label("loc_2AA4")

    SetChrChipByIndex(0xEE, 10)
    SetChrSubChip(0xEE, 3)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 3)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 3)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 3)
    SetChrFlags(0xEE, 0x800)
    SetChrFlags(0xEF, 0x800)
    SetChrFlags(0xF0, 0x800)
    SetChrFlags(0xF1, 0x800)
    OP_43(0xEE, 0x0, 0x0, 0x9)
    OP_43(0xEF, 0x0, 0x0, 0x9)
    OP_43(0xF0, 0x0, 0x0, 0x9)
    OP_43(0xF1, 0x0, 0x0, 0x9)
    OP_6D(60160, 0, 71550, 0)
    OP_67(0, 4090, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(306, 0)

    def lambda_2B3F():
        OP_6B(2730, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2B3F)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #80
        0x109,
        (
            "#1070F#6P传、传说的『剑圣』……\x01",
            "……竟然这么厉害………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10C,
        (
            "#117F#12P呼、呼……\x01",
            "………成功了吗…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        (
            "#1125F#5P………漂亮。\x01",
            "终于跨过我这道障壁了呢。\x02\x03",

            "#1122F理查德啊……\x01",
            "你心头的迷雾终于明朗了吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_44(0x0, 0x0)
    Sleep(50)
    OP_44(0x1, 0x0)
    Sleep(50)
    OP_44(0x2, 0x0)
    Sleep(50)
    OP_44(0x3, 0x0)
    Sleep(500)

    ChrTalk(    #83
        0x10C,
        (
            "#115F#12P………是。\x02\x03",

            "不管身处什么立场，\x01",
            "都能够活用从您那里\x01",
            "继承的剑法……\x02\x03",

            "#111F所以，既然选择了这条路，\x01",
            "我就会勇敢的前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "#1120F#5P是吗……\x02\x03",

            "#1123F唉，如果你回来的话\x01",
            "就可以把所有的军务\x01",
            "压在你和希德身上……\x02\x03",

            "看来我想退役还早着呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10C,
        (
            "#119F#12P呵呵……\x01",
            "可不会那么容易呢。\x02\x03",

            "#112F……这次的事件……\x02\x03",

            "作为我最后的军务，\x01",
            "我将全力以赴\x01",
            "将其顺利解决。\x02\x03",

            "请放心。\x02",
        )
    )

    Jump("loc_2E2E")

    label("loc_2E2E")

    CloseMessageWindow()

    ChrTalk(    #86
        0x10,
        (
            "#1120F#5P嗯……\x01",
            "拜托了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FF4")
    Sleep(500)

    ChrTalk(    #87
        0x101,
        (
            "#1025F#12P老爸……\x02\x03",

            "我会和约修亚一起\x01",
            "平安回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x102,
        (
            "#1514F#12P……嗯。\x01",
            "您不用担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x10,
        (
            "#1125F#5P嗯……\x01",
            "你们一定没有问题的。\x02\x03",

            "#1120F要是有空了，\x01",
            "就常回利贝尔看看。\x02\x03",

            "#1121F那小姑娘是叫玲吗……\x01",
            "希望你们带着她一起回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1004F#12P啊……\x02\x03",

            "#1017F嗯……！\x01",
            "我们会的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1501F#12P哈哈……\x01",
            "到时候还请多关照。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B4")

    label("loc_2FF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30CC")

    ChrTalk(    #92
        0x101,
        (
            "#1025F#12P老爸……\x02\x03",

            "我会和约修亚一起\x01",
            "平安回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "#1125F#5P嗯……\x01",
            "你们一定没有问题的。\x02\x03",

            "#1120F要是有空了，\x01",
            "就常回利贝尔看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1017F#12P嘿嘿，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_31B4")

    label("loc_30CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31B4")

    ChrTalk(    #95
        0x102,
        (
            "#1513F#12P父亲……\x01",
            "请不用担心。\x02\x03",

            "#1514F我一定会带着艾丝蒂尔\x01",
            "平安回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x10,
        (
            "#1125F#5P嗯……\x01",
            "你们一定没有问题的。\x02\x03",

            "#1120F要是有空了，\x01",
            "就常回利贝尔看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        "#1501F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    label("loc_31B4")

    Sleep(500)

    ChrTalk(    #98
        0x10,
        (
            "#1125F#5P……那么……\x01",
            "好像就要到极限了……\x02\x03",

            "#1122F凯文神父……\x01",
            "你也该注意到了吧。\x02\x03",

            "关于『影之王』的真实身份。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x109,
        (
            "#1840F#6P是啊……\x01",
            "已经只差一步了。\x02\x03",

            "#1075F在下一个领域\x01",
            "大概就可以得到确信。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "#1128F#5P#40W是吗……\x02\x03",

            "#1125F#40W……对你\x01",
            "我没有什么好说的……\x02\x03",

            "#40W但是……\x01",
            "不要忘了这点……\x02\x03",

            "#1120F#40W人……不管有怎样的愿望……\x01",
            "都不会希望真正的孤独……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x109,
        "#1079F#6P#3S！！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, 100, -600, 0, 0, 0, 0, 2100, 2100, 2100, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_33D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_33D6)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_342B")

    ChrTalk(    #102
        0x101,
        "#1026F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_342B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3459")

    ChrTalk(    #103
        0x102,
        "#1504F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3459")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3487")

    ChrTalk(    #104
        0x103,
        "#1523F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3487")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34BA")

    ChrTalk(    #105
        0x106,
        "#055F#12P……啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_34BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34ED")

    ChrTalk(    #106
        0x108,
        "#072F#12P……啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_34ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_351A")

    ChrTalk(    #107
        0x10E,
        "#173F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_351A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3548")

    ChrTalk(    #108
        0x10A,
        "#1317F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_357B")

    ChrTalk(    #109
        0x10D,
        "#273F#12P……啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_357B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35A8")

    ChrTalk(    #110
        0x110,
        "#264F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_35A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35D6")

    ChrTalk(    #111
        0x105,
        "#1163F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_35D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_360A")

    ChrTalk(    #112
        0x104,
        "#1543F#12P……啊………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_360A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3638")

    ChrTalk(    #113
        0x10F,
        "#1444F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3662")

    ChrTalk(    #114
        0x10B,
        "#213F#12P啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3662")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_369F")

    ChrTalk(    #115
        0x107,
        "#063F#12P……卡西乌斯叔叔………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_369F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36E2")

    ChrTalk(    #116
        0x10B,
        "#215F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_36E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3726")

    ChrTalk(    #117
        0x10F,
        "#1445F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_3726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_376A")

    ChrTalk(    #118
        0x104,
        "#1542F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_376A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37AE")

    ChrTalk(    #119
        0x105,
        "#1163F#12P………卡西乌斯先生……………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_37AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37F2")

    ChrTalk(    #120
        0x110,
        "#1307F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_37F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3835")

    ChrTalk(    #121
        0x10D,
        "#276F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_3835")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3878")

    ChrTalk(    #122
        0x10A,
        "#813F#12P………卡西乌斯先生……………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_3878")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38B9")

    ChrTalk(    #123
        0x10E,
        "#175F#12P……卡西乌斯准将……………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_38B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38FC")

    ChrTalk(    #124
        0x108,
        "#572F#12P……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_38FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3939")

    ChrTalk(    #125
        0x106,
        "#053F#12P………大叔………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_3939")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_397B")

    ChrTalk(    #126
        0x103,
        "#1532F#12P…………老师…………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_39B8")

    label("loc_397B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39B8")

    ChrTalk(    #127
        0x102,
        "#1503F#12P…………父亲………………\x02",
    )

    CloseMessageWindow()

    label("loc_39B8")


    def lambda_39BE():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_39BE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M4110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_28B4 end

    def Function_8_39E0(): pass

    label("Function_8_39E0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A01")
    Sleep(100)
    Jump("loc_3A7C")

    label("loc_3A01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A16")
    Sleep(200)
    Jump("loc_3A7C")

    label("loc_3A16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2B")
    Sleep(300)
    Jump("loc_3A7C")

    label("loc_3A2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A40")
    Sleep(400)
    Jump("loc_3A7C")

    label("loc_3A40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A55")
    Sleep(500)
    Jump("loc_3A7C")

    label("loc_3A55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A6A")
    Sleep(600)
    Jump("loc_3A7C")

    label("loc_3A6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7C")
    Sleep(700)

    label("loc_3A7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A9E")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_3A7C")

    label("loc_3A9E")

    Return()

    # Function_8_39E0 end

    def Function_9_3A9F(): pass

    label("Function_9_3A9F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B77")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC9")
    Sleep(100)
    Jump("loc_3B44")

    label("loc_3AC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ADE")
    Sleep(200)
    Jump("loc_3B44")

    label("loc_3ADE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF3")
    Sleep(300)
    Jump("loc_3B44")

    label("loc_3AF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B08")
    Sleep(400)
    Jump("loc_3B44")

    label("loc_3B08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B1D")
    Sleep(500)
    Jump("loc_3B44")

    label("loc_3B1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B32")
    Sleep(600)
    Jump("loc_3B44")

    label("loc_3B32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B44")
    Sleep(700)

    label("loc_3B44")

    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_9_3A9F")

    label("loc_3B77")

    Return()

    # Function_9_3A9F end

    def Function_10_3B78(): pass

    label("Function_10_3B78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 57980, 0, 68490, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BD9")
    SetChrPos(0xEF, 59650, 0, 68450, 0)
    SetChrPos(0xF0, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66650, 0)
    Jump("loc_3C5E")

    label("loc_3BD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C1D")
    SetChrPos(0xF0, 59650, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF1, 59260, 0, 66650, 0)
    Jump("loc_3C5E")

    label("loc_3C1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5E")
    SetChrPos(0xF1, 59650, 0, 68450, 0)
    SetChrPos(0xEF, 57410, 0, 66470, 0)
    SetChrPos(0xF0, 59260, 0, 66650, 0)

    label("loc_3C5E")

    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_6D(60000, 0, 71900, 0)
    OP_67(0, 4740, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #128
        0x10C,
        "#116F#5P………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_3D0F():
        OP_6D(60000, 0, 68900, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3D0F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D5F")

    def lambda_3D35():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3D35)
    Sleep(300)

    def lambda_3D48():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D48)
    Sleep(100)
    OP_8C(0xF0, 45, 400)
    Jump("loc_3DD8")

    label("loc_3D5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9D")

    def lambda_3D73():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_3D73)
    Sleep(300)

    def lambda_3D86():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D86)
    Sleep(100)
    OP_8C(0xEF, 45, 400)
    Jump("loc_3DD8")

    label("loc_3D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD8")

    def lambda_3DB1():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_3DB1)
    Sleep(300)

    def lambda_3DC4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3DC4)
    Sleep(100)
    OP_8C(0xEF, 45, 400)

    label("loc_3DD8")

    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #129
        0x10C,
        (
            "#111F#5P好了……\x01",
            "剩下的只有一个领域了。\x02\x03",

            "#119F不管前方有\x01",
            "什么样的考验等待着……\x01",
            "都没有必要害怕了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E8D")

    ChrTalk(    #130
        0x101,
        "#1016F#6P哈哈……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EBE")

    ChrTalk(    #131
        0x102,
        "#1513F#6P……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3EBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EF3")

    ChrTalk(    #132
        0x103,
        "#1521F#6P呵呵……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3EF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F27")

    ChrTalk(    #133
        0x106,
        "#556F#6P呵……确实啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3F27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F5B")

    ChrTalk(    #134
        0x108,
        "#573F#6P哈哈……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3F5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F90")

    ChrTalk(    #135
        0x105,
        "#1165F#6P呵呵……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3F90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC4")

    ChrTalk(    #136
        0x10E,
        "#179F#6P呵……确实啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3FC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FFB")

    ChrTalk(    #137
        0x10A,
        "#1314F#6P啊哈哈……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_3FFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4032")

    ChrTalk(    #138
        0x104,
        "#1545F#6P呵呵……确实啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_4032")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4068")

    ChrTalk(    #139
        0x10D,
        "#278F#6P呵呵……确实啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_4068")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40A6")

    ChrTalk(    #140
        0x107,
        (
            "#067F#6P嘿嘿……\x01",
            "是啊。\x02",
        )
    )

    Jump("loc_40A2")

    label("loc_40A2")

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_40A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40DB")

    ChrTalk(    #141
        0x10F,
        "#1447F#6P呵呵……确实。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4115")

    label("loc_40DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4115")

    ChrTalk(    #142
        0x110,
        (
            "#263F#6P确实……\x01",
            "可以这么说呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4115")


    ChrTalk(    #143
        0x109,
        (
            "#1075F#6P……我们先回周游道，\x01",
            "确认一下最后的石碑吧。\x02\x03",

            "#1840F那上面一定刻着\x01",
            "进入下一领域的条件。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x2B20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41AC")
    OP_A2(0x2639)

    label("loc_41AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41BD")
    OP_A2(0x263A)

    label("loc_41BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41CE")
    OP_A2(0x263B)

    label("loc_41CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41DF")
    OP_A2(0x263C)

    label("loc_41DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F0")
    OP_A2(0x263D)

    label("loc_41F0")

    OP_28(0x3A, 0x4, 0x4)
    OP_28(0x3A, 0x4, 0x8)
    OP_28(0x3A, 0x1, 0x1)
    OP_6D(58950, 0, 68910, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 58950, 0, 68910, 180)
    SetChrPos(0x1, 58950, 0, 68910, 180)
    SetChrPos(0x2, 58950, 0, 68910, 180)
    SetChrPos(0x3, 58950, 0, 68910, 180)
    OP_21()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_1D(0xE8)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    EventEnd(0x0)
    Return()

    # Function_10_3B78 end

    def Function_11_42A3(): pass

    label("Function_11_42A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4372")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(6912)
    Sleep(500)
    Jump("loc_4375")

    label("loc_4372")

    TalkBegin(0xFF)

    label("loc_4375")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #144
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_439F")

    label("loc_439F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_450A")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_4404")

    label("loc_4404")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4421"),
        (1, "loc_449C"),
        (2, "loc_44CB"),
        (SWITCH_DEFAULT, "loc_44FA"),
    )


    label("loc_4421")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE8)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4507")

    label("loc_449C")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #145
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_44C8")

    label("loc_44C8")

    Jump("loc_4507")

    label("loc_44CB")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #146
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_44F7")

    label("loc_44F7")

    Jump("loc_4507")

    label("loc_44FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4507")

    label("loc_4507")

    Jump("loc_43B2")

    label("loc_450A")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4537")
    OP_A2(0x259D)
    EventEnd(0x1)
    Jump("loc_453A")

    label("loc_4537")

    TalkEnd(0xFF)

    label("loc_453A")

    Return()

    # Function_11_42A3 end

    SaveToFile()

Try(main)
