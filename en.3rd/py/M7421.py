from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7421   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7421.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
        'Sleipnir',                             # 9
        'Rod Balloon',                          # 10
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
        'ED6_DT29/CH14610 ._CH',             # 00
        'ED6_DT29/CH14611 ._CH',             # 01
        'ED6_DT29/CH14040 ._CH',             # 02
        'ED6_DT29/CH14041 ._CH',             # 03
        'ED6_DT29/CH14880 ._CH',             # 04
        'ED6_DT29/CH14880 ._CH',             # 05
        'ED6_DT29/CH14890 ._CH',             # 06
        'ED6_DT29/CH14890 ._CH',             # 07
        'ED6_DT29/CH14840 ._CH',             # 08
        'ED6_DT29/CH14840 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH14610P._CP',             # 00
        'ED6_DT29/CH14611P._CP',             # 01
        'ED6_DT29/CH14040P._CP',             # 02
        'ED6_DT29/CH14041P._CP',             # 03
        'ED6_DT29/CH14880P._CP',             # 04
        'ED6_DT29/CH14880P._CP',             # 05
        'ED6_DT29/CH14890P._CP',             # 06
        'ED6_DT29/CH14890P._CP',             # 07
        'ED6_DT29/CH14840P._CP',             # 08
        'ED6_DT29/CH14840P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 130,
        Z                   = 4000,
        Y                   = 90130,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x326,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4190,
        Z                   = 0,
        Y                   = 191700,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -3910,
        Y                   = -1000,
        Z                   = -10300,
        Range               = 4260,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFE3FE,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 4000,
        TriggerY            = 88000,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 5000,
        ActorY              = 88000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2500,
        TriggerZ            = 4000,
        TriggerY            = 88000,
        TriggerRange        = 1000,
        ActorX              = -2500,
        ActorZ              = 5000,
        ActorY              = 88000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2500,
        TriggerZ            = 4000,
        TriggerY            = 88000,
        TriggerRange        = 1000,
        ActorX              = 2500,
        ActorZ              = 5000,
        ActorY              = 88000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2800,
        TriggerZ            = 0,
        TriggerY            = 229000,
        TriggerRange        = 1000,
        ActorX              = 2800,
        ActorZ              = 1000,
        ActorY              = 229000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2800,
        TriggerZ            = 0,
        TriggerY            = 229000,
        TriggerRange        = 1000,
        ActorX              = -2800,
        ActorZ              = 1000,
        ActorY              = 229000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_246",          # 00, 0
        "Function_1_2D1",          # 01, 1
        "Function_2_3D6",          # 02, 2
        "Function_3_54A",          # 03, 3
        "Function_4_5FC",          # 04, 4
        "Function_5_772",          # 05, 5
        "Function_6_89D",          # 06, 6
        "Function_7_9E6",          # 07, 7
        "Function_8_1030",         # 08, 8
        "Function_9_106D",         # 09, 9
    )


    def Function_0_246(): pass

    label("Function_0_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A4")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -180, 500, 850, 180)

    def lambda_26E():

        label("loc_26E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_26E")

    QueueWorkItem2(0x10, 3, lambda_26E)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1600, 2500, 440, 180)

    def lambda_297():

        label("loc_297")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_297")

    QueueWorkItem2(0x11, 3, lambda_297)

    label("loc_2A4")

    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_246 end

    def Function_1_2D1(): pass

    label("Function_1_2D1")

    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9")
    OP_6F(0x0, 0)
    Jump("loc_300")

    label("loc_2F9")

    OP_6F(0x0, 60)

    label("loc_300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312")
    OP_6F(0x1, 0)
    Jump("loc_319")

    label("loc_312")

    OP_6F(0x1, 60)

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B")
    OP_6F(0x2, 0)
    Jump("loc_332")

    label("loc_32B")

    OP_6F(0x2, 60)

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344")
    OP_6F(0x3, 0)
    Jump("loc_34B")

    label("loc_344")

    OP_6F(0x3, 60)

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D")
    OP_6F(0x4, 0)
    Jump("loc_364")

    label("loc_35D")

    OP_6F(0x4, 60)

    label("loc_364")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A5")
    OP_E5(0x0, 0xFF, 0x1, 1)
    OP_E5(0x0, 0xFF, 0x17, 1)
    OP_E5(0x0, 0xFF, 0x19, 1)
    OP_E5(0x1, 0xFF, 0x2, 1)
    OP_E5(0x1, 0xFF, 0x18, 1)
    OP_E5(0x1, 0xFF, 0x1A, 1)
    Jump("loc_3D5")

    label("loc_3A5")

    OP_E5(0x1, 0xFF, 0x1, 1)
    OP_E5(0x1, 0xFF, 0x17, 1)
    OP_E5(0x1, 0xFF, 0x19, 1)
    OP_E5(0x0, 0xFF, 0x2, 1)
    OP_E5(0x0, 0xFF, 0x18, 1)
    OP_E5(0x0, 0xFF, 0x1A, 1)

    label("loc_3D5")

    Return()

    # Function_1_2D1 end

    def Function_2_3D6(): pass

    label("Function_2_3D6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_444")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x06\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBC)
    Jump("loc_4AC")

    label("loc_444")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x06\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x06\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4AC")

    Jump("loc_53C")

    label("loc_4AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05The chest seems shy. You give it a modest pat-pat on the top of its lid,\x01",
            "then a quiet giggle in response.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_53C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_3D6 end

    def Function_3_54A(): pass

    label("Function_3_54A")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CBD)
    Jump("loc_5E5")

    label("loc_59B")


    AnonymousTalk(    #3
        "\x07\x05All the items here are pretty amazing, aren't they? Use them well.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5E5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_3_54A end

    def Function_4_5FC(): pass

    label("Function_4_5FC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x173, 1)"), scpexpr(EXPR_END)), "loc_66A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Found \x1F\x73\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBE)
    Jump("loc_6D2")

    label("loc_66A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Found \x1F\x73\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x73\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6D2")

    Jump("loc_764")

    label("loc_6D5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05The chest glares as if it wants to say, 'You got any special reason for\x01",
            "taking that? It's okay. I'll wait.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_764")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5FC end

    def Function_5_772(): pass

    label("Function_5_772")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_7E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Found \x1F\xF7\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBF)
    Jump("loc_848")

    label("loc_7E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05Found \x1F\xF7\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF7\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_848")

    Jump("loc_88F")

    label("loc_84B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05You're almost there! Keep going!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_88F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_772 end

    def Function_6_89D(): pass

    label("Function_6_89D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_976")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_90B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CBB)
    Jump("loc_973")

    label("loc_90B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_973")

    Jump("loc_9D8")

    label("loc_976")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05The chest presents to you an invitation to its birthday party.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_9D8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_89D end

    def Function_7_9E6(): pass

    label("Function_7_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 1)), scpexpr(EXPR_END)), "loc_9EE")
    Return()

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x586, 2)), scpexpr(EXPR_END)), "loc_AF0")
    EventBegin(0x0)
    Fade(500)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    SetChrPos(0x0, -580, 0, -9940, 0)
    SetChrPos(0x1, 780, 0, -10100, 0)
    SetChrPos(0x2, -1000, 0, -11770, 0)
    SetChrPos(0x3, 720, 0, -11820, 0)
    OP_6D(1500, 0, -4950, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2360, 0)
    OP_6C(45000, 0)
    OP_6E(426, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 10)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 11)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 12)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 13)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)
    Jump("loc_D30")

    label("loc_AF0")

    EventBegin(0x0)
    OP_E0(0, 0x4A, 0x2)
    OP_E0(1, 0x4B, 0x2)
    OP_E0(2, 0x4C, 0x2)
    OP_E0(3, 0x4D, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -180, 2500, 850, 180)

    def lambda_B22():

        label("loc_B22")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B22")

    QueueWorkItem2(0x10, 3, lambda_B22)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1600, 5500, 440, 180)

    def lambda_B56():

        label("loc_B56")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B56")

    QueueWorkItem2(0x11, 3, lambda_B56)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_B90():
        OP_6D(1980, 0, 2020, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B90)

    def lambda_BA8():
        OP_67(0, 4950, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BA8)

    def lambda_BC0():
        OP_6B(2390, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BC0)

    def lambda_BD0():
        OP_6E(436, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BD0)

    def lambda_BE0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_BE0)
    Sleep(100)

    def lambda_BF3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BF3)
    Sleep(100)

    def lambda_C06():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_C06)
    Sleep(100)
    OP_8C(0x3, 0, 400)
    WaitChrThread(0x0, 0x0)
    SetChrPos(0x0, -580, 0, -9940, 0)
    SetChrPos(0x1, 780, 0, -10100, 0)
    SetChrPos(0x2, -1000, 0, -11770, 0)
    SetChrPos(0x3, 720, 0, -11820, 0)
    OP_43(0x10, 0x0, 0x0, 0x8)
    OP_43(0x11, 0x0, 0x0, 0x9)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(1000)

    def lambda_C86():
        OP_6D(1500, 0, -4950, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_C86)

    def lambda_C9E():
        OP_67(0, 5520, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_C9E)

    def lambda_CB6():
        OP_6B(2360, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_CB6)

    def lambda_CC6():
        OP_6E(426, 1500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_CC6)
    WaitChrThread(0x0, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 10)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 11)
    SetChrSubChip(0x1, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 12)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 13)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)
    Sleep(500)

    label("loc_D30")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_D3F():
        OP_6D(1100, 0, -7600, 400)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_D3F)

    def lambda_D57():
        OP_67(0, 5640, -10000, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_D57)

    def lambda_D6F():
        OP_6B(1880, 400)
        ExitThread()

    QueueWorkItem(0x2, 3, lambda_D6F)

    def lambda_D7F():
        OP_6E(370, 400)
        ExitThread()

    QueueWorkItem(0x3, 3, lambda_D7F)
    SetChrChipByIndex(0x11, 3)

    def lambda_D94():
        OP_8F(0xFE, 0x96, 0x3E8, 0xFFFFD81E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_D94)

    def lambda_DAF():

        label("loc_DAF")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_DAF")

    QueueWorkItem2(0x11, 3, lambda_DAF)
    Sleep(50)
    SetChrChipByIndex(0x10, 1)

    def lambda_DCC():
        OP_8F(0xFE, 0x96, 0x1F4, 0xFFFFD81E, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_DCC)

    def lambda_DE7():

        label("loc_DE7")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_DE7")

    QueueWorkItem2(0x10, 3, lambda_DE7)
    WaitChrThread(0x0, 0x3)
    Battle(0x332, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E26"),
        (2, "loc_EF7"),
        (1, "loc_101A"),
        (SWITCH_DEFAULT, "loc_101F"),
    )


    label("loc_E26")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(50, 0, -6510, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, 50, 0, -6510, 0)
    SetChrPos(0x1, 50, 0, -6510, 0)
    SetChrPos(0x2, 50, 0, -6510, 0)
    SetChrPos(0x3, 50, 0, -6510, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C31)
    Jump("loc_101F")

    label("loc_EF7")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -180, 500, 850, 180)

    def lambda_F2E():

        label("loc_F2E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F2E")

    QueueWorkItem2(0x10, 3, lambda_F2E)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1600, 2500, 440, 180)

    def lambda_F57():

        label("loc_F57")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_F57")

    QueueWorkItem2(0x11, 3, lambda_F57)
    OP_6D(-30, 0, -11530, 0)
    OP_67(0, 6650, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(380, 0)
    SetChrPos(0x0, -30, 0, -11530, 0)
    SetChrPos(0x1, -30, 0, -11530, 0)
    SetChrPos(0x2, -30, 0, -11530, 0)
    SetChrPos(0x3, -30, 0, -11530, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2C32)
    Jump("loc_101F")

    label("loc_101A")

    OP_B4(0x0)
    Jump("loc_101F")

    label("loc_101F")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_9E6 end

    def Function_8_1030(): pass

    label("Function_8_1030")


    def lambda_1036():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1036)

    def lambda_1048():
        OP_8F(0xFE, 0xFFFFFF4C, 0x1F4, 0x352, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1048)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_8_1030 end

    def Function_9_106D(): pass

    label("Function_9_106D")


    def lambda_1073():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1073)

    def lambda_1085():
        OP_8F(0xFE, 0x640, 0x9C4, 0x1B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1085)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_9_106D end

    SaveToFile()

Try(main)
