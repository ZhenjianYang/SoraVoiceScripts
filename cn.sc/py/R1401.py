from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1401   ._SN',
        MapName             = 'Bose',
        Location            = 'R1401.x',
        MapIndex            = 58,
        MapDefaultBGM       = "ed60029",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '柏斯方向',                             # 10
        '瓦雷利亚湖畔方向',                     # 11
        '琥珀之塔方向',                         # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
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
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10310 ._CH',             # 02
        'ED6_DT09/CH10311 ._CH',             # 03
        'ED6_DT09/CH10320 ._CH',             # 04
        'ED6_DT09/CH10321 ._CH',             # 05
        'ED6_DT09/CH10350 ._CH',             # 06
        'ED6_DT09/CH10351 ._CH',             # 07
        'ED6_DT09/CH10540 ._CH',             # 08
        'ED6_DT09/CH10541 ._CH',             # 09
        'ED6_DT09/CH10550 ._CH',             # 0A
        'ED6_DT09/CH10551 ._CH',             # 0B
        'ED6_DT09/CH10870 ._CH',             # 0C
        'ED6_DT09/CH10871 ._CH',             # 0D
        'ED6_DT09/CH10920 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10310P._CP',             # 02
        'ED6_DT09/CH10311P._CP',             # 03
        'ED6_DT09/CH10320P._CP',             # 04
        'ED6_DT09/CH10321P._CP',             # 05
        'ED6_DT09/CH10350P._CP',             # 06
        'ED6_DT09/CH10351P._CP',             # 07
        'ED6_DT09/CH10540P._CP',             # 08
        'ED6_DT09/CH10541P._CP',             # 09
        'ED6_DT09/CH10550P._CP',             # 0A
        'ED6_DT09/CH10551P._CP',             # 0B
        'ED6_DT09/CH10870P._CP',             # 0C
        'ED6_DT09/CH10871P._CP',             # 0D
        'ED6_DT09/CH10920P._CP',             # 0E
    )

    DeclNpc(
        X                   = -140750,
        Z                   = -10,
        Y                   = -203060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -141010,
        Z                   = -10,
        Y                   = -90880,
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
        X                   = -140930,
        Z                   = 230,
        Y                   = -255020,
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
        X                   = -218590,
        Z                   = -180,
        Y                   = -201180,
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


    DeclMonster(
        X                   = -145850,
        Z                   = -20,
        Y                   = -134350,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -139690,
        Z                   = 0,
        Y                   = -154320,
        Unknown_0C          = 0,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x120,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121830,
        Z                   = -20,
        Y                   = -180660,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x119,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -129880,
        Z                   = 0,
        Y                   = -195360,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162770,
        Z                   = -230,
        Y                   = -194700,
        Unknown_0C          = 0,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -189220,
        Z                   = -40,
        Y                   = -199700,
        Unknown_0C          = 0,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -128580,
        Z                   = 0,
        Y                   = -225570,
        Unknown_0C          = 0,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -117400,
        Z                   = -70,
        Y                   = -170080,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -140750,
        Y                   = -500,
        Z                   = -203060,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -144240,
        TriggerZ            = -190,
        TriggerY            = -129530,
        TriggerRange        = 1000,
        ActorX              = -144670,
        ActorZ              = -190,
        ActorY              = -129090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -164140,
        TriggerZ            = 20,
        TriggerY            = -201240,
        TriggerRange        = 1000,
        ActorX              = -163700,
        ActorZ              = 20,
        ActorY              = -201730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -191560,
        TriggerZ            = 0,
        TriggerY            = -195170,
        TriggerRange        = 1000,
        ActorX              = -191030,
        ActorZ              = 0,
        ActorY              = -195440,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -145200,
        TriggerZ            = 0,
        TriggerY            = -202770,
        TriggerRange        = 1500,
        ActorX              = -145200,
        ActorZ              = 1400,
        ActorY              = -202770,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -141090,
        TriggerZ            = 0,
        TriggerY            = -211150,
        TriggerRange        = 1500,
        ActorX              = -141090,
        ActorZ              = 1500,
        ActorY              = -211150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_356",          # 00, 0
        "Function_1_357",          # 01, 1
        "Function_2_3C5",          # 02, 2
        "Function_3_4DC",          # 03, 3
        "Function_4_5F3",          # 04, 4
        "Function_5_70A",          # 05, 5
        "Function_6_75C",          # 06, 6
        "Function_7_79F",          # 07, 7
    )


    def Function_0_356(): pass

    label("Function_0_356")

    Return()

    # Function_0_356 end

    def Function_1_357(): pass

    label("Function_1_357")

    OP_16(0x2, 0xFA0, 0xFFFBA2D0, 0xFFFB50C8, 0x23001D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B")
    OP_6F(0x0, 0)
    Jump("loc_382")

    label("loc_37B")

    OP_6F(0x0, 60)

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394")
    OP_6F(0x2, 0)
    Jump("loc_39B")

    label("loc_394")

    OP_6F(0x2, 60)

    label("loc_39B")

    OP_64(0x1, 0x1)
    OP_71(0x1, 0x0)
    OP_71(0x1, 0x4)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C4")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_3C4")

    Return()

    # Function_1_357 end

    def Function_2_3C5(): pass

    label("Function_2_3C5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_434")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B44)
    Jump("loc_49A")

    label("loc_434")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_49A")

    Jump("loc_4CE")

    label("loc_49D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3C5 end

    def Function_3_4DC(): pass

    label("Function_3_4DC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D5, 1)"), scpexpr(EXPR_END)), "loc_54B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xD5\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B45)
    Jump("loc_5B1")

    label("loc_54B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xD5\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD5\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_5B1")

    Jump("loc_5E5")

    label("loc_5B4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5E5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4DC end

    def Function_4_5F3(): pass

    label("Function_4_5F3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_662")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B46)
    Jump("loc_6C8")

    label("loc_662")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6C8")

    Jump("loc_6FC")

    label("loc_6CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5F3 end

    def Function_5_70A(): pass

    label("Function_5_70A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x05西　琥珀之塔\x01",
            "※魔兽很多，危险！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_5_70A end

    def Function_6_75C(): pass

    label("Function_6_75C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #10
        "\x07\x05南　瓦雷利亚湖畔\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_75C end

    def Function_7_79F(): pass

    label("Function_7_79F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 7)), scpexpr(EXPR_END)), "loc_7A7")
    Return()

    label("loc_7A7")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_88C"),
        (SWITCH_DEFAULT, "loc_8AF"),
    )


    label("loc_88C")

    Fade(500)
    OP_89(0x0, -133690, 0, -203000, 267)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_8AF")

    Battle(0xEEE, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -133690, 0, -203000, 267)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_8E8"),
        (1, "loc_8EB"),
        (SWITCH_DEFAULT, "loc_8EE"),
    )


    label("loc_8E8")

    EventEnd(0x0)
    Return()

    label("loc_8EB")

    OP_B4(0x0)
    Return()

    label("loc_8EE")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20F7)
    OP_28(0xB6, 0x4, 0x10)
    OP_28(0xB6, 0x4, 0x2)
    OP_28(0xB6, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_79F end

    SaveToFile()

Try(main)
