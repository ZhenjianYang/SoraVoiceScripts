from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1400   ._SN',
        MapName             = 'Bose',
        Location            = 'R1400.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '柏斯方向',                             # 9
        '瓦雷利亚湖畔方向',                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
    )

    DeclNpc(
        X                   = -153950,
        Z                   = 0,
        Y                   = 68430,
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
        X                   = -140970,
        Z                   = -10,
        Y                   = -85530,
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
        X                   = -159990,
        Z                   = 0,
        Y                   = 15330,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -162450,
        Z                   = -30,
        Y                   = 220,
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
        X                   = -181290,
        Z                   = 50,
        Y                   = -41120,
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
        X                   = -147870,
        Z                   = 20,
        Y                   = -37440,
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
        X                   = -132980,
        Z                   = 0,
        Y                   = -60680,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x11A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -156160,
        TriggerZ            = 20,
        TriggerY            = -10160,
        TriggerRange        = 1000,
        ActorX              = -155470,
        ActorZ              = 20,
        ActorY              = -10210,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -166090,
        TriggerZ            = -220,
        TriggerY            = -6880,
        TriggerRange        = 1000,
        ActorX              = -166670,
        ActorZ              = -220,
        ActorY              = -6930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -151930,
        TriggerZ            = 360,
        TriggerY            = -34470,
        TriggerRange        = 1000,
        ActorX              = -151180,
        ActorZ              = 360,
        ActorY              = -34380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -160560,
        TriggerZ            = 0,
        TriggerY            = 35590,
        TriggerRange        = 1500,
        ActorX              = -160560,
        ActorZ              = 1500,
        ActorY              = 35590,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_276",          # 00, 0
        "Function_1_277",          # 01, 1
        "Function_2_2CA",          # 02, 2
        "Function_3_2E0",          # 03, 3
        "Function_4_3B9",          # 04, 4
        "Function_5_4D0",          # 05, 5
        "Function_6_5E7",          # 06, 6
    )


    def Function_0_276(): pass

    label("Function_0_276")

    Return()

    # Function_0_276 end

    def Function_1_277(): pass

    label("Function_1_277")

    OP_16(0x2, 0xFA0, 0xFFFB9EE8, 0xFFFDF878, 0x23001C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    OP_6F(0x1, 0)
    Jump("loc_2A2")

    label("loc_29B")

    OP_6F(0x1, 60)

    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4")
    OP_6F(0x2, 0)
    Jump("loc_2BB")

    label("loc_2B4")

    OP_6F(0x2, 60)

    label("loc_2BB")

    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    Return()

    # Function_1_277 end

    def Function_2_2CA(): pass

    label("Function_2_2CA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2CA")

    label("loc_2DF")

    Return()

    # Function_2_2CA end

    def Function_3_2E0(): pass

    label("Function_3_2E0")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#62I时之耀晶片×５０\x01",
            "\x07\x02#60I空之耀晶片×５０\x01",
            "\x07\x02#61I幻之耀晶片×５０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B40)
    Jump("loc_3A7")

    label("loc_38D")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3A7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2E0 end

    def Function_4_3B9(): pass

    label("Function_4_3B9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_491")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_428")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B42)
    Jump("loc_48E")

    label("loc_428")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_48E")

    Jump("loc_4C2")

    label("loc_491")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4C2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3B9 end

    def Function_5_4D0(): pass

    label("Function_5_4D0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x368, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_53F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B43)
    Jump("loc_5A5")

    label("loc_53F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_5A5")

    Jump("loc_5D9")

    label("loc_5A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5D9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_4D0 end

    def Function_6_5E7(): pass

    label("Function_6_5E7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #8
        (
            "\x07\x05北　柏斯市\x01",
            "南　瓦雷利亚湖畔　２００塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_5E7 end

    SaveToFile()

Try(main)
