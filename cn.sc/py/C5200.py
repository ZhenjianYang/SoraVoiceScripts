from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5200   ._SN',
        MapName             = 'Other',
        Location            = 'C5200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60063",
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
        'ED6_DT29/CH12950 ._CH',             # 00
        'ED6_DT29/CH12951 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH12950P._CP',             # 00
        'ED6_DT29/CH12951P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
    )

    DeclNpc(
        X                   = 95050,
        Z                   = 7000,
        Y                   = -69760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -53380,
        Z                   = -4000,
        Y                   = 122950,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28750,
        Z                   = -4000,
        Y                   = 122990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 155140,
        Z                   = 0,
        Y                   = 23120,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 47170,
        Z                   = 0,
        Y                   = 58660,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 66780,
        Z                   = -2000,
        Y                   = -74110,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 88840,
        Z                   = 0,
        Y                   = -179320,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -70750,
        Z                   = 0,
        Y                   = -129720,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 59740,
        Z                   = 2000,
        Y                   = -63590,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 84410,
        Z                   = 2000,
        Y                   = -84740,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x43A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 53090,
        TriggerZ            = 0,
        TriggerY            = 206880,
        TriggerRange        = 800,
        ActorX              = 53490,
        ActorZ              = 1200,
        ActorY              = 206980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 49220,
        TriggerZ            = 0,
        TriggerY            = 207080,
        TriggerRange        = 800,
        ActorX              = 49220,
        ActorZ              = 1300,
        ActorY              = 207080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -119070,
        TriggerZ            = 0,
        TriggerY            = -112040,
        TriggerRange        = 1000,
        ActorX              = -119730,
        ActorZ              = 0,
        ActorY              = -112040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -119160,
        TriggerZ            = 0,
        TriggerY            = -162000,
        TriggerRange        = 1000,
        ActorX              = -119780,
        ActorZ              = 0,
        ActorY              = -162000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 36940,
        TriggerZ            = 0,
        TriggerY            = -242420,
        TriggerRange        = 1000,
        ActorX              = 36940,
        ActorZ              = 0,
        ActorY              = -243040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 88900,
        TriggerZ            = 0,
        TriggerY            = -240840,
        TriggerRange        = 1000,
        ActorX              = 88900,
        ActorZ              = 0,
        ActorY              = -241500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 96460,
        TriggerZ            = 0,
        TriggerY            = 23070,
        TriggerRange        = 1000,
        ActorX              = 97120,
        ActorZ              = 0,
        ActorY              = 23070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 95050,
        TriggerZ            = 6000,
        TriggerY            = -69050,
        TriggerRange        = 1000,
        ActorX              = 95050,
        ActorZ              = 6000,
        ActorY              = -69760,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 57620,
        TriggerZ            = 2000,
        TriggerY            = -61400,
        TriggerRange        = 1000,
        ActorX              = 57160,
        ActorZ              = 2000,
        ActorY              = -60930,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_32B",          # 01, 1
        "Function_2_3DB",          # 02, 2
        "Function_3_3F1",          # 03, 3
        "Function_4_508",          # 04, 4
        "Function_5_61F",          # 05, 5
        "Function_6_736",          # 06, 6
        "Function_7_889",          # 07, 7
        "Function_8_9A0",          # 08, 8
        "Function_9_B70",          # 09, 9
        "Function_10_C87",         # 0A, 10
        "Function_11_CBD",         # 0B, 11
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Return()

    # Function_0_32A end

    def Function_1_32B(): pass

    label("Function_1_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33D")
    OP_6F(0x13, 0)
    Jump("loc_344")

    label("loc_33D")

    OP_6F(0x13, 60)

    label("loc_344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356")
    OP_6F(0x14, 0)
    Jump("loc_35D")

    label("loc_356")

    OP_6F(0x14, 60)

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F")
    OP_6F(0x15, 0)
    Jump("loc_376")

    label("loc_36F")

    OP_6F(0x15, 60)

    label("loc_376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_388")
    OP_6F(0x16, 0)
    Jump("loc_38F")

    label("loc_388")

    OP_6F(0x16, 60)

    label("loc_38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1")
    OP_6F(0x17, 0)
    Jump("loc_3A8")

    label("loc_3A1")

    OP_6F(0x17, 60)

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA")
    OP_6F(0x18, 0)
    Jump("loc_3C1")

    label("loc_3BA")

    OP_6F(0x18, 60)

    label("loc_3C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3")
    OP_6F(0x19, 0)
    Jump("loc_3DA")

    label("loc_3D3")

    OP_6F(0x19, 60)

    label("loc_3DA")

    Return()

    # Function_1_32B end

    def Function_2_3DB(): pass

    label("Function_2_3DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3DB")

    label("loc_3F0")

    Return()

    # Function_2_3DB end

    def Function_3_3F1(): pass

    label("Function_3_3F1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_460")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2300)
    Jump("loc_4C6")

    label("loc_460")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_4C6")

    Jump("loc_4FA")

    label("loc_4C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4FA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3F1 end

    def Function_4_508(): pass

    label("Function_4_508")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x14, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_577")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFF\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2301)
    Jump("loc_5DD")

    label("loc_577")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFF\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFF\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x14, 60)
    OP_70(0x14, 0x0)

    label("loc_5DD")

    Jump("loc_611")

    label("loc_5E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_611")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_508 end

    def Function_5_61F(): pass

    label("Function_5_61F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_68E")
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
    OP_A2(0x2302)
    Jump("loc_6F4")

    label("loc_68E")

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
    OP_6F(0x15, 60)
    OP_70(0x15, 0x0)

    label("loc_6F4")

    Jump("loc_728")

    label("loc_6F7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_728")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_61F end

    def Function_6_736(): pass

    label("Function_6_736")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x16, 0x1E)
    OP_73(0x16)
    OP_6F(0x16, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    AddSepith(0x4, 0x64)
    AddSepith(0x5, 0x64)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x02#62I时之耀晶片×１００\x01",
            "\x07\x02#60I空之耀晶片×１００\x01",
            "\x07\x02#61I幻之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2303)
    Jump("loc_877")

    label("loc_85D")


    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_877")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_736 end

    def Function_7_889(): pass

    label("Function_7_889")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_961")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x297, 1)"), scpexpr(EXPR_END)), "loc_8F8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\x97\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2304)
    Jump("loc_95E")

    label("loc_8F8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\x97\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x97\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_95E")

    Jump("loc_992")

    label("loc_961")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_992")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_889 end

    def Function_8_9A0(): pass

    label("Function_8_9A0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B33")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7F")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_9F2():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9F2)

    def lambda_A0D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A0D)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #14
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x43D, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_A5A"),
        (2, "loc_A6C"),
        (1, "loc_A7C"),
        (SWITCH_DEFAULT, "loc_A7F"),
    )


    label("loc_A5A")

    OP_A2(0x2306)
    OP_6F(0x18, 60)
    Sleep(500)
    Jump("loc_A7F")

    label("loc_A6C")

    OP_6F(0x18, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_A7C")

    OP_B4(0x0)
    Return()

    label("loc_A7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xEF, 1)"), scpexpr(EXPR_END)), "loc_ACE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        "\x07\x00得到了\x1F\xEF\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2305)
    Jump("loc_B30")

    label("loc_ACE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #16
        (
            "宝箱里装有\x1F\xEF\x00\x07\x00。 \x01",
            "所持物品已经满了，\x1F\xEF\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_B30")

    Jump("loc_B62")

    label("loc_B33")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B62")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_9A0 end

    def Function_9_B70(): pass

    label("Function_9_B70")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C48")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A7, 1)"), scpexpr(EXPR_END)), "loc_BDF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "\x07\x00得到了\x1F\xA7\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2307)
    Jump("loc_C45")

    label("loc_BDF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "宝箱里装有\x1F\xA7\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA7\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x19, 60)
    OP_70(0x19, 0x0)

    label("loc_C45")

    Jump("loc_C79")

    label("loc_C48")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C79")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_B70 end

    def Function_10_C87(): pass

    label("Function_10_C87")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #21
        "\x07\x05门坚固地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_10_C87 end

    def Function_11_CBD(): pass

    label("Function_11_CBD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        (
            "\x07\x05【紧急避难通道】\x01",
            "卡尔玛丽≌ 中枢塔\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #23
        (
            "\x07\x05只有在来自『中枢塔』的\x01",
            "导力供给产生异常的情况下\x01",
            "才会自动解除锁定。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05此外，门附近\x01",
            "禁止放置会对避难\x01",
            "造成障碍的物体。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_11_CBD end

    SaveToFile()

Try(main)
