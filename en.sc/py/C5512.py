from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5512   ._SN',
        MapName             = 'Other',
        Location            = 'C5512.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C5511   ._SN',
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
        'ED6_DT27/CH04000 ._CH',             # 00
        'ED6_DT27/CH04001 ._CH',             # 01
        'ED6_DT07/CH00420 ._CH',             # 02
        'ED6_DT07/CH00421 ._CH',             # 03
        'ED6_DT29/CH12180 ._CH',             # 04
        'ED6_DT29/CH12181 ._CH',             # 05
        'ED6_DT29/CH12230 ._CH',             # 06
        'ED6_DT29/CH12231 ._CH',             # 07
        'ED6_DT29/CH12270 ._CH',             # 08
        'ED6_DT29/CH12271 ._CH',             # 09
        'ED6_DT29/CH12360 ._CH',             # 0A
        'ED6_DT29/CH12361 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT27/CH04000P._CP',             # 00
        'ED6_DT27/CH04001P._CP',             # 01
        'ED6_DT07/CH00420P._CP',             # 02
        'ED6_DT07/CH00421P._CP',             # 03
        'ED6_DT29/CH12180P._CP',             # 04
        'ED6_DT29/CH12181P._CP',             # 05
        'ED6_DT29/CH12230P._CP',             # 06
        'ED6_DT29/CH12231P._CP',             # 07
        'ED6_DT29/CH12270P._CP',             # 08
        'ED6_DT29/CH12271P._CP',             # 09
        'ED6_DT29/CH12360P._CP',             # 0A
        'ED6_DT29/CH12361P._CP',             # 0B
    )

    DeclMonster(
        X                   = -19850,
        Z                   = -4000,
        Y                   = -5550,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -23550,
        Z                   = -4000,
        Y                   = -23640,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -15630,
        Z                   = -4000,
        Y                   = 11180,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -19630,
        Z                   = -4000,
        Y                   = 33560,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30080,
        Z                   = 0,
        Y                   = 11750,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -55630,
        Z                   = 0,
        Y                   = 4340,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -46020,
        Z                   = 0,
        Y                   = -11250,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -51600,
        Y                   = -100,
        Z                   = 46300,
        Range               = -40600,
        Unknown_10          = 0x2A94,
        Unknown_14          = 0xDFD4,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    DeclActor(
        TriggerX            = -51110,
        TriggerZ            = 0,
        TriggerY            = 21930,
        TriggerRange        = 800,
        ActorX              = -51640,
        ActorZ              = 1000,
        ActorY              = 22460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24980,
        TriggerZ            = -4000,
        TriggerY            = 35970,
        TriggerRange        = 1000,
        ActorX              = -25600,
        ActorZ              = -4000,
        ActorY              = 36000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -50740,
        TriggerZ            = 1000,
        TriggerY            = 6930,
        TriggerRange        = 1000,
        ActorX              = -50040,
        ActorZ              = 1000,
        ActorY              = 6840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_269",          # 01, 1
        "Function_2_2BF",          # 02, 2
        "Function_3_2C4",          # 03, 3
        "Function_4_4F9",          # 04, 4
        "Function_5_6D2",          # 05, 5
        "Function_6_8D9",          # 06, 6
        "Function_7_A1D",          # 07, 7
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_268")
    OP_A3(0x10F0)
    Event(0, 4)

    label("loc_268")

    Return()

    # Function_0_25A end

    def Function_1_269(): pass

    label("Function_1_269")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1CD, 0x0, 0x64)
    OP_22(0x1CE, 0x1, 0x50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28C")
    OP_10(0x2, 0x0)

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29E")
    OP_6F(0x0, 0)
    Jump("loc_2A5")

    label("loc_29E")

    OP_6F(0x0, 60)

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B7")
    OP_6F(0x1, 0)
    Jump("loc_2BE")

    label("loc_2B7")

    OP_6F(0x1, 60)

    label("loc_2BE")

    Return()

    # Function_1_269 end

    def Function_2_2BF(): pass

    label("Function_2_2BF")

    Call(0, 3)
    Return()

    # Function_2_2BF end

    def Function_3_2C4(): pass

    label("Function_3_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_480")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-51390, 0, 21380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -51390, 0, 21380, 315)
    SetChrPos(0x10A, -50750, 0, 22020, 315)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05Saint-Croix Forest\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #1
        "\x07\x05Ranger and survival skills training grounds.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #2
        0x101,
        "#1004FHey, this sign...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10A,
        (
            "#811FLooks like a guidepost to me!\x02\x03",

            "#1310FWe passed by this way yesterday,\x01",
            "so I'm sure this is the way out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1006FAwesome! Now we can get out of the forest!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1010)
    OP_28(0x7F, 0x1, 0x1000)
    EventEnd(0x0)
    Jump("loc_4F8")

    label("loc_480")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "\x07\x05Saint-Croix Forest\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #6
        "\x07\x05Ranger and survival skills training grounds.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_4F8")

    Return()

    # Function_3_2C4 end

    def Function_4_4F9(): pass

    label("Function_4_4F9")

    EventBegin(0x0)
    OP_6D(-45960, 0, 42730, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -47410, 0, 40720, 184)
    SetChrPos(0x10A, -46250, 0, 42000, 184)

    def lambda_560():
        OP_8E(0x101, 0xFFFF46CE, 0x0, 0x670C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_560)

    def lambda_57B():
        OP_8E(0x10A, 0xFFFF4B56, 0x0, 0x6720, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_57B)

    def lambda_596():
        OP_6D(-46460, 0, 25850, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_596)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 500)
    WaitChrThread(0x10A, 0x1)
    OP_8C(0x10A, 270, 500)
    OP_8C(0x10A, 0, 500)
    WaitChrThread(0x101, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(    #7
        0x101,
        (
            "#1007FPhew! Looks like she isn't\x01",
            "going to chase us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#1316F#4PYeah, thank the Goddess...\x02\x03",

            "#812FShe's probably gonna join up\x01",
            "with the rest of her team so she\x01",
            "can have a real 'hunting party.'\x02\x03",

            "We need to take her down\x01",
            "as fast as we can!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_4F9 end

    def Function_5_6D2(): pass

    label("Function_5_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x202, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6DF")
    Return()

    label("loc_6DF")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-46840, 0, 47650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -47380, 0, 47720, 0)
    SetChrPos(0x10A, -45870, 0, 47720, 0)
    OP_0D()
    TurnDirection(0x10A, 0x101, 400)
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #9
        0x10A,
        (
            "#812FThat crazy jaeger lady is\x01",
            "probably still waiting for us.\x02\x03",

            "Estelle, you think we're ready?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Keep Preparing\x01",        # 0
            "Bash Her Face In\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_850")
    Fade(1000)
    SetChrPos(0x101, -46320, 0, 45210, 172)
    SetChrPos(0x10A, -46320, 0, 45210, 172)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_850")


    ChrTalk(    #10
        0x101,
        "#1002FOkay... Come on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10A,
        "#815FLet's bash her face in!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x10A, 2)

    def lambda_89E():
        OP_90(0x101, 0x0, 0x0, 0x2710, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_89E)
    Sleep(200)
    OP_90(0x10A, 0x0, 0x0, 0x2710, 0x1B58, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5507   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_6D2 end

    def Function_6_8D9(): pass

    label("Function_6_8D9")

    OP_EA(0x2, 0x9C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x19B, 1)"), scpexpr(EXPR_END)), "loc_94A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "Found \x1F\x9B\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1136)
    Jump("loc_9AE")

    label("loc_94A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "Found \x1F\x9B\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x9B\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_9AE")

    Jump("loc_A0F")

    label("loc_9B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "\x07\x05The chest is empty now. So empty. So lonely.\x01",
            "Please don't go...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A0F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_8D9 end

    def Function_7_A1D(): pass

    label("Function_7_A1D")

    OP_EA(0x2, 0x9D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x226, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A8E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1137)
    Jump("loc_AF2")

    label("loc_A8E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_AF2")

    Jump("loc_B2C")

    label("loc_AF5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05Sorry, kid. I'm retired.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B2C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_A1D end

    SaveToFile()

Try(main)
