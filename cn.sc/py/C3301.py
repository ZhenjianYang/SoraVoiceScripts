from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3301   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT09/CH10630 ._CH',             # 00
        'ED6_DT09/CH10631 ._CH',             # 01
        'ED6_DT09/CH10640 ._CH',             # 02
        'ED6_DT09/CH10641 ._CH',             # 03
        'ED6_DT09/CH10650 ._CH',             # 04
        'ED6_DT09/CH10651 ._CH',             # 05
        'ED6_DT09/CH10660 ._CH',             # 06
        'ED6_DT09/CH10661 ._CH',             # 07
        'ED6_DT09/CH10670 ._CH',             # 08
        'ED6_DT09/CH10671 ._CH',             # 09
        'ED6_DT09/CH10680 ._CH',             # 0A
        'ED6_DT09/CH10681 ._CH',             # 0B
        'ED6_DT09/CH10690 ._CH',             # 0C
        'ED6_DT09/CH10691 ._CH',             # 0D
        'ED6_DT09/CH10700 ._CH',             # 0E
        'ED6_DT09/CH10701 ._CH',             # 0F
        'ED6_DT29/CH12420 ._CH',             # 10
        'ED6_DT29/CH12421 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT09/CH10630P._CP',             # 00
        'ED6_DT09/CH10631P._CP',             # 01
        'ED6_DT09/CH10640P._CP',             # 02
        'ED6_DT09/CH10641P._CP',             # 03
        'ED6_DT09/CH10650P._CP',             # 04
        'ED6_DT09/CH10651P._CP',             # 05
        'ED6_DT09/CH10660P._CP',             # 06
        'ED6_DT09/CH10661P._CP',             # 07
        'ED6_DT09/CH10670P._CP',             # 08
        'ED6_DT09/CH10671P._CP',             # 09
        'ED6_DT09/CH10680P._CP',             # 0A
        'ED6_DT09/CH10681P._CP',             # 0B
        'ED6_DT09/CH10690P._CP',             # 0C
        'ED6_DT09/CH10691P._CP',             # 0D
        'ED6_DT09/CH10700P._CP',             # 0E
        'ED6_DT09/CH10701P._CP',             # 0F
        'ED6_DT29/CH12420P._CP',             # 10
        'ED6_DT29/CH12421P._CP',             # 11
    )

    DeclMonster(
        X                   = 151480,
        Z                   = 10,
        Y                   = -36090,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 173520,
        Z                   = -30,
        Y                   = -9860,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 145980,
        Z                   = 0,
        Y                   = -16110,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 133740,
        Z                   = -10,
        Y                   = -17360,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100000,
        Z                   = 40,
        Y                   = -11970,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 103250,
        Z                   = 60,
        Y                   = -23320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 86210,
        Z                   = -10,
        Y                   = -27450,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E1,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 68170,
        Z                   = 20,
        Y                   = -25410,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 158010,
        TriggerZ            = 30,
        TriggerY            = -64629,
        TriggerRange        = 1000,
        ActorX              = 157660,
        ActorZ              = 1530,
        ActorY              = -65230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 140470,
        TriggerZ            = -30,
        TriggerY            = -11410,
        TriggerRange        = 1000,
        ActorX              = 140500,
        ActorZ              = 1470,
        ActorY              = -10700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 90610,
        TriggerZ            = 50,
        TriggerY            = -19930,
        TriggerRange        = 1000,
        ActorX              = 91210,
        ActorZ              = 1550,
        ActorY              = -19850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 97500,
        TriggerZ            = -20,
        TriggerY            = -18130,
        TriggerRange        = 1000,
        ActorX              = 96830,
        ActorZ              = 1480,
        ActorY              = -18060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2AA",          # 00, 0
        "Function_1_2AB",          # 01, 1
        "Function_2_315",          # 02, 2
        "Function_3_42C",          # 03, 3
        "Function_4_543",          # 04, 4
        "Function_5_65A",          # 05, 5
    )


    def Function_0_2AA(): pass

    label("Function_0_2AA")

    Return()

    # Function_0_2AA end

    def Function_1_2AB(): pass

    label("Function_1_2AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD")
    OP_6F(0x0, 0)
    Jump("loc_2C4")

    label("loc_2BD")

    OP_6F(0x0, 60)

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6")
    OP_6F(0x1, 0)
    Jump("loc_2DD")

    label("loc_2D6")

    OP_6F(0x1, 60)

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF")
    OP_6F(0x2, 0)
    Jump("loc_2F6")

    label("loc_2EF")

    OP_6F(0x2, 60)

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308")
    OP_6F(0x3, 0)
    Jump("loc_30F")

    label("loc_308")

    OP_6F(0x3, 60)

    label("loc_30F")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_2AB end

    def Function_2_315(): pass

    label("Function_2_315")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_384")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1531)
    Jump("loc_3EA")

    label("loc_384")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFE\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3EA")

    Jump("loc_41E")

    label("loc_3ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_41E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_315 end

    def Function_3_42C(): pass

    label("Function_3_42C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_504")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x134, 1)"), scpexpr(EXPR_END)), "loc_49B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x34\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1532)
    Jump("loc_501")

    label("loc_49B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x34\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x34\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_501")

    Jump("loc_535")

    label("loc_504")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_535")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_42C end

    def Function_4_543(): pass

    label("Function_4_543")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x152, 1)"), scpexpr(EXPR_END)), "loc_5B2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x52\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1534)
    Jump("loc_618")

    label("loc_5B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x52\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x52\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_618")

    Jump("loc_64C")

    label("loc_61B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_64C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_543 end

    def Function_5_65A(): pass

    label("Function_5_65A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_732")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_6C9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1536)
    Jump("loc_72F")

    label("loc_6C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_72F")

    Jump("loc_763")

    label("loc_732")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_763")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_65A end

    SaveToFile()

Try(main)
