from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1301   ._SN',
        MapName             = 'Bose',
        Location            = 'R1301.x',
        MapIndex            = 57,
        MapDefaultBGM       = "ed60022",
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
        '东柏斯街道方向',                       # 9
        '哈肯大门方向',                         # 10
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
        'ED6_DT09/CH10370 ._CH',             # 00
        'ED6_DT09/CH10371 ._CH',             # 01
        'ED6_DT09/CH10360 ._CH',             # 02
        'ED6_DT09/CH10361 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT09/CH10370P._CP',             # 00
        'ED6_DT09/CH10371P._CP',             # 01
        'ED6_DT09/CH10360P._CP',             # 02
        'ED6_DT09/CH10361P._CP',             # 03
    )

    DeclNpc(
        X                   = -204170,
        Z                   = 20,
        Y                   = 10080,
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
        X                   = -222100,
        Z                   = 10,
        Y                   = 149520,
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
        X                   = -215110,
        Z                   = 0,
        Y                   = 47900,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -212230,
        Z                   = 10,
        Y                   = 71070,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x105,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -214830,
        Z                   = -50,
        Y                   = 109950,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x106,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -220630,
        TriggerZ            = -190,
        TriggerY            = 85710,
        TriggerRange        = 1000,
        ActorX              = -221300,
        ActorZ              = -190,
        ActorY              = 85710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -203450,
        TriggerZ            = -30,
        TriggerY            = 57000,
        TriggerRange        = 1000,
        ActorX              = -202740,
        ActorZ              = -30,
        ActorY              = 57050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1A7",          # 01, 1
        "Function_2_1EC",          # 02, 2
        "Function_3_303",          # 03, 3
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Return()

    # Function_0_1A6 end

    def Function_1_1A7(): pass

    label("Function_1_1A7")

    OP_16(0x2, 0xFA0, 0xFFFACBF8, 0xFFFF63C0, 0x230014)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB")
    OP_6F(0x0, 0)
    Jump("loc_1D2")

    label("loc_1CB")

    OP_6F(0x0, 60)

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4")
    OP_6F(0x1, 0)
    Jump("loc_1EB")

    label("loc_1E4")

    OP_6F(0x1, 60)

    label("loc_1EB")

    Return()

    # Function_1_1A7 end

    def Function_2_1EC(): pass

    label("Function_2_1EC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3D4, 1)"), scpexpr(EXPR_END)), "loc_25B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xD4\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B12)
    Jump("loc_2C1")

    label("loc_25B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xD4\x03\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xD4\x03\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2C1")

    Jump("loc_2F5")

    label("loc_2C4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2F5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_1EC end

    def Function_3_303(): pass

    label("Function_3_303")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x362, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DB")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_372")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFC\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B13)
    Jump("loc_3D8")

    label("loc_372")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFC\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFC\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_3D8")

    Jump("loc_40C")

    label("loc_3DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_40C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_303 end

    SaveToFile()

Try(main)
