from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5505   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5505.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60231",
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
        'Gilbert',                              # 9
        'Emotion Dummy',                        # 10
        'Wererat',                              # 11
        'Wererat',                              # 12
        'Wererat',                              # 13
        'Wererat',                              # 14
        'Wererat',                              # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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
        'ED6_DT27/CH03750 ._CH',             # 00
        'ED6_DT26/CH20445 ._CH',             # 01
        'ED6_DT26/CH20450 ._CH',             # 02
        'ED6_DT29/CH14540 ._CH',             # 03
        'ED6_DT29/CH14541 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT27/CH03750P._CP',             # 00
        'ED6_DT26/CH20445P._CP',             # 01
        'ED6_DT26/CH20450P._CP',             # 02
        'ED6_DT29/CH14540P._CP',             # 03
        'ED6_DT29/CH14541P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -11870,
        Z                   = 0,
        Y                   = -4340,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -31080,
        Z                   = 0,
        Y                   = 4130,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16430,
        Z                   = 0,
        Y                   = 29760,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3250,
        Z                   = 0,
        Y                   = -18980,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x198,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 18540,
        Y                   = -1000,
        Z                   = -11640,
        Range               = 23800,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xF50,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -30480,
        Y                   = -1000,
        Z                   = -29590,
        Range               = -13210,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF969C,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -9850,
        TriggerZ            = 0,
        TriggerY            = 2640,
        TriggerRange        = 1000,
        ActorX              = -9850,
        ActorZ              = 1000,
        ActorY              = 2640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -25140,
        TriggerZ            = 0,
        TriggerY            = 4380,
        TriggerRange        = 1000,
        ActorX              = -25140,
        ActorZ              = 1000,
        ActorY              = 4380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27020,
        TriggerZ            = 0,
        TriggerY            = 4360,
        TriggerRange        = 1000,
        ActorX              = -27020,
        ActorZ              = 1000,
        ActorY              = 4360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4930,
        TriggerZ            = 0,
        TriggerY            = -18050,
        TriggerRange        = 1000,
        ActorX              = 4930,
        ActorZ              = 1000,
        ActorY              = -18050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24270,
        TriggerZ            = 0,
        TriggerY            = 15620,
        TriggerRange        = 1000,
        ActorX              = -24350,
        ActorZ              = 3000,
        ActorY              = 14740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_316",          # 00, 0
        "Function_1_32A",          # 01, 1
        "Function_2_3BC",          # 02, 2
        "Function_3_4FE",          # 03, 3
        "Function_4_64C",          # 04, 4
        "Function_5_7A6",          # 05, 5
        "Function_6_8B1",          # 06, 6
        "Function_7_D5A",          # 07, 7
        "Function_8_D6B",          # 08, 8
        "Function_9_1726",         # 09, 9
        "Function_10_1763",        # 0A, 10
        "Function_11_1782",        # 0B, 11
        "Function_12_17A6",        # 0C, 12
        "Function_13_17CA",        # 0D, 13
        "Function_14_17EE",        # 0E, 14
        "Function_15_1812",        # 0F, 15
        "Function_16_1836",        # 10, 16
        "Function_17_185A",        # 11, 17
        "Function_18_187E",        # 12, 18
        "Function_19_18A2",        # 13, 19
        "Function_20_3268",        # 14, 20
        "Function_21_32AC",        # 15, 21
        "Function_22_3305",        # 16, 22
        "Function_23_34EA",        # 17, 23
        "Function_24_35A0",        # 18, 24
    )


    def Function_0_316(): pass

    label("Function_0_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_329")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_329")

    Return()

    # Function_0_316 end

    def Function_1_32A(): pass

    label("Function_1_32A")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x2300A2)
    OP_22(0x1CD, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353")
    OP_6F(0x2, 0)
    Jump("loc_35A")

    label("loc_353")

    OP_6F(0x2, 60)

    label("loc_35A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C")
    OP_6F(0x3, 0)
    Jump("loc_373")

    label("loc_36C")

    OP_6F(0x3, 60)

    label("loc_373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_385")
    OP_6F(0x4, 0)
    Jump("loc_38C")

    label("loc_385")

    OP_6F(0x4, 60)

    label("loc_38C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    OP_6F(0x5, 0)
    Jump("loc_3A5")

    label("loc_39E")

    OP_6F(0x5, 60)

    label("loc_3A5")

    OP_82(0x94, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3B8")
    OP_82(0x95, 0x0)
    Jump("loc_3BB")

    label("loc_3B8")

    OP_82(0x96, 0x0)

    label("loc_3BB")

    Return()

    # Function_1_32A end

    def Function_2_3BC(): pass

    label("Function_2_3BC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_495")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_42A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x02\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B0)
    Jump("loc_492")

    label("loc_42A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x02\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x02\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_492")

    Jump("loc_4F0")

    label("loc_495")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Not really sure what you expected from me. I'm a box...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x79, 0x0)

    label("loc_4F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3BC end

    def Function_3_4FE(): pass

    label("Function_3_4FE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2CB, 1)"), scpexpr(EXPR_END)), "loc_56C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xCB\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B1)
    Jump("loc_5D4")

    label("loc_56C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xCB\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xCB\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_5D4")

    Jump("loc_63E")

    label("loc_5D7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05This chest was made with state-of-the-art air freshener technology.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x7A, 0x0)

    label("loc_63E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_4FE end

    def Function_4_64C(): pass

    label("Function_4_64C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_725")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x4FD, 1)"), scpexpr(EXPR_END)), "loc_6BA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xFD\x04\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x29B2)
    Jump("loc_722")

    label("loc_6BA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xFD\x04\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x04\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_722")

    Jump("loc_798")

    label("loc_725")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05The first step towards beating kleptomania is admitting that there's a\x01",
            "problem.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x7B, 0x0)

    label("loc_798")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_64C end

    def Function_5_7A6(): pass

    label("Function_5_7A6")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x536, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_868")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x1E)
    OP_73(0x5)
    OP_6F(0x5, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)

    AnonymousTalk(    #9
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x100\x01",
            "#57IWater Sepith x100\x01",
            "#58IFire Sepith x100\x01",
            "#59IWind Sepith x100.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x29B3)
    Jump("loc_89A")

    label("loc_868")


    AnonymousTalk(    #10
        "\x07\x05Say, what year is this? I've lost count...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_89A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x7C, 0x0)
    Return()

    # Function_5_7A6 end

    def Function_6_8B1(): pass

    label("Function_6_8B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_END)), "loc_8B9")
    Return()

    label("loc_8B9")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8E")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 13600, 0, -1310, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Fade(500)
    OP_6C(225000, 0)
    OP_0D()
    Sleep(300)

    NpcTalk(    #11
        0x10,
        "Young Man's Voice",
        (
            "#1SS-Stay away!#2S\x02\x03",

            "#1SPlease, don't come any closer!#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AC")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A13")

    label("loc_9AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9D4")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A13")

    label("loc_9D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A13")

    label("loc_9FC")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A13")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A40")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AA7")

    label("loc_A40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AA7")

    label("loc_A68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A90")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AA7")

    label("loc_A90")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_AA7")

    Sleep(1000)

    def lambda_AB2():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB2)
    Sleep(100)

    def lambda_AC5():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC5)
    Sleep(100)

    def lambda_AD8():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_AD8)
    Sleep(100)
    TurnDirection(0xF0, 0x10, 400)

    ChrTalk(    #12
        0x102,
        "#1504F#5PThat sounds like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#5PYeah. It does.\x02\x03",

            "#1840FIt sounded like it was coming from over there.\x01",
            "Might as well go look.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x80)
    OP_A2(0x2907)
    OP_28(0x33, 0x1, 0x4)
    Sleep(300)
    Jump("loc_D3E")

    label("loc_B8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C15")

    ChrTalk(    #14
        0x109,
        (
            "#1063F(We better go check up on that voice we heard.)\x02\x03",

            "(The area it seemed to be coming from isn't far\x01",
            "from here.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3E")

    label("loc_C15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC3")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #15
        0x109,
        (
            "#1063FWe better go check up on that voice we heard.\x02\x03",

            "The area it seemed to be coming from isn't far\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3E")

    label("loc_CC3")

    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #16
        0x109,
        (
            "#1063FWe better go check up on that voice we heard.\x02\x03",

            "The area it seemed to be coming from isn't far\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3E")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_6_8B1 end

    def Function_7_D5A(): pass

    label("Function_7_D5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 0)), scpexpr(EXPR_END)), "loc_D62")
    Return()

    label("loc_D62")

    Call(0, 8)
    Call(0, 19)
    Return()

    # Function_7_D5A end

    def Function_8_D6B(): pass

    label("Function_8_D6B")

    EventBegin(0x0)
    OP_E0(238, 0x45, 0x2)
    OP_E0(238, 0x46, 0x3)
    OP_E0(239, 0x47, 0x2)
    OP_E0(239, 0x48, 0x3)
    OP_E0(240, 0x49, 0x2)
    OP_E0(240, 0x4A, 0x3)
    OP_E0(241, 0x4B, 0x2)
    OP_E0(241, 0x4C, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 42320, 1000, -6690, 270)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x800)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x12, 38210, 0, -5690, 90)
    SetChrPos(0x13, 39850, 0, -3470, 135)
    SetChrPos(0x14, 44470, 0, -4300, 225)
    SetChrPos(0x15, 43650, 0, -10050, 315)
    SetChrPos(0x16, 39470, 0, -9530, 0)

    def lambda_E3E():

        label("loc_E3E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E3E")

    QueueWorkItem2(0x12, 3, lambda_E3E)

    def lambda_E51():

        label("loc_E51")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E51")

    QueueWorkItem2(0x13, 3, lambda_E51)

    def lambda_E64():

        label("loc_E64")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E64")

    QueueWorkItem2(0x14, 3, lambda_E64)

    def lambda_E77():

        label("loc_E77")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E77")

    QueueWorkItem2(0x15, 3, lambda_E77)

    def lambda_E8A():

        label("loc_E8A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_E8A")

    QueueWorkItem2(0x16, 3, lambda_E8A)
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 7)), scpexpr(EXPR_END)), "loc_EC9")
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x0, 0x10, 400)
    Jump("loc_1178")

    label("loc_EC9")

    Fade(500)
    OP_6D(18700, 10, -6020, 0)
    OP_67(0, 8420, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0xEE, 18520, 0, -5690, 90)
    SetChrPos(0xEF, 18350, 0, -4260, 90)
    SetChrPos(0xF0, 17050, 0, -5550, 90)
    SetChrPos(0xF1, 16800, 0, -4000, 90)
    OP_0D()
    Sleep(300)

    NpcTalk(    #17
        0x10,
        "Young Man's Voice",
        (
            "S-Stay away!\x02\x03",

            "Please, don't come any closer!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF9")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1060")

    label("loc_FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1021")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1060")

    label("loc_1021")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1049")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1060")

    label("loc_1049")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1060")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108D")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10F4")

    label("loc_108D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10F4")

    label("loc_10B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DD")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10F4")

    label("loc_10DD")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_10F4")

    Sleep(500)

    def lambda_10FF():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10FF)
    Sleep(50)

    def lambda_1112():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1112)
    Sleep(50)

    def lambda_1125():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1125)
    Sleep(50)
    TurnDirection(0x3, 0x10, 400)

    ChrTalk(    #18
        0x102,
        "#1504F#6PThat sounds like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        "#1063F#5PYeah. It does.\x02",
    )

    CloseMessageWindow()

    label("loc_1178")


    def lambda_117E():
        OP_6D(43350, 0, -6810, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_117E)

    def lambda_1196():
        OP_67(0, 6670, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1196)

    def lambda_11AE():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11AE)

    def lambda_11BE():
        OP_6C(101000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_11BE)

    def lambda_11CE():
        OP_6E(255, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11CE)
    Sleep(2500)
    OP_1D(0xB4)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x109, 33500, 0, -4180, 90)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_43(0x10, 0x0, 0x0, 0x9)
    Sleep(500)

    ChrTalk(    #20
        0x10,
        (
            "#1224FI-I didn't mean any harm! I swear!\x02\x03",

            "I'll never do anything like that ever ever eeever again,\x01",
            "so please! Please spare my pitiful life!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)
    OP_22(0x194, 0x0, 0x64)
    Sleep(300)

    def lambda_12DC():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12DC)
    OP_43(0x12, 0x0, 0x0, 0xA)
    OP_43(0x13, 0x0, 0x0, 0xB)
    OP_43(0x14, 0x0, 0x0, 0xC)
    OP_43(0x15, 0x0, 0x0, 0xD)
    OP_43(0x16, 0x0, 0x0, 0xE)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #21
        0x109,
        (
            "#5P*sigh* The Goddess just loves bringing us together,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x10, 0x0)
    SetChrPos(0xEE, 25640, 670, -5350, 90)
    SetChrPos(0xEF, 25090, 60, -4120, 90)
    SetChrPos(0xF0, 23470, 500, -5000, 90)
    SetChrPos(0xF1, 22490, 0, -3200, 90)
    Fade(500)
    ClearMapFlags(0x10)
    SetChrPos(0x10, 42400, 900, -6550, 270)
    OP_6D(39000, 550, -7300, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(143000, 0)
    OP_6E(288, 0)
    OP_43(0x109, 0x0, 0x0, 0xF)
    OP_43(0x102, 0x0, 0x0, 0x10)
    OP_43(0xF0, 0x0, 0x0, 0x11)
    OP_43(0xF1, 0x0, 0x0, 0x12)
    Sleep(500)

    def lambda_1450():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1450)
    Sleep(50)

    def lambda_1463():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1463)
    Sleep(50)

    def lambda_1476():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_1476)
    Sleep(50)

    def lambda_1489():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1489)
    Sleep(50)
    OP_8C(0x16, 270, 400)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(300)

    ChrTalk(    #22
        0x10,
        "#1225F#5PI-I'm saved!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #23
        0x10,
        "#1227F#3S#5PMy saviors! Please, help me!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1512F#5P...Do we even have a choice?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        (
            "#1840F#11PI don't want his death on my conscience\x01",
            "any more than you do, so...no. Not really.\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_15B6():
        OP_6D(36580, 0, -7280, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_15B6)

    def lambda_15CE():
        OP_67(0, 8350, -10000, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_15CE)

    def lambda_15E6():
        OP_6B(2660, 400)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_15E6)

    def lambda_15F6():
        OP_6E(266, 400)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_15F6)
    SetChrChipByIndex(0x12, 4)

    def lambda_160B():

        label("loc_160B")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_160B")

    QueueWorkItem2(0x12, 3, lambda_160B)

    def lambda_161E():
        OP_8F(0xFE, 0x899E, 0x0, 0xFFFFE930, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_161E)
    Sleep(10)
    SetChrChipByIndex(0x15, 4)

    def lambda_1643():

        label("loc_1643")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_1643")

    QueueWorkItem2(0x15, 3, lambda_1643)

    def lambda_1656():
        OP_8F(0xFE, 0x88A4, 0x0, 0xFFFFE638, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1656)
    Sleep(15)
    SetChrChipByIndex(0x13, 4)

    def lambda_167B():

        label("loc_167B")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_167B")

    QueueWorkItem2(0x13, 3, lambda_167B)

    def lambda_168E():
        OP_8F(0xFE, 0x8B24, 0x0, 0xFFFFEB88, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_168E)
    Sleep(10)
    SetChrChipByIndex(0x14, 4)

    def lambda_16B3():

        label("loc_16B3")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_16B3")

    QueueWorkItem2(0x14, 3, lambda_16B3)

    def lambda_16C6():
        OP_8F(0xFE, 0x899E, 0x0, 0xFFFFE930, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_16C6)
    Sleep(15)
    SetChrChipByIndex(0x16, 4)

    def lambda_16EB():

        label("loc_16EB")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_16EB")

    QueueWorkItem2(0x16, 3, lambda_16EB)

    def lambda_16FE():
        OP_8F(0xFE, 0x88AE, 0x0, 0xFFFFE3FE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_16FE)
    WaitChrThread(0x109, 0x0)
    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_D6B end

    def Function_9_1726(): pass

    label("Function_9_1726")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1762")
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1000)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(1500)
    Jump("Function_9_1726")

    label("loc_1762")

    Return()

    # Function_9_1726 end

    def Function_10_1763(): pass

    label("Function_10_1763")

    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0x9C9A, 0x0, 0xFFFFE7DC, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_10_1763 end

    def Function_11_1782(): pass

    label("Function_11_1782")

    Sleep(100)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0xA096, 0x0, 0xFFFFEC8C, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_11_1782 end

    def Function_12_17A6(): pass

    label("Function_12_17A6")

    Sleep(120)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0xA8B6, 0x0, 0xFFFFEB74, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_12_17A6 end

    def Function_13_17CA(): pass

    label("Function_13_17CA")

    Sleep(30)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0xA7BC, 0x0, 0xFFFFDEB8, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_13_17CA end

    def Function_14_17EE(): pass

    label("Function_14_17EE")

    Sleep(60)
    SetChrChipByIndex(0xFE, 4)
    OP_8E(0xFE, 0x9F1A, 0x0, 0xFFFFE099, 0x3E8, 0x0)
    SetChrChipByIndex(0xFE, 3)
    Return()

    # Function_14_17EE end

    def Function_15_1812(): pass

    label("Function_15_1812")

    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x8426, 0x0, 0xFFFFE5FC, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_15_1812 end

    def Function_16_1836(): pass

    label("Function_16_1836")

    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x844E, 0x0, 0xFFFFEBB0, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_16_1836 end

    def Function_17_185A(): pass

    label("Function_17_185A")

    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x7E36, 0x0, 0xFFFFE638, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_17_185A end

    def Function_18_187E(): pass

    label("Function_18_187E")

    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    OP_8E(0xFE, 0x7DFA, 0x0, 0xFFFFEC8C, 0x1388, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_18_187E end

    def Function_19_18A2(): pass

    label("Function_19_18A2")

    EventBegin(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    SetChrPos(0xEE, 37940, 0, -6610, 90)
    SetChrPos(0xEF, 38210, 0, -5250, 90)
    SetChrPos(0xF0, 36330, 0, -6400, 90)
    SetChrPos(0xF1, 36670, 0, -4740, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 40920, 0, -6220, 270)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 40560, 0, -6340, 270)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_6D(39860, 0, -6820, 0)
    OP_67(0, 7450, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(135000, 0)
    OP_6E(292, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #26
        0x10,
        (
            "#1228F#5P*pant*...*pant*...\x02\x03",

            "Th-That was terrifying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1068F#12P*sigh* Aren't you supposed to be a part of\x01",
            "Ouroboros?\x02\x03",

            "#1063FHow do you keep getting yourself into these\x01",
            "messes?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrSubChip(0x10, 1)
    OP_0D()
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #28
        0x10,
        (
            "#1222F#5PYou are so rude!\x02\x03",

            "I didn't end up in this situation because of my\x01",
            "own error! It was the result of a tale so tragic,\x01",
            "anyone who heard it would be moved to tears!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1505F#6PI think there's a more pressing issue here,\x01",
            "to be honest.\x02\x03",

            "#1502FHow did you even get here ahead of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1079F#12PThat's a good question. Did you get through the\x01",
            "second and third plane's warp circles before us\x01",
            "somehow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1220F#5PHeh. After parting ways with you at the castle,\x01",
            "I found myself surrounded by armored knights.\x02\x03",

            "#1226FNaturally, I fought back with all the skill and \x01",
            "grace I'm known for, but during the fight,\x01",
            "I was engulfed in some kind of strange vortex.\x02\x03",

            "Next thing I knew, I was in front of a building\x01",
            "near a cliff.\x02\x03",

            "#1221FWhat a miracle! Clearly I have been chosen by\x01",
            "Aidios Herself to be the hero of a new story!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E41")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1EA8")

    label("loc_1E41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E69")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1EA8")

    label("loc_1E69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E91")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1EA8")

    label("loc_1E91")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1EA8")

    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EEC")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1F53")

    label("loc_1EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F14")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1F53")

    label("loc_1F14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3C")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_1F53")

    label("loc_1F3C")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_1F53")

    Sleep(1500)

    ChrTalk(    #32
        0x102,
        "#1508F#6P(Kevin, you think...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        (
            "#1068F#11P(Yeah. Sounds like he just ended up getting\x01",
            "drawn into one of those vortexes that pop up in\x01",
            "battle every so often and make things vanish.)\x02\x03",

            "#1840F(Damn, though. Ending up all the way here on the\x01",
            "fourth plane just because of that is some luck.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20B5")

    ChrTalk(    #34
        0x10B,
        "#413F#12P(*sigh* Seriously...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_20B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20EA")

    ChrTalk(    #35
        0x10A,
        "#819F#12P(Ahaha... Seriously.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_20EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(    #36
        0x104,
        "#1541F#12P(Heh. Truly.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_214E")

    ChrTalk(    #37
        0x108,
        "#573F#12P(You're telling me...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_214E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2179")

    ChrTalk(    #38
        0x105,
        "#1165F#12P(Truly...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_2179")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A7")

    ChrTalk(    #39
        0x10D,
        "#278F#12P(Heh. Indeed.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_21D6")

    label("loc_21A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D6")

    ChrTalk(    #40
        0x10E,
        "#179F#12P(*sigh* Indeed...)\x02",
    )

    CloseMessageWindow()

    label("loc_21D6")


    ChrTalk(    #41
        0x10,
        (
            "#1221F#5PLost for words, I see.\x02\x03",

            "#1226FNot that I can blame you for being in awe\x01",
            "of my good fortune.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1068F#12POh, we're in awe, all right... \x02\x03",

            "#1060FAnyway, you said you ended up in front of\x01",
            "the lodge... So how'd you end up all the way\x01",
            "out here?\x02\x03",

            "Did you decide to start looking around?\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #43
        0x10,
        "#1224F#5PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1504F#6PAnd this time, you're the one with the good\x01",
            "question.\x02\x03",

            "You were saying things like, 'I didn't mean any\x01",
            "harm,' and, 'I'll never do anything like that ever\x01",
            "again!' earlier... What was that about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1226F#5PHaha... Haha... Whatever do you mean?\x01",
            "I have absolute no ideee--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x160, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A0")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_24F8")

    label("loc_24A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C3")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_24F8")

    label("loc_24C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24E6")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_24F8")

    label("loc_24E6")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_24F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251B")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2573")

    label("loc_251B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_253E")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2573")

    label("loc_253E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2561")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2573")

    label("loc_2561")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_2573")

    Sleep(2000)
    OP_63(0x109)
    OP_63(0x102)
    OP_63(0xF0)
    OP_63(0xF1)
    OP_62(0x11, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #46
        0x10,
        (
            "#1224F#5PW-Will one of you SAY something?!\x02\x03",

            "That was merely the result of me being so\x01",
            "relieved to finally be out of mortal danger!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1841F#12PI think I know what happened now...\x02\x03",

            "#1840FYou were so hungry that you went and tried\x01",
            "to grab those beastmen's food, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#1224F#5PUh... Well...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_271D")

    ChrTalk(    #49
        0x107,
        (
            "#069F#12PP-Poor guy...\x02\x03",

            "We had no idea you were that desperate...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_271D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27A4")

    ChrTalk(    #50
        0x105,
        (
            "#1382F#12PUmm... I don't think you really have any reason\x01",
            "to feel ashamed, though.\x02\x03",

            "#1165FEveryone needs to eat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_281A")

    label("loc_27A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_281A")

    ChrTalk(    #51
        0x104,
        (
            "#1541F#12PYou have no reason to feel ashamed,\x01",
            "my man.\x02\x03",

            "#1540FEveryone needs food in order to live.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28CA")

    ChrTalk(    #52
        0x10B,
        (
            "#413F#12P*sigh* I can see where you were coming\x01",
            "from...\x02\x03",

            "#210F...but having no food and being tied up by\x01",
            "beastmen is even worse than just having\x01",
            "no food.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2964")

    label("loc_28CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2964")

    ChrTalk(    #53
        0x10E,
        (
            "#176F#12P*sigh* I can sympathize with your plight...\x02\x03",

            "#178F...but your careless actions only succeeded\x01",
            "in making your situation worse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29B3")

    ChrTalk(    #54
        0x108,
        "#075F#12PThat was pretty damn reckless of you, for sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FC")

    label("loc_29B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29FC")

    ChrTalk(    #55
        0x10D,
        "#272F#12PHmph. Sounds like you got what you deserved.\x02",
    )

    CloseMessageWindow()

    label("loc_29FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A70")

    ChrTalk(    #56
        0x10A,
        (
            "#1317F#12PU-Umm...\x02\x03",

            "#819FYou want a cookie? I've got a few of them\x01",
            "on me to snack on as it is...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A70")


    ChrTalk(    #57
        0x102,
        (
            "#1505F#6PErr... Gilbert...\x02\x03",

            "#1514FDo you want to come back to our base with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        (
            "#1840F#12PThat might be an idea.\x02\x03",

            "We've got plenty of food and water back there.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x10,
        "#1227F#5PS-Save your pity!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0xA3, 0x0, 0x64)
    Fade(250)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_2B7B():
        OP_96(0xFE, 0xA348, 0x0, 0xFFFFE778, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2B7B)
    WaitChrThread(0x10, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_0D()
    Sleep(300)

    ChrTalk(    #60
        0x10,
        (
            "#1225F#5PI was able to steal at least a month's worth of\x01",
            "food from them already!\x02\x03",

            "I'm not going to need any more for quite a while!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_2C37():
        OP_6D(33590, 0, -6230, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C37)

    def lambda_2C4F():
        OP_67(0, 7700, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C4F)

    def lambda_2C67():
        OP_6B(3050, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2C67)

    def lambda_2C77():
        OP_6C(225000, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C77)

    def lambda_2C87():
        OP_6E(267, 2500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2C87)
    OP_43(0x10, 0x0, 0x0, 0x14)

    def lambda_2C9E():

        label("loc_2C9E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2C9E")

    QueueWorkItem2(0x109, 0, lambda_2C9E)

    def lambda_2CAF():

        label("loc_2CAF")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2CAF")

    QueueWorkItem2(0x102, 0, lambda_2CAF)

    def lambda_2CC0():

        label("loc_2CC0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2CC0")

    QueueWorkItem2(0xF0, 0, lambda_2CC0)

    def lambda_2CD1():

        label("loc_2CD1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2CD1")

    QueueWorkItem2(0xF1, 0, lambda_2CD1)
    Sleep(3000)
    OP_44(0x109, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)

    def lambda_2CF7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CF7)

    def lambda_2D05():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D05)

    def lambda_2D13():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_2D13)

    def lambda_2D21():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_2D21)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #61
        0x10,
        (
            "#1221F#11PHeh. And it's all mine--and mine only!\x02\x03",

            "I won't give any of you so much as a crumb!\x02\x03",

            "#1226FHahaha! So long, losers!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)

    def lambda_2DC3():
        OP_6D(31450, 0, -6180, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DC3)

    def lambda_2DDB():
        OP_8E(0xFE, 0x1C02, 0x0, 0xFFFFF16E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2DDB)
    WaitChrThread(0x109, 0x0)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E34")
    OP_62(0xF0, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2E9B")

    label("loc_2E34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5C")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2E9B")

    label("loc_2E5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E84")
    OP_62(0xF0, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2E9B")

    label("loc_2E84")

    OP_62(0xF0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2E9B")

    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EDF")
    OP_62(0xF1, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2F46")

    label("loc_2EDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F07")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2F46")

    label("loc_2F07")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2F")
    OP_62(0xF1, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2F46")

    label("loc_2F2F")

    OP_62(0xF1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2F46")

    Sleep(1500)

    def lambda_2F51():
        OP_6D(35750, 0, -7170, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F51)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        (
            "#1068F#5P*sigh* He's incapable of listening, isn't he?\x02\x03",

            "#1840FIs he planning on staying here for over a month?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1505F#6PWho knows...? But all we can do is leave him to\x01",
            "his own devices for now if he doesn't want our\x01",
            "help.\x02\x03",

            "#1500FI wouldn't be surprised if he changed his mind.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(    #64
        0x107,
        "#067F#5PA-Ahaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_30B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30E2")

    ChrTalk(    #65
        0x10E,
        "#179F#5PHaha... Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_30E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_310D")

    ChrTalk(    #66
        0x10D,
        "#278F#5PHeh. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_310D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_313C")

    ChrTalk(    #67
        0x105,
        "#1165F#5PHeehee. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_313C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3168")

    ChrTalk(    #68
        0x108,
        "#070F#5PHaha... Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_3168")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31A4")

    ChrTalk(    #69
        0x104,
        "#1541F#5PHeh. That does sound likely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31E2")

    label("loc_31A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31E2")

    ChrTalk(    #70
        0x10A,
        "#819F#5PAhaha... That does sound possible.\x02",
    )

    CloseMessageWindow()

    label("loc_31E2")


    ChrTalk(    #71
        0x109,
        (
            "#1066F#5PHaha. We'll just have to be ready to give him\x01",
            "a warm welcome when he does, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2908)
    OP_28(0x33, 0x1, 0x8)
    OP_28(0x33, 0x1, 0x10)
    OP_28(0x33, 0x1, 0x20)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_19_18A2 end

    def Function_20_3268(): pass

    label("Function_20_3268")

    OP_8E(0xFE, 0x9D62, 0x0, 0xFFFFDDA0, 0x1B58, 0x0)
    OP_8E(0xFE, 0x8868, 0x0, 0xFFFFDD96, 0x1B58, 0x0)
    OP_8E(0xFE, 0x7B20, 0x0, 0xFFFFEDF4, 0x1B58, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_20_3268 end

    def Function_21_32AC(): pass

    label("Function_21_32AC")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        "\x07\x05Open the Door?\x18\x02",
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Return()

    # Function_21_32AC end

    def Function_22_3305(): pass

    label("Function_22_3305")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -25530, 0, 17040, 180)
    SetChrPos(0x1, -23780, 0, 17410, 180)
    SetChrPos(0x2, -25750, 0, 18940, 180)
    SetChrPos(0x3, -23820, 0, 19550, 180)
    OP_6D(-24210, 0, 16120, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(4310, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DB")
    OP_28(0x3, 0x4, 0x2)
    OP_82(0x95, 0x2)
    PlayEffect(0x96, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_33DB")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #73
        (
            "\x07\x05#40WBring to me the girl who shines like the sun,\x01",
            "and may the boy who cherishes that light be\x01",
            "at her side.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34DE")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34DB")
    Call(0, 23)

    label("loc_34DB")

    Jump("loc_34DE")

    label("loc_34DE")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_22_3305 end

    def Function_23_34EA(): pass

    label("Function_23_34EA")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    Sleep(500)

    def lambda_3553():
        OP_6B(3930, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3553)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_E3(0x0, 0x11, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_34EA end

    def Function_24_35A0(): pass

    label("Function_24_35A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -25530, 0, 17040, 180)
    SetChrPos(0x1, -23780, 0, 17410, 180)
    SetChrPos(0x2, -25750, 0, 18940, 180)
    SetChrPos(0x3, -23820, 0, 19550, 180)
    OP_6D(-24210, 0, 16120, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(4310, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_24_35A0 end

    SaveToFile()

Try(main)
