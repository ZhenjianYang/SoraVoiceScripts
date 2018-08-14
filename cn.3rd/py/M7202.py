from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7202   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60223",
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
        '封印石? ',                             # 9
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
        'ED6_DT29/CH14470 ._CH',             # 00
        'ED6_DT29/CH14471 ._CH',             # 01
        'ED6_DT29/CH15050 ._CH',             # 02
        'ED6_DT29/CH15051 ._CH',             # 03
        'ED6_DT29/CH15060 ._CH',             # 04
        'ED6_DT29/CH15061 ._CH',             # 05
        'ED6_DT29/CH14480 ._CH',             # 06
        'ED6_DT29/CH14481 ._CH',             # 07
        'ED6_DT29/CH14490 ._CH',             # 08
        'ED6_DT29/CH14491 ._CH',             # 09
        'ED6_DT29/CH14560 ._CH',             # 0A
        'ED6_DT29/CH14561 ._CH',             # 0B
        'ED6_DT29/CH14010 ._CH',             # 0C
        'ED6_DT29/CH14011 ._CH',             # 0D
        'ED6_DT26/CH20669 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT29/CH14470P._CP',             # 00
        'ED6_DT29/CH14471P._CP',             # 01
        'ED6_DT29/CH15050P._CP',             # 02
        'ED6_DT29/CH15051P._CP',             # 03
        'ED6_DT29/CH15060P._CP',             # 04
        'ED6_DT29/CH15061P._CP',             # 05
        'ED6_DT29/CH14480P._CP',             # 06
        'ED6_DT29/CH14481P._CP',             # 07
        'ED6_DT29/CH14490P._CP',             # 08
        'ED6_DT29/CH14491P._CP',             # 09
        'ED6_DT29/CH14560P._CP',             # 0A
        'ED6_DT29/CH14561P._CP',             # 0B
        'ED6_DT29/CH14010P._CP',             # 0C
        'ED6_DT29/CH14011P._CP',             # 0D
        'ED6_DT26/CH20669P._CP',             # 0E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -24160,
        Z                   = -6800,
        Y                   = -490,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24710,
        Z                   = -6800,
        Y                   = -300,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 57980,
        Z                   = -3200,
        Y                   = 39180,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21770,
        Z                   = -10800,
        Y                   = 86320,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21820,
        Z                   = -10800,
        Y                   = 101120,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x208,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -350,
        Z                   = -1600,
        Y                   = 73940,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31970,
        Z                   = -1650,
        Y                   = 43830,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x209,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3980,
        Y                   = -2200,
        Z                   = 99990,
        Range               = 4360,
        Unknown_10          = 0x898,
        Unknown_14          = 0x19294,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = -1600,
        TriggerY            = 111640,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = -300,
        ActorY              = 111640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -32000,
        TriggerZ            = -1650,
        TriggerY            = 40000,
        TriggerRange        = 1000,
        ActorX              = -32000,
        ActorZ              = -650,
        ActorY              = 40000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 58000,
        TriggerZ            = -7200,
        TriggerY            = 0,
        TriggerRange        = 1000,
        ActorX              = 58000,
        ActorZ              = -6200,
        ActorY              = 0,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 58000,
        TriggerZ            = -3200,
        TriggerY            = 45000,
        TriggerRange        = 1000,
        ActorX              = 58000,
        ActorZ              = -2200,
        ActorY              = 45000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_30D",          # 01, 1
        "Function_2_481",          # 02, 2
        "Function_3_5A7",          # 03, 3
        "Function_4_6CD",          # 04, 4
        "Function_5_7F3",          # 05, 5
        "Function_6_1130",         # 06, 6
        "Function_7_152D",         # 07, 7
        "Function_8_1CD2",         # 08, 8
        "Function_9_1DB0",         # 09, 9
        "Function_10_1E8E",        # 0A, 10
        "Function_11_1F6C",        # 0B, 11
        "Function_12_204A",        # 0C, 12
        "Function_13_2128",        # 0D, 13
        "Function_14_2206",        # 0E, 14
        "Function_15_22FF",        # 0F, 15
        "Function_16_23BB",        # 10, 16
        "Function_17_2477",        # 11, 17
        "Function_18_2533",        # 12, 18
        "Function_19_25EF",        # 13, 19
        "Function_20_26AB",        # 14, 20
        "Function_21_27C1",        # 15, 21
        "Function_22_280F",        # 16, 22
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30C")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2E2"),
        (101, "loc_2E9"),
        (102, "loc_2F0"),
        (103, "loc_2F7"),
        (104, "loc_2FE"),
        (105, "loc_305"),
        (SWITCH_DEFAULT, "loc_30C"),
    )


    label("loc_2E2")

    Event(0, 8)
    Jump("loc_30C")

    label("loc_2E9")

    Event(0, 9)
    Jump("loc_30C")

    label("loc_2F0")

    Event(0, 10)
    Jump("loc_30C")

    label("loc_2F7")

    Event(0, 11)
    Jump("loc_30C")

    label("loc_2FE")

    Event(0, 12)
    Jump("loc_30C")

    label("loc_305")

    Event(0, 13)
    Jump("loc_30C")

    label("loc_30C")

    Return()

    # Function_0_2B6 end

    def Function_1_30D(): pass

    label("Function_1_30D")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8CE8, 0x23008D)
    OP_1B(0x0, 0x0, 0xE)
    OP_1B(0x1, 0x0, 0xF)
    OP_1B(0x2, 0x0, 0x10)
    OP_1B(0x3, 0x0, 0x11)
    OP_1B(0x4, 0x0, 0x12)
    OP_1B(0x5, 0x0, 0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9")
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, 0, -300, 111640, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_3FD")

    label("loc_3F9")

    OP_64(0x0, 0x1)

    label("loc_3FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_410")
    OP_71(0x402, 0x0)
    ExitThread()
    Jump("loc_414")

    label("loc_410")

    Call(0, 22)

    label("loc_414")

    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_447")
    OP_6F(0x3, 0)
    Jump("loc_44E")

    label("loc_447")

    OP_6F(0x3, 60)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_460")
    OP_6F(0x4, 0)
    Jump("loc_467")

    label("loc_460")

    OP_6F(0x4, 60)

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_479")
    OP_6F(0x5, 0)
    Jump("loc_480")

    label("loc_479")

    OP_6F(0x5, 60)

    label("loc_480")

    Return()

    # Function_1_30D end

    def Function_2_481(): pass

    label("Function_2_481")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_566")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6C, 1)"), scpexpr(EXPR_END)), "loc_4F5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x6C\x00\x07\x00。\x02",
    )

    Jump("loc_4DA")

    label("loc_4DA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A90)
    Jump("loc_563")

    label("loc_4F5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x6C\x00\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6C\x00\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_544")

    label("loc_544")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_563")

    Jump("loc_599")

    label("loc_566")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_599")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_481 end

    def Function_3_5A7(): pass

    label("Function_3_5A7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_61B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_600")

    label("loc_600")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A91)
    Jump("loc_689")

    label("loc_61B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_66A")

    label("loc_66A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_689")

    Jump("loc_6BF")

    label("loc_68C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6BF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_5A7 end

    def Function_4_6CD(): pass

    label("Function_4_6CD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x552, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x16D, 1)"), scpexpr(EXPR_END)), "loc_741")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x6D\x01\x07\x00。\x02",
    )

    Jump("loc_726")

    label("loc_726")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2A92)
    Jump("loc_7AF")

    label("loc_741")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x6D\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x6D\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_790")

    label("loc_790")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_7AF")

    Jump("loc_7E5")

    label("loc_7B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7E5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_6CD end

    def Function_5_7F3(): pass

    label("Function_5_7F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_806")
    Call(0, 7)
    Return()

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 5)), scpexpr(EXPR_END)), "loc_80E")
    Return()

    label("loc_80E")

    EventBegin(0x0)
    OP_8C(0x0, 0, 0)
    OP_8C(0x1, 0, 0)
    OP_8C(0x2, 0, 0)
    OP_8C(0x3, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BB")

    label("loc_854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87C")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BB")

    label("loc_87C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A4")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BB")

    label("loc_8A4")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E3")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_94A")

    label("loc_8E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90B")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_94A")

    label("loc_90B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_933")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_94A")

    label("loc_933")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_94A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_972")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D9")

    label("loc_972")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D9")

    label("loc_99A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9D9")

    label("loc_9C2")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A01")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A68")

    label("loc_A01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A29")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A68")

    label("loc_A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A68")

    label("loc_A51")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A68")

    Sleep(1000)

    ChrTalk(    #9
        0x10F,
        "#1444F#6P那、那是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1004F#6P#4S！！\x02",
    )

    CloseMessageWindow()

    def lambda_AB2():
        OP_6D(-40, 1230, 122310, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_AB2)

    def lambda_ACA():
        OP_67(0, 1780, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_ACA)

    def lambda_AE2():
        OP_6B(5200, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_AE2)

    def lambda_AF2():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_AF2)

    def lambda_B02():
        OP_6E(240, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B02)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x2)
    SetChrPos(0x10F, 1310, -1200, 101560, 0)
    SetChrPos(0x101, 90, -1200, 101450, 0)
    SetChrPos(0xF0, 1680, -1200, 99810, 0)
    SetChrPos(0xF1, 110, -1200, 99700, 0)
    Sleep(500)

    ChrTalk(    #11
        0x101,
        "#1020F#5P『帕蒂尔·玛蒂尔』……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC4")

    ChrTalk(    #12
        0x10E,
        "#173F#5P那时的人形兵器……！\x02",
    )

    CloseMessageWindow()

    label("loc_BC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFC")

    ChrTalk(    #13
        0x104,
        "#1545F#5P呼……这东西也来了？\x02",
    )

    CloseMessageWindow()

    label("loc_BFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2E")

    ChrTalk(    #14
        0x103,
        "#1525F#5P这该怎么办……\x02",
    )

    CloseMessageWindow()

    label("loc_C2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C62")

    ChrTalk(    #15
        0x105,
        "#1163F#5P真是难以置信……\x02",
    )

    CloseMessageWindow()

    label("loc_C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(    #16
        0x10B,
        (
            "#216F#5P那个大家伙……\x01",
            "是那个小丫头所驾驶的人形兵器！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF2")

    ChrTalk(    #17
        0x106,
        (
            "#055F#5P喂喂……\x01",
            "是那个大块头啊！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2C")

    ChrTalk(    #18
        0x108,
        (
            "#072F#5P唔……\x01",
            "真是让人吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7D")

    ChrTalk(    #19
        0x10A,
        (
            "#1317F#5P那个机器……　\x01",
            "我好像在结社的研究所见过呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DB4")

    ChrTalk(    #20
        0x10D,
        "#270F#5P唔……好大的机器人。\x02",
    )

    CloseMessageWindow()

    label("loc_DB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFE")

    ChrTalk(    #21
        0x10C,
        (
            "#112F#5P就是那个在王都出现的\x01",
            "巨型人形兵器吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC8")

    ChrTalk(    #22
        0x107,
        (
            "#064F#5P为、为什么会在这儿……\x02\x03",

            "#065F那、那么……\x01",
            "那里的封印石就是……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x102,
        (
            "#1505F#5P啊啊，不会有错的。\x02\x03",

            "#1502F这还……\x01",
            "真是出乎预料啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F94")

    label("loc_EC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #24
        0x102,
        (
            "#1504F#5P为什么会在这里呢……\x02\x03",

            "#1502F也就是说那个封印石是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F94")

    label("loc_F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F94")

    ChrTalk(    #25
        0x107,
        (
            "#064F#5P为、为什么会在这儿……\x02\x03",

            "#065F那、那么……\x01",
            "那里的封印石就是……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F94")

    Sleep(300)
    Fade(500)
    OP_6D(-700, -1200, 107500, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(4110, 0)
    OP_6C(315000, 0)
    OP_6E(207, 0)
    SetChrPos(0x10F, 1310, -1200, 105560, 0)
    SetChrPos(0x101, 90, -1200, 105450, 0)
    SetChrPos(0xF0, 1680, -1200, 103810, 0)
    SetChrPos(0xF1, 110, -1200, 103700, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x10F,
        (
            "#1443F#6P看起来应该是\x01",
            "『噬身之蛇』的大型人形兵器……\x02\x03",

            "不过对你们来说\x01",
            "应该也是充满回忆的东西吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1007F#5P……嗯。\x01",
            "发生过一些事情吧。\x02\x03",

            "#1002F总之……\x01",
            "先把封印石拿到手再说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2A05)
    OP_28(0x36, 0x1, 0x2)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_5_7F3 end

    def Function_6_1130(): pass

    label("Function_6_1130")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-1000, -1430, 109500, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(4150, 0)
    OP_6C(218000, 0)
    OP_6E(207, 0)
    OP_6D(-1000, -1430, 109500, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(4150, 0)
    OP_6C(218000, 0)
    OP_6E(207, 0)
    SetChrPos(0x10F, 200, -1400, 108620, 0)
    SetChrPos(0x101, 0, -1600, 109740, 0)
    SetChrPos(0xF0, -1620, -1400, 108530, 45)
    SetChrPos(0xF1, 1800, -1200, 107910, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    OP_8E(0x101, 0x0, 0xFFFFF9C0, 0x1AF72, 0x3E8, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 14)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0xFFFFFFCE, 0xFFFFFDA8, 0x1B0D0, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x10, 0x80)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x00得到了\x1F\x5F\x03\x07\x00。\x02",
    )

    Jump("loc_12AC")

    label("loc_12AC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35F, 1)
    OP_64(0x0, 0x1)

    ChrTalk(    #29
        0x101,
        "#1025F#5P#40W………………………………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #30
        0x101,
        (
            "#1016F#5P#40W啊哈哈……\x01",
            "总算是找到了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1376")

    ChrTalk(    #31
        0x102,
        "#1514F#5P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_1376")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A9")

    ChrTalk(    #32
        0x107,
        "#560F#5P艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()

    label("loc_13A9")


    ChrTalk(    #33
        0x10F,
        (
            "#1447F#5P……看起来，\x01",
            "这是你一直在寻找的人吧。\x02\x03",

            "#1448F那我们马上回据点去\x01",
            "将其解放出来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #34
        0x101,
        (
            "#1025F#12P嗯……\x01",
            "谢谢你，莉丝小姐。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2A06)
    OP_28(0x36, 0x1, 0x4)
    OP_28(0x36, 0x1, 0x8)
    Sleep(500)
    OP_6D(200, -1600, 109620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 200, -1600, 109620, 0)
    SetChrPos(0x1, 200, -1600, 109620, 0)
    SetChrPos(0x2, 200, -1600, 109620, 0)
    SetChrPos(0x3, 200, -1600, 109620, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_1130 end

    def Function_7_152D(): pass

    label("Function_7_152D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_153D")
    Return()

    label("loc_153D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_154B")
    Return()

    label("loc_154B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x541, 0)), scpexpr(EXPR_END)), "loc_1553")
    Return()

    label("loc_1553")

    EventBegin(0x0)
    OP_8C(0x110, 0, 0)
    OP_62(0x110, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x110,
        "#1308F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_159A():
        OP_6D(100, -100, 133990, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_159A)

    def lambda_15B2():
        OP_67(0, 2770, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_15B2)

    def lambda_15CA():
        OP_6B(4400, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_15CA)

    def lambda_15DA():
        OP_6C(0, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_15DA)

    def lambda_15EA():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15EA)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10F, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-3980, -1200, 130900, 0)
    OP_67(0, 2600, -10000, 0)
    OP_6B(4990, 0)
    OP_6C(338000, 0)
    OP_6E(270, 0)
    SetChrPos(0x101, 940, -1200, 118140, 7)
    SetChrPos(0x10F, -1120, -1200, 118300, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_169A")
    SetChrPos(0x110, -320, -1200, 119490, 7)
    SetChrPos(0xF1, 80, -1200, 117080, 7)
    Jump("loc_16CA")

    label("loc_169A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16CA")
    SetChrPos(0x110, -320, -1200, 119490, 7)
    SetChrPos(0xF0, 80, -1200, 117080, 7)

    label("loc_16CA")

    OP_0D()
    Sleep(500)

    ChrTalk(    #36
        0x110,
        (
            "#1307F#5P帕蒂尔·玛蒂尔……\x02\x03",

            "喂……\x01",
            "你能听到玲的话吗？\x02",
        )
    )

    Jump("loc_1722")

    label("loc_1722")

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #37
        "\x07\x05\x18#2S#80W…………………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_62(0x110, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x110)
    Sleep(500)

    ChrTalk(    #38
        0x110,
        "#268F#5P……看来不行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1026F#5P玲……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_6D(-1240, -1200, 120760, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(326000, 0)
    OP_6E(270, 0)

    def lambda_1836():
        TurnDirection(0xFE, 0x110, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1836)

    def lambda_1844():
        TurnDirection(0xFE, 0x110, 0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_1844)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189F")

    ChrTalk(    #40
        0x107,
        (
            "#065F#6P是、是不是导力引擎\x01",
            "出现了异常故障……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_189F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E7")

    ChrTalk(    #41
        0x102,
        (
            "#1502F#6P果然……\x01",
            "导力引擎出了异常吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_18E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192C")

    ChrTalk(    #42
        0x10B,
        (
            "#212F#6P导力引擎\x01",
            "果然出现了异常吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_192C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1977")

    ChrTalk(    #43
        0x10E,
        (
            "#178F#6P应该是导力引擎\x01",
            "出现了异常情况吧……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_1977")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C0")

    ChrTalk(    #44
        0x10D,
        (
            "#270F#6P果然，导力引擎\x01",
            "也出现了异常吗……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19FA")

    label("loc_19C0")


    ChrTalk(    #45
        0x10F,
        (
            "#1802F#11P果然……\x01",
            "还是导力引擎的问题吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FA")


    ChrTalk(    #46
        0x110,
        (
            "#268F#5P……嗯，应该就是这样。\x02\x03",

            "#1300F是哪儿被破坏了呢，\x01",
            "还是被这个世界的力量\x01",
            "禁止了行动呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x110, 180, 400)
    Sleep(300)

    ChrTalk(    #47
        0x110,
        (
            "#263F#11P——算了。\x01",
            "现在就让它睡一会吧。\x02\x03",

            "#260F迟早我一定\x01",
            "会让它醒过来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10F,
        "#1444F#5P看来你很有把握嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x110,
        (
            "#261F#11P嘻嘻，那当然啦。\x02\x03",

            "#265F因为『帕蒂尔·玛蒂尔』——\x01",
            "是玲的爸爸和妈妈啊。\x02\x03",

            "每当玲遇到危机的时候，\x01",
            "它总是能够及时飞到我身边。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC8")

    ChrTalk(    #50
        0x102,
        "#1503F#6P玲……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF1")

    label("loc_1BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BF1")

    ChrTalk(    #51
        0x107,
        "#063F#6P玲……\x02",
    )

    CloseMessageWindow()

    label("loc_1BF1")


    ChrTalk(    #52
        0x10F,
        "#1445F#5P……这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1003F#6P…………………………………\x02\x03",

            "#1006F好吧。\x01",
            "那我们鼓足干劲继续前进吧。\x02\x03",

            "也许可以找到\x01",
            "让这家伙动起来的线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x110,
        "#261F#11P嘻嘻，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A08)
    OP_28(0x36, 0x1, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_7_152D end

    def Function_8_1CD2(): pass

    label("Function_8_1CD2")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -100, 370, 60, 0)
    SetChrPos(0x1, -100, 370, 60, 0)
    SetChrPos(0x2, -100, 370, 60, 0)
    SetChrPos(0x3, -100, 370, 60, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, 370, 60, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_8_1CD2 end

    def Function_9_1DB0(): pass

    label("Function_9_1DB0")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 210, 3700, 49810, 180)
    SetChrPos(0x1, 210, 3700, 49810, 180)
    SetChrPos(0x2, 210, 3700, 49810, 180)
    SetChrPos(0x3, 210, 3700, 49810, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 210, 3700, 49810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_9_1DB0 end

    def Function_10_1E8E(): pass

    label("Function_10_1E8E")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -49790, -7100, 25790, 180)
    SetChrPos(0x1, -49790, -7100, 25790, 180)
    SetChrPos(0x2, -49790, -7100, 25790, 180)
    SetChrPos(0x3, -49790, -7100, 25790, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -49790, -7100, 25790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_1E8E end

    def Function_11_1F6C(): pass

    label("Function_11_1F6C")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 160, -7100, -50290, 0)
    SetChrPos(0x1, 160, -7100, -50290, 0)
    SetChrPos(0x2, 160, -7100, -50290, 0)
    SetChrPos(0x3, 160, -7100, -50290, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 160, -7100, -50290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_1F6C end

    def Function_12_204A(): pass

    label("Function_12_204A")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -21940, -11150, 93890, 90)
    SetChrPos(0x1, -21940, -11150, 93890, 90)
    SetChrPos(0x2, -21940, -11150, 93890, 90)
    SetChrPos(0x3, -21940, -11150, 93890, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21940, -11150, 93890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_12_204A end

    def Function_13_2128(): pass

    label("Function_13_2128")

    OP_DE(0x0, 0x5, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 32159, -1550, 39880, 0)
    SetChrPos(0x1, 32159, -1550, 39880, 0)
    SetChrPos(0x2, 32159, -1550, 39880, 0)
    SetChrPos(0x3, 32159, -1550, 39880, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 32159, -1550, 39880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 20)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_2128 end

    def Function_14_2206(): pass

    label("Function_14_2206")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(-770, 370, -900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(5000, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x3, -100, 370, 60, 180)
    SetChrPos(0x2, -100, 370, 60, 180)
    SetChrPos(0x1, -100, 370, 60, 180)
    SetChrPos(0x0, -100, 370, 60, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -100, 370, 60, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7201   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_2206 end

    def Function_15_22FF(): pass

    label("Function_15_22FF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 210, 3700, 49810, 0)
    SetChrPos(0x2, 210, 3700, 49810, 0)
    SetChrPos(0x1, 210, 3700, 49810, 0)
    SetChrPos(0x0, 210, 3700, 49810, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 210, 3700, 49810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_22FF end

    def Function_16_23BB(): pass

    label("Function_16_23BB")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -49790, -7100, 25790, 0)
    SetChrPos(0x2, -49790, -7100, 25790, 0)
    SetChrPos(0x1, -49790, -7100, 25790, 0)
    SetChrPos(0x0, -49790, -7100, 25790, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -49790, -7100, 25790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_16_23BB end

    def Function_17_2477(): pass

    label("Function_17_2477")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 160, -7100, -50290, 180)
    SetChrPos(0x2, 160, -7100, -50290, 180)
    SetChrPos(0x1, 160, -7100, -50290, 180)
    SetChrPos(0x0, 160, -7100, -50290, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 160, -7100, -50290, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2477 end

    def Function_18_2533(): pass

    label("Function_18_2533")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -21940, -11150, 93890, 270)
    SetChrPos(0x2, -21940, -11150, 93890, 270)
    SetChrPos(0x1, -21940, -11150, 93890, 270)
    SetChrPos(0x0, -21940, -11150, 93890, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -21940, -11150, 93890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2533 end

    def Function_19_25EF(): pass

    label("Function_19_25EF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 32159, -1550, 39880, 180)
    SetChrPos(0x2, 32159, -1550, 39880, 180)
    SetChrPos(0x1, 32159, -1550, 39880, 180)
    SetChrPos(0x0, 32159, -1550, 39880, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 32159, -1550, 39880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 21)
    NewScene("ED6_DT21/M7203   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_19_25EF end

    def Function_20_26AB(): pass

    label("Function_20_26AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26D4")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_26C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26C8)

    label("loc_26D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26FD")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_26F1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_26F1)

    label("loc_26FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2726")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_271A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_271A)

    label("loc_2726")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274F")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2743():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2743)

    label("loc_274F")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_277B")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_277B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2792")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_2792")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27A9")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_27A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C0")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_27C0")

    Return()

    # Function_20_26AB end

    def Function_21_27C1(): pass

    label("Function_21_27C1")


    def lambda_27C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_27C7)

    def lambda_27D9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_27D9)

    def lambda_27EB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_27EB)

    def lambda_27FD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_27FD)
    Sleep(1000)
    Return()

    # Function_21_27C1 end

    def Function_22_280F(): pass

    label("Function_22_280F")

    OP_E5(0x0, 0x2, 0x0, 262144)
    OP_E5(0x0, 0x2, 0x1, 262144)
    OP_E5(0x0, 0x2, 0x2, 262144)
    OP_E5(0x0, 0x2, 0x3, 262144)
    OP_E5(0x0, 0x2, 0x4, 262144)
    OP_E5(0x0, 0x2, 0x5, 262144)
    OP_E5(0x0, 0x2, 0x6, 262144)
    OP_E5(0x0, 0x2, 0x7, 262144)
    OP_E5(0x0, 0x2, 0x8, 262144)
    OP_E5(0x0, 0x2, 0x9, 262144)
    OP_E5(0x0, 0x2, 0xA, 262144)
    OP_E5(0x0, 0x2, 0xB, 262144)
    OP_E5(0x0, 0x2, 0xC, 262144)
    OP_E5(0x0, 0x2, 0xD, 262144)
    OP_E5(0x0, 0x2, 0xE, 262144)
    OP_E5(0x0, 0x2, 0xF, 262144)
    OP_E5(0x0, 0x2, 0x10, 262144)
    OP_E5(0x0, 0x2, 0x11, 262144)
    OP_E5(0x0, 0x2, 0x12, 262144)
    OP_E5(0x0, 0x2, 0x13, 262144)
    OP_E5(0x0, 0x2, 0x14, 262144)
    OP_E5(0x0, 0x2, 0x15, 262144)
    OP_E5(0x0, 0x2, 0x16, 262144)
    OP_E5(0x0, 0x2, 0x17, 262144)
    OP_E5(0x0, 0x2, 0x18, 262144)
    OP_E5(0x0, 0x2, 0x19, 262144)
    OP_E5(0x0, 0x2, 0x1A, 262144)
    OP_E5(0x0, 0x2, 0x1B, 262144)
    OP_E5(0x0, 0x2, 0x1C, 262144)
    OP_E5(0x0, 0x2, 0x1D, 262144)
    OP_E5(0x0, 0x2, 0x1E, 262144)
    OP_E5(0x0, 0x2, 0x1F, 262144)
    OP_E5(0x0, 0x2, 0x20, 262144)
    OP_E5(0x0, 0x2, 0x21, 262144)
    OP_E5(0x0, 0x2, 0x22, 262144)
    OP_E5(0x0, 0x2, 0x23, 262144)
    OP_E5(0x0, 0x2, 0x24, 262144)
    OP_E5(0x0, 0x2, 0x25, 262144)
    OP_E5(0x0, 0x2, 0x26, 262144)
    OP_E5(0x0, 0x2, 0x27, 262144)
    OP_E5(0x0, 0x2, 0x28, 262144)
    OP_E5(0x0, 0x2, 0x29, 262144)
    OP_E5(0x0, 0x2, 0x2A, 262144)
    OP_E5(0x0, 0x2, 0x2B, 262144)
    OP_E5(0x0, 0x2, 0x2C, 262144)
    OP_E5(0x0, 0x2, 0x2D, 262144)
    OP_E5(0x0, 0x2, 0x2E, 262144)
    OP_E5(0x0, 0x2, 0x2F, 262144)
    OP_E5(0x0, 0x2, 0x30, 262144)
    OP_E5(0x0, 0x2, 0x31, 262144)
    OP_E5(0x0, 0x2, 0x32, 262144)
    OP_E5(0x0, 0x2, 0x33, 262144)
    OP_E5(0x0, 0x2, 0x34, 262144)
    OP_E5(0x0, 0x2, 0x35, 262144)
    OP_E5(0x0, 0x2, 0x36, 262144)
    OP_E5(0x0, 0x2, 0x37, 262144)
    OP_E5(0x0, 0x2, 0x38, 262144)
    OP_E5(0x0, 0x2, 0x39, 262144)
    OP_E5(0x0, 0x2, 0x3A, 262144)
    OP_E5(0x0, 0x2, 0x3B, 262144)
    OP_E5(0x0, 0x2, 0x3C, 262144)
    OP_E5(0x0, 0x2, 0x3D, 262144)
    OP_E5(0x0, 0x2, 0x3E, 262144)
    OP_E5(0x0, 0x2, 0x3F, 262144)
    OP_E5(0x0, 0x2, 0x40, 262144)
    OP_E5(0x0, 0x2, 0x41, 262144)
    OP_E5(0x0, 0x2, 0x42, 262144)
    OP_E5(0x0, 0x2, 0x43, 262144)
    OP_E5(0x0, 0x2, 0x44, 262144)
    OP_E5(0x0, 0x2, 0x45, 262144)
    OP_E5(0x0, 0x2, 0x46, 262144)
    OP_E5(0x0, 0x2, 0x47, 262144)
    OP_E5(0x0, 0x2, 0x48, 262144)
    OP_E5(0x0, 0x2, 0x49, 262144)
    OP_E5(0x0, 0x2, 0x4A, 262144)
    OP_E5(0x0, 0x2, 0x4B, 262144)
    OP_E5(0x0, 0x2, 0x4C, 262144)
    OP_E5(0x0, 0x2, 0x4D, 262144)
    OP_E5(0x0, 0x2, 0x4E, 262144)
    OP_E5(0x0, 0x2, 0x4F, 262144)
    OP_E5(0x0, 0x2, 0x50, 262144)
    OP_E5(0x0, 0x2, 0x51, 262144)
    OP_E5(0x0, 0x2, 0x52, 262144)
    OP_E5(0x0, 0x2, 0x53, 262144)
    OP_E5(0x0, 0x2, 0x54, 262144)
    OP_E5(0x0, 0x2, 0x55, 262144)
    OP_E5(0x0, 0x2, 0x56, 262144)
    OP_E5(0x0, 0x2, 0x57, 262144)
    OP_E5(0x0, 0x2, 0x58, 262144)
    OP_E5(0x0, 0x2, 0x59, 262144)
    OP_E5(0x0, 0x2, 0x5A, 262144)
    OP_E5(0x0, 0x2, 0x5B, 262144)
    OP_E5(0x0, 0x2, 0x5C, 262144)
    OP_E5(0x0, 0x2, 0x5D, 262144)
    OP_E5(0x0, 0x2, 0x5E, 262144)
    OP_E5(0x0, 0x2, 0x5F, 262144)
    OP_E5(0x0, 0x2, 0x60, 262144)
    OP_E5(0x0, 0x2, 0x61, 262144)
    OP_E5(0x0, 0x2, 0x62, 262144)
    OP_E5(0x0, 0x2, 0x63, 262144)
    OP_E5(0x0, 0x2, 0x64, 262144)
    OP_E5(0x0, 0x2, 0x65, 262144)
    OP_E5(0x0, 0x2, 0x66, 262144)
    OP_E5(0x0, 0x2, 0x67, 262144)
    OP_E5(0x0, 0x2, 0x68, 262144)
    OP_E5(0x0, 0x2, 0x69, 262144)
    OP_E5(0x0, 0x2, 0x6A, 262144)
    OP_E5(0x0, 0x2, 0x6B, 262144)
    OP_E5(0x0, 0x2, 0x6C, 262144)
    OP_E5(0x0, 0x2, 0x6D, 262144)
    OP_E5(0x0, 0x2, 0x6E, 262144)
    OP_E5(0x0, 0x2, 0x6F, 262144)
    OP_E5(0x0, 0x2, 0x70, 262144)
    OP_E5(0x0, 0x2, 0x71, 262144)
    OP_E5(0x0, 0x2, 0x72, 262144)
    OP_E5(0x0, 0x2, 0x73, 262144)
    OP_E5(0x0, 0x2, 0x74, 262144)
    OP_E5(0x0, 0x2, 0x75, 262144)
    OP_E5(0x0, 0x2, 0x76, 262144)
    OP_E5(0x0, 0x2, 0x77, 262144)
    OP_E5(0x0, 0x2, 0x78, 262144)
    OP_E5(0x0, 0x2, 0x79, 262144)
    OP_E5(0x0, 0x2, 0x7A, 262144)
    OP_E5(0x0, 0x2, 0x7B, 262144)
    OP_E5(0x0, 0x2, 0x7C, 262144)
    OP_E5(0x0, 0x2, 0x7D, 262144)
    OP_E5(0x0, 0x2, 0x7E, 262144)
    OP_E5(0x0, 0x2, 0x7F, 262144)
    OP_E5(0x0, 0x2, 0x80, 262144)
    OP_E5(0x0, 0x2, 0x81, 262144)
    OP_E5(0x0, 0x2, 0x82, 262144)
    OP_E5(0x0, 0x2, 0x83, 262144)
    OP_E5(0x0, 0x2, 0x84, 262144)
    OP_E5(0x0, 0x2, 0x85, 262144)
    OP_E5(0x0, 0x2, 0x86, 262144)
    OP_E5(0x0, 0x2, 0x87, 262144)
    OP_E5(0x0, 0x2, 0x88, 262144)
    OP_E5(0x0, 0x2, 0x89, 262144)
    OP_E5(0x0, 0x2, 0x8A, 262144)
    OP_E5(0x0, 0x2, 0x8B, 262144)
    OP_E5(0x0, 0x2, 0x8C, 262144)
    OP_E5(0x0, 0x2, 0x8D, 262144)
    OP_E5(0x0, 0x2, 0x8E, 262144)
    OP_E5(0x0, 0x2, 0x8F, 262144)
    OP_E5(0x0, 0x2, 0x90, 262144)
    OP_E5(0x0, 0x2, 0x91, 262144)
    OP_E5(0x0, 0x2, 0x92, 262144)
    OP_E5(0x0, 0x2, 0x93, 262144)
    OP_E5(0x0, 0x2, 0x94, 262144)
    OP_E5(0x0, 0x2, 0x95, 262144)
    OP_E5(0x0, 0x2, 0x96, 262144)
    OP_E5(0x0, 0x2, 0x97, 262144)
    OP_E5(0x0, 0x2, 0x98, 262144)
    OP_E5(0x0, 0x2, 0x99, 262144)
    OP_E5(0x0, 0x2, 0x9A, 262144)
    OP_E5(0x0, 0x2, 0x9B, 262144)
    OP_E5(0x0, 0x2, 0x9C, 262144)
    OP_E5(0x0, 0x2, 0x9D, 262144)
    OP_E5(0x0, 0x2, 0x9E, 262144)
    OP_E5(0x0, 0x2, 0x9F, 262144)
    OP_E5(0x0, 0x2, 0xA0, 262144)
    OP_E5(0x0, 0x2, 0xA1, 262144)
    OP_E5(0x0, 0x2, 0xA2, 262144)
    OP_E5(0x0, 0x2, 0xA3, 262144)
    OP_E5(0x0, 0x2, 0xA4, 262144)
    OP_E5(0x0, 0x2, 0xA5, 262144)
    OP_E5(0x0, 0x2, 0xA6, 262144)
    OP_E5(0x0, 0x2, 0xA7, 262144)
    OP_E5(0x0, 0x2, 0xA8, 262144)
    OP_E5(0x0, 0x2, 0xA9, 262144)
    OP_E5(0x0, 0x2, 0xAA, 262144)
    OP_E5(0x0, 0x2, 0xAB, 262144)
    OP_E5(0x0, 0x2, 0xAC, 262144)
    OP_E5(0x0, 0x2, 0xAD, 262144)
    OP_E5(0x0, 0x2, 0xAE, 262144)
    OP_E5(0x0, 0x2, 0xAF, 262144)
    OP_E5(0x0, 0x2, 0xB0, 262144)
    OP_E5(0x0, 0x2, 0xB1, 262144)
    OP_E5(0x0, 0x2, 0xB2, 262144)
    OP_E5(0x2, 0x2, 0x0, 800)
    OP_E5(0x2, 0x2, 0x1, 800)
    OP_E5(0x2, 0x2, 0x2, 800)
    OP_E5(0x2, 0x2, 0x3, 800)
    OP_E5(0x2, 0x2, 0x4, 800)
    OP_E5(0x2, 0x2, 0x5, 800)
    OP_E5(0x2, 0x2, 0x6, 800)
    OP_E5(0x2, 0x2, 0x7, 800)
    OP_E5(0x2, 0x2, 0x8, 800)
    OP_E5(0x2, 0x2, 0x9, 800)
    OP_E5(0x2, 0x2, 0xA, 800)
    OP_E5(0x2, 0x2, 0xB, 800)
    OP_E5(0x2, 0x2, 0xC, 800)
    OP_E5(0x2, 0x2, 0xD, 800)
    OP_E5(0x2, 0x2, 0xE, 800)
    OP_E5(0x2, 0x2, 0xF, 800)
    OP_E5(0x2, 0x2, 0x10, 800)
    OP_E5(0x2, 0x2, 0x11, 800)
    OP_E5(0x2, 0x2, 0x12, 800)
    OP_E5(0x2, 0x2, 0x13, 800)
    OP_E5(0x2, 0x2, 0x14, 800)
    OP_E5(0x2, 0x2, 0x15, 800)
    OP_E5(0x2, 0x2, 0x16, 800)
    OP_E5(0x2, 0x2, 0x17, 800)
    OP_E5(0x2, 0x2, 0x18, 800)
    OP_E5(0x2, 0x2, 0x19, 800)
    OP_E5(0x2, 0x2, 0x1A, 800)
    OP_E5(0x2, 0x2, 0x1B, 800)
    OP_E5(0x2, 0x2, 0x1C, 800)
    OP_E5(0x2, 0x2, 0x1D, 800)
    OP_E5(0x2, 0x2, 0x1E, 800)
    OP_E5(0x2, 0x2, 0x1F, 800)
    OP_E5(0x2, 0x2, 0x20, 800)
    OP_E5(0x2, 0x2, 0x21, 800)
    OP_E5(0x2, 0x2, 0x22, 800)
    OP_E5(0x2, 0x2, 0x23, 800)
    OP_E5(0x2, 0x2, 0x24, 800)
    OP_E5(0x2, 0x2, 0x25, 800)
    OP_E5(0x2, 0x2, 0x26, 800)
    OP_E5(0x2, 0x2, 0x27, 800)
    OP_E5(0x2, 0x2, 0x28, 800)
    OP_E5(0x2, 0x2, 0x29, 800)
    OP_E5(0x2, 0x2, 0x2A, 800)
    OP_E5(0x2, 0x2, 0x2B, 800)
    OP_E5(0x2, 0x2, 0x2C, 800)
    OP_E5(0x2, 0x2, 0x2D, 800)
    OP_E5(0x2, 0x2, 0x2E, 800)
    OP_E5(0x2, 0x2, 0x2F, 800)
    OP_E5(0x2, 0x2, 0x30, 800)
    OP_E5(0x2, 0x2, 0x31, 800)
    OP_E5(0x2, 0x2, 0x32, 800)
    OP_E5(0x2, 0x2, 0x33, 800)
    OP_E5(0x2, 0x2, 0x34, 800)
    OP_E5(0x2, 0x2, 0x35, 800)
    OP_E5(0x2, 0x2, 0x36, 800)
    OP_E5(0x2, 0x2, 0x37, 800)
    OP_E5(0x2, 0x2, 0x38, 800)
    OP_E5(0x2, 0x2, 0x39, 800)
    OP_E5(0x2, 0x2, 0x3A, 800)
    OP_E5(0x2, 0x2, 0x3B, 800)
    OP_E5(0x2, 0x2, 0x3C, 800)
    OP_E5(0x2, 0x2, 0x3D, 800)
    OP_E5(0x2, 0x2, 0x3E, 800)
    OP_E5(0x2, 0x2, 0x3F, 800)
    OP_E5(0x2, 0x2, 0x40, 800)
    OP_E5(0x2, 0x2, 0x41, 800)
    OP_E5(0x2, 0x2, 0x42, 800)
    OP_E5(0x2, 0x2, 0x43, 800)
    OP_E5(0x2, 0x2, 0x44, 800)
    OP_E5(0x2, 0x2, 0x45, 800)
    OP_E5(0x2, 0x2, 0x46, 800)
    OP_E5(0x2, 0x2, 0x47, 800)
    OP_E5(0x2, 0x2, 0x48, 800)
    OP_E5(0x2, 0x2, 0x49, 800)
    OP_E5(0x2, 0x2, 0x4A, 800)
    OP_E5(0x2, 0x2, 0x4B, 800)
    OP_E5(0x2, 0x2, 0x4C, 800)
    OP_E5(0x2, 0x2, 0x4D, 800)
    OP_E5(0x2, 0x2, 0x4E, 800)
    OP_E5(0x2, 0x2, 0x4F, 800)
    OP_E5(0x2, 0x2, 0x50, 800)
    OP_E5(0x2, 0x2, 0x51, 800)
    OP_E5(0x2, 0x2, 0x52, 800)
    OP_E5(0x2, 0x2, 0x53, 800)
    OP_E5(0x2, 0x2, 0x54, 800)
    OP_E5(0x2, 0x2, 0x55, 800)
    OP_E5(0x2, 0x2, 0x56, 800)
    OP_E5(0x2, 0x2, 0x57, 800)
    OP_E5(0x2, 0x2, 0x58, 800)
    OP_E5(0x2, 0x2, 0x59, 800)
    OP_E5(0x2, 0x2, 0x5A, 800)
    OP_E5(0x2, 0x2, 0x5B, 800)
    OP_E5(0x2, 0x2, 0x5C, 800)
    OP_E5(0x2, 0x2, 0x5D, 800)
    OP_E5(0x2, 0x2, 0x5E, 800)
    OP_E5(0x2, 0x2, 0x5F, 800)
    OP_E5(0x2, 0x2, 0x60, 800)
    OP_E5(0x2, 0x2, 0x61, 800)
    OP_E5(0x2, 0x2, 0x62, 800)
    OP_E5(0x2, 0x2, 0x63, 800)
    OP_E5(0x2, 0x2, 0x64, 800)
    OP_E5(0x2, 0x2, 0x65, 800)
    OP_E5(0x2, 0x2, 0x66, 800)
    OP_E5(0x2, 0x2, 0x67, 800)
    OP_E5(0x2, 0x2, 0x68, 800)
    OP_E5(0x2, 0x2, 0x69, 800)
    OP_E5(0x2, 0x2, 0x6A, 800)
    OP_E5(0x2, 0x2, 0x6B, 800)
    OP_E5(0x2, 0x2, 0x6C, 800)
    OP_E5(0x2, 0x2, 0x6D, 800)
    OP_E5(0x2, 0x2, 0x6E, 800)
    OP_E5(0x2, 0x2, 0x6F, 800)
    OP_E5(0x2, 0x2, 0x70, 800)
    OP_E5(0x2, 0x2, 0x71, 800)
    OP_E5(0x2, 0x2, 0x72, 800)
    OP_E5(0x2, 0x2, 0x73, 800)
    OP_E5(0x2, 0x2, 0x74, 800)
    OP_E5(0x2, 0x2, 0x75, 800)
    OP_E5(0x2, 0x2, 0x76, 800)
    OP_E5(0x2, 0x2, 0x77, 800)
    OP_E5(0x2, 0x2, 0x78, 800)
    OP_E5(0x2, 0x2, 0x79, 800)
    OP_E5(0x2, 0x2, 0x7A, 800)
    OP_E5(0x2, 0x2, 0x7B, 800)
    OP_E5(0x2, 0x2, 0x7C, 800)
    OP_E5(0x2, 0x2, 0x7D, 800)
    OP_E5(0x2, 0x2, 0x7E, 800)
    OP_E5(0x2, 0x2, 0x7F, 800)
    OP_E5(0x2, 0x2, 0x80, 800)
    OP_E5(0x2, 0x2, 0x81, 800)
    OP_E5(0x2, 0x2, 0x82, 800)
    OP_E5(0x2, 0x2, 0x83, 800)
    OP_E5(0x2, 0x2, 0x84, 800)
    OP_E5(0x2, 0x2, 0x85, 800)
    OP_E5(0x2, 0x2, 0x86, 800)
    OP_E5(0x2, 0x2, 0x87, 800)
    OP_E5(0x2, 0x2, 0x88, 800)
    OP_E5(0x2, 0x2, 0x89, 800)
    OP_E5(0x2, 0x2, 0x8A, 800)
    OP_E5(0x2, 0x2, 0x8B, 800)
    OP_E5(0x2, 0x2, 0x8C, 800)
    OP_E5(0x2, 0x2, 0x8D, 800)
    OP_E5(0x2, 0x2, 0x8E, 800)
    OP_E5(0x2, 0x2, 0x8F, 800)
    OP_E5(0x2, 0x2, 0x90, 800)
    OP_E5(0x2, 0x2, 0x91, 800)
    OP_E5(0x2, 0x2, 0x92, 800)
    OP_E5(0x2, 0x2, 0x93, 800)
    OP_E5(0x2, 0x2, 0x94, 800)
    OP_E5(0x2, 0x2, 0x95, 800)
    OP_E5(0x2, 0x2, 0x96, 800)
    OP_E5(0x2, 0x2, 0x97, 800)
    OP_E5(0x2, 0x2, 0x98, 800)
    OP_E5(0x2, 0x2, 0x99, 800)
    OP_E5(0x2, 0x2, 0x9A, 800)
    OP_E5(0x2, 0x2, 0x9B, 800)
    OP_E5(0x2, 0x2, 0x9C, 800)
    OP_E5(0x2, 0x2, 0x9D, 800)
    OP_E5(0x2, 0x2, 0x9E, 800)
    OP_E5(0x2, 0x2, 0x9F, 800)
    OP_E5(0x2, 0x2, 0xA0, 800)
    OP_E5(0x2, 0x2, 0xA1, 800)
    OP_E5(0x2, 0x2, 0xA2, 800)
    OP_E5(0x2, 0x2, 0xA3, 800)
    OP_E5(0x2, 0x2, 0xA4, 800)
    OP_E5(0x2, 0x2, 0xA5, 800)
    OP_E5(0x2, 0x2, 0xA6, 800)
    OP_E5(0x2, 0x2, 0xA7, 800)
    OP_E5(0x2, 0x2, 0xA8, 800)
    OP_E5(0x2, 0x2, 0xA9, 800)
    OP_E5(0x2, 0x2, 0xAA, 800)
    OP_E5(0x2, 0x2, 0xAB, 800)
    OP_E5(0x2, 0x2, 0xAC, 800)
    OP_E5(0x2, 0x2, 0xAD, 800)
    OP_E5(0x2, 0x2, 0xAE, 800)
    OP_E5(0x2, 0x2, 0xAF, 800)
    OP_E5(0x2, 0x2, 0xB0, 800)
    OP_E5(0x2, 0x2, 0xB1, 800)
    OP_E5(0x2, 0x2, 0xB2, 800)
    Return()

    # Function_22_280F end

    SaveToFile()

Try(main)
