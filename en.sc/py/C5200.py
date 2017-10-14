from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        "Function_4_57E",          # 04, 4
        "Function_5_6A2",          # 05, 5
        "Function_6_7C7",          # 06, 6
        "Function_7_90D",          # 07, 7
        "Function_8_A3E",          # 08, 8
        "Function_9_C18",          # 09, 9
        "Function_10_DA7",         # 0A, 10
        "Function_11_DEA",         # 0B, 11
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

    OP_EA(0x2, 0x9, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x13, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_462")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x02\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2300)
    Jump("loc_4C6")

    label("loc_462")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x02\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x02\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x13, 60)
    OP_70(0x13, 0x0)

    label("loc_4C6")

    Jump("loc_570")

    label("loc_4C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You nearly tear the top of the chest of its\x01",
            "hinges in your excitement to open it. Your face\x01",
            "falls as you realize there's nothing inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_570")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_3F1 end

    def Function_4_57E(): pass

    label("Function_4_57E")

    OP_EA(0x2, 0xA, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x14, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FF, 1)"), scpexpr(EXPR_END)), "loc_5EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\xFF\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2301)
    Jump("loc_653")

    label("loc_5EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\xFF\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFF\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x14, 60)
    OP_70(0x14, 0x0)

    label("loc_653")

    Jump("loc_694")

    label("loc_656")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Sorry, but I'm cutting you off.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_694")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_57E end

    def Function_5_6A2(): pass

    label("Function_5_6A2")

    OP_EA(0x2, 0xB, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x15, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_713")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2302)
    Jump("loc_777")

    label("loc_713")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x15, 60)
    OP_70(0x15, 0x0)

    label("loc_777")

    Jump("loc_7B9")

    label("loc_77A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Don't flip your lid...flip mine.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6A2 end

    def Function_6_7C7(): pass

    label("Function_6_7C7")

    OP_EA(0x2, 0xC, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8BE")
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
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2303)
    Jump("loc_8FB")

    label("loc_8BE")


    AnonymousTalk(    #10
        (
            "\x07\x05You look mighty familiar...\x01",
            "Didn't we meet last game?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_8FB")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7C7 end

    def Function_7_90D(): pass

    label("Function_7_90D")

    OP_EA(0x2, 0xD, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x297, 1)"), scpexpr(EXPR_END)), "loc_97E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "Found \x1F\x97\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2304)
    Jump("loc_9E2")

    label("loc_97E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "Found \x1F\x97\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x97\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_9E2")

    Jump("loc_A30")

    label("loc_9E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05Is this your way of asking me out on a date?\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A30")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_90D end

    def Function_8_A3E(): pass

    label("Function_8_A3E")

    OP_EA(0x2, 0xE, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B28")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_A95():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A95)

    def lambda_AB0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AB0)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #14
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x43D, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B03"),
        (2, "loc_B15"),
        (1, "loc_B25"),
        (SWITCH_DEFAULT, "loc_B28"),
    )


    label("loc_B03")

    OP_A2(0x2306)
    OP_6F(0x18, 60)
    Sleep(500)
    Jump("loc_B28")

    label("loc_B15")

    OP_6F(0x18, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_B25")

    OP_B4(0x0)
    Return()

    label("loc_B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xEF, 1)"), scpexpr(EXPR_END)), "loc_B74")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #15
        "Found \x1F\xEF\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2305)
    Jump("loc_BD6")

    label("loc_B74")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #16
        (
            "Found \x1F\xEF\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xEF\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_BD6")

    Jump("loc_C0A")

    label("loc_BD9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #17
        "\x07\x05THIS SPACE FOR RENT.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C0A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_A3E end

    def Function_9_C18(): pass

    label("Function_9_C18")

    OP_EA(0x2, 0xF, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x460, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x19, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A7, 1)"), scpexpr(EXPR_END)), "loc_C89")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #18
        "Found \x1F\xA7\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2307)
    Jump("loc_CED")

    label("loc_C89")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        (
            "Found \x1F\xA7\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA7\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x19, 60)
    OP_70(0x19, 0x0)

    label("loc_CED")

    Jump("loc_D99")

    label("loc_CF0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05As you reach into the chest, the lid suddenly\x01",
            "snaps down! IT'S EATING YOU ALIVE. ...Kidding!\x01",
            "Oh, you should've seen the look on your face!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D99")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_C18 end

    def Function_10_DA7(): pass

    label("Function_10_DA7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #21
        "\x07\x05The door is tightly locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_10_DA7 end

    def Function_11_DEA(): pass

    label("Function_11_DEA")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #22
        "\x07\x05Emergency Evacuation Route: Calmare ⇔ Axis Pillar \x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #23
        (
            "\x07\x05Automatically unlocks should any disruption occur in the\x01",
            "supply of orbal energy from the Axis Pillar.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #24
        (
            "\x07\x05Be advised, any obstructions in the vicinity of this gate\x01",
            "that might interfere with evacuation is a crime.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_11_DEA end

    SaveToFile()

Try(main)
