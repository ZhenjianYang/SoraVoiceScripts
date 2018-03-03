from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5500   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        'ED6_DT29/CH14540 ._CH',             # 00
        'ED6_DT29/CH14541 ._CH',             # 01
        'ED6_DT29/CH14860 ._CH',             # 02
        'ED6_DT29/CH14861 ._CH',             # 03
        'ED6_DT29/CH15000 ._CH',             # 04
        'ED6_DT29/CH15000 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14540P._CP',             # 00
        'ED6_DT29/CH14541P._CP',             # 01
        'ED6_DT29/CH14860P._CP',             # 02
        'ED6_DT29/CH14861P._CP',             # 03
        'ED6_DT29/CH15000P._CP',             # 04
        'ED6_DT29/CH15000P._CP',             # 05
    )

    DeclMonster(
        X                   = -33200,
        Z                   = 0,
        Y                   = 54880,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4400,
        Z                   = 0,
        Y                   = 53380,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -50400,
        Z                   = 0,
        Y                   = 61050,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x190,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -49910,
        Z                   = 0,
        Y                   = 99480,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x191,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -32900,
        TriggerZ            = 0,
        TriggerY            = 84900,
        TriggerRange        = 1700,
        ActorX              = -32900,
        ActorZ              = 2500,
        ActorY              = 84900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13900,
        TriggerZ            = 0,
        TriggerY            = 73100,
        TriggerRange        = 1700,
        ActorX              = -13900,
        ActorZ              = 2500,
        ActorY              = 73100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -50080,
        TriggerZ            = 0,
        TriggerY            = 52990,
        TriggerRange        = 1000,
        ActorX              = -49780,
        ActorZ              = 1000,
        ActorY              = 52490,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10560,
        TriggerZ            = 0,
        TriggerY            = 99890,
        TriggerRange        = 1000,
        ActorX              = -10560,
        ActorZ              = 1000,
        ActorY              = 99890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_1DB",          # 01, 1
        "Function_2_295",          # 02, 2
        "Function_3_40A",          # 03, 3
        "Function_4_536",          # 04, 4
        "Function_5_7E2",          # 05, 5
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Return()

    # Function_0_1DA end

    def Function_1_1DB(): pass

    label("Function_1_1DB")

    OP_22(0x85, 0x1, 0x4B)
    SetMapFlags(0x100000)
    OP_72(0x2800, 0x0)
    ExitThread()
    OP_72(0x2801, 0x0)
    ExitThread()
    OP_72(0x2802, 0x0)
    ExitThread()
    OP_72(0x2803, 0x0)
    ExitThread()
    OP_72(0x2804, 0x0)
    ExitThread()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 0)), scpexpr(EXPR_END)), "loc_211")
    OP_6F(0x1, 60)

    label("loc_211")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 1)), scpexpr(EXPR_END)), "loc_226")
    OP_6F(0x0, 120)
    OP_6F(0x1, 160)

    label("loc_226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 2)), scpexpr(EXPR_END)), "loc_23B")
    OP_6F(0x3, 120)
    OP_6F(0x4, 60)

    label("loc_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 3)), scpexpr(EXPR_END)), "loc_250")
    OP_6F(0x2, 120)
    OP_6F(0x4, 160)

    label("loc_250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262")
    OP_6F(0x7, 0)
    Jump("loc_269")

    label("loc_262")

    OP_6F(0x7, 60)

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B")
    OP_6F(0x8, 0)
    Jump("loc_282")

    label("loc_27B")

    OP_6F(0x8, 60)

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294")
    OP_64(0x2, 0x1)
    OP_71(0x407, 0x0)
    ExitThread()

    label("loc_294")

    Return()

    # Function_1_1DB end

    def Function_2_295(): pass

    label("Function_2_295")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x74, 1)"), scpexpr(EXPR_END)), "loc_303")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x74\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2983)
    Jump("loc_36B")

    label("loc_303")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x74\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x74\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)

    label("loc_36B")

    Jump("loc_3FC")

    label("loc_36E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Didn't Sunday school teach you not to steal? I bet you were one of those\x01",
            "kids who slept through lessons...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x69, 0x0)

    label("loc_3FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_295 end

    def Function_3_40A(): pass

    label("Function_3_40A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x530, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x196, 1)"), scpexpr(EXPR_END)), "loc_478")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x96\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2984)
    Jump("loc_4E0")

    label("loc_478")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x96\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x96\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_4E0")

    Jump("loc_528")

    label("loc_4E3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05I am content without my contents.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x6A, 0x0)

    label("loc_528")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_40A end

    def Function_4_536(): pass

    label("Function_4_536")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Push to the Right\x01",      # 0
            "Push to the Left\x01",       # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A0")
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x2960)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674")
    Sleep(500)
    LoadEffect(0x0, "craft\\\\cr162_02.eff")
    OP_6D(-50120, 0, 52390, 2000)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFF, -50080, 1000, 52390, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_72(0x407, 0x0)
    ExitThread()
    OP_A2(0x296F)
    OP_65(0x2, 0x1)
    Sleep(1500)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_69D")

    label("loc_674")

    Sleep(300)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Nothing happened.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_69D")

    Jump("loc_708")

    label("loc_6A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_708")
    OP_6F(0x1, 100)
    OP_70(0x1, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A2(0x2961)
    Sleep(500)
    OP_6D(-32340, -60, 91590, 1000)
    Sleep(300)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_708")

    Jump("loc_7DA")

    label("loc_70B")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 0)), scpexpr(EXPR_END)), "loc_778")
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    OP_A3(0x2960)
    Jump("loc_7DA")

    label("loc_778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 1)), scpexpr(EXPR_END)), "loc_7DA")
    OP_6F(0x1, 160)
    OP_70(0x1, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x1)
    Sleep(500)
    OP_6D(-32340, -60, 91590, 1000)
    Sleep(300)
    OP_6F(0x0, 120)
    OP_70(0x0, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x0)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    OP_A3(0x2961)

    label("loc_7DA")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_4_536 end

    def Function_5_7E2(): pass

    label("Function_5_7E2")

    EventBegin(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05There is a lever. Move it?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F0")

    Menu(
        0,
        10,
        100,
        1,
        (
            "Push to the Right\x01",      # 0
            "Push to the Left\x01",       # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AA")
    OP_6F(0x4, 0)
    OP_70(0x4, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2962)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Jump("loc_8E6")

    label("loc_8AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E6")
    OP_6F(0x4, 100)
    OP_70(0x4, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_A2(0x2963)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x2)

    label("loc_8E6")

    OP_69(0x0, 0x258)
    Jump("loc_9A9")

    label("loc_8F0")


    Menu(
        0,
        10,
        100,
        1,
        (
            "Return to Original Position\x01",      # 0
            "Cancel\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 2)), scpexpr(EXPR_END)), "loc_973")
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    OP_A3(0x2962)
    Jump("loc_9A9")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52C, 3)), scpexpr(EXPR_END)), "loc_9A9")
    OP_6F(0x4, 160)
    OP_70(0x4, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x4)
    OP_6F(0x2, 120)
    OP_70(0x2, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x2963)

    label("loc_9A9")

    EventEnd(0x1)
    SetMapFlags(0x100000)
    Return()

    # Function_5_7E2 end

    SaveToFile()

Try(main)
