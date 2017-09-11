from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0132   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0132.x',
        MapIndex            = 8,
        MapDefaultBGM       = "ed60010",
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
        'Verne',                                # 9
        'Girl in Uniform',                      # 10
        'Seagaro',                              # 11
        'Edel',                                 # 12
        'Target Camera',                        # 13
    )

    DeclEntryPoint(
        Unknown_00              = 6000,
        Unknown_04              = 0,
        Unknown_08              = 184000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 8,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 8000,
        Unknown_04              = 0,
        Unknown_08              = 181000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH02330 ._CH',             # 01
        'ED6_DT07/CH01040 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH02330P._CP',             # 01
        'ED6_DT07/CH01040P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190662,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -88400,
        Z                   = 0,
        Y                   = 155930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -48500,
        Z                   = 0,
        Y                   = 155890,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -44250,
        Z                   = 0,
        Y                   = 152480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 1000,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F6",          # 00, 0
        "Function_1_257",          # 01, 1
        "Function_2_282",          # 02, 2
        "Function_3_298",          # 03, 3
        "Function_4_2BC",          # 04, 4
        "Function_5_2E0",          # 05, 5
        "Function_6_334",          # 06, 6
        "Function_7_388",          # 07, 7
        "Function_8_3DC",          # 08, 8
        "Function_9_3E1",          # 09, 9
        "Function_10_1541",        # 0A, 10
        "Function_11_1887",        # 0B, 11
        "Function_12_19AD",        # 0C, 12
        "Function_13_1D96",        # 0D, 13
    )


    def Function_0_1F6(): pass

    label("Function_0_1F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20A")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_21B")

    label("loc_20A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21B")
    ClearChrFlags(0x9, 0x80)

    label("loc_21B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_225")
    Jump("loc_24A")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_239")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_24A")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_24A")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_256")
    ClearChrFlags(0x9, 0x10)

    label("loc_256")

    Return()

    # Function_0_1F6 end

    def Function_1_257(): pass

    label("Function_1_257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    OP_B1("t0132_y")
    Jump("loc_278")

    label("loc_26F")

    OP_B1("t0132_n")

    label("loc_278")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Return()

    # Function_1_257 end

    def Function_2_282(): pass

    label("Function_2_282")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_297")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_282")

    label("loc_297")

    Return()

    # Function_2_282 end

    def Function_3_298(): pass

    label("Function_3_298")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BB")
    OP_8D(0xFE, -86000, 151900, -82840, 154200, 3000)
    Jump("Function_3_298")

    label("loc_2BB")

    Return()

    # Function_3_298 end

    def Function_4_2BC(): pass

    label("Function_4_2BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF")
    OP_8D(0xFE, -46100, 153900, -42900, 151500, 3000)
    Jump("Function_4_2BC")

    label("loc_2DF")

    Return()

    # Function_4_2BC end

    def Function_5_2E0(): pass

    label("Function_5_2E0")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x3)
    Jump("loc_32E")

    label("loc_328")

    OP_82(0x80, 0x2)
    OP_A3(0x3)

    label("loc_32E")

    ClearMapFlags(0x80)
    Return()

    # Function_5_2E0 end

    def Function_6_334(): pass

    label("Function_6_334")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C")
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x4)
    Jump("loc_382")

    label("loc_37C")

    OP_82(0x81, 0x2)
    OP_A3(0x4)

    label("loc_382")

    ClearMapFlags(0x80)
    Return()

    # Function_6_334 end

    def Function_7_388(): pass

    label("Function_7_388")

    SetMapFlags(0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D0")
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A2(0x5)
    Jump("loc_3D6")

    label("loc_3D0")

    OP_82(0x82, 0x2)
    OP_A3(0x5)

    label("loc_3D6")

    ClearMapFlags(0x80)
    Return()

    # Function_7_388 end

    def Function_8_3DC(): pass

    label("Function_8_3DC")

    Call(0, 9)
    Return()

    # Function_8_3DC end

    def Function_9_3E1(): pass

    label("Function_9_3E1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_END)), "loc_459")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_448")
    OP_0D()
    OP_A9(0x3)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_448")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_459")
    TalkEnd(0x8)
    Return()

    label("loc_459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CD")
    OP_A2(0x0)

    ChrTalk(    #0
        0x8,
        "Oh...are you off to somewhere?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "It appears that all airliner flights\x01",
            "have been canceled, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#000FYep. That's why we're headed\x01",
            "to Bose on foot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#010FThere are some things we want\x01",
            "to investigate there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Ah, so this has something to\x01",
            "do with work, does it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "Forgive me for not being aware of\x01",
            "the situation. Have a safe trip.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_672")

    label("loc_5CD")


    ChrTalk(    #6
        0x8,
        (
            "A number of guests left for Bose\x01",
            "on foot this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "With the airliners not running, it's\x01",
            "been pretty inconvenient for people...\x01",
            "but most are making do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_672")

    Jump("loc_1538")

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_8DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86A")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)

    ChrTalk(    #8
        0x8,
        (
            "Estelle, Joshua, and even\x01",
            "Scherazard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Is something the matter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#002FDo you remember a girl named\x01",
            "Josette?\x02\x03",

            "#002FShe's a student from the Royal Academy\x01",
            "who should be staying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "Of course I remember her, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "She checked out just a moment ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        "#022FShoot, we're a minute too late.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        (
            "#012FLet's hurry to the landing port.\x01",
            "We might be able to catch her there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#007FShe really didn't seem like a\x01",
            "bad girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "???\x02",
    )

    CloseMessageWindow()
    OP_A2(0x262)
    OP_28(0x1B, 0x1, 0x4)
    OP_28(0x1B, 0x1, 0x8)
    EventEnd(0x1)
    Jump("loc_8DB")

    label("loc_86A")


    ChrTalk(    #17
        0x8,
        (
            "Ms. Josette checked out just\x01",
            "moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "She did appear to be in somewhat\x01",
            "of a rush if I might add...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DB")

    Jump("loc_1538")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A4")
    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        (
            "Estelle, Joshua, I heard about your\x01",
            "admirable performance at the farm\x01",
            "and the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "A number of guests have been\x01",
            "asking about you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "Keep up the good work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A19")

    label("loc_9A4")


    ChrTalk(    #22
        0x8,
        (
            "Estelle, Joshua, I heard about your\x01",
            "admirable performance at the farm\x01",
            "and the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        "Keep up the good work.\x02",
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_1538")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_AED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_END)), "loc_A95")

    ChrTalk(    #24
        0x8,
        (
            "It looks like you were able to make\x01",
            "contact with that reporter, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "Good luck with your job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AEA")

    label("loc_A95")


    ChrTalk(    #26
        0x8,
        (
            "How did things go? Were you able\x01",
            "to meet up with that reporter and\x01",
            "his partner?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEA")

    Jump("loc_1538")

    label("loc_AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 0)), scpexpr(EXPR_END)), "loc_E17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA5")
    EventBegin(0x0)
    OP_69(0x8, 0x3E8)
    OP_A2(0x251)
    OP_28(0x19, 0x1, 0x4)

    ChrTalk(    #27
        0x101,
        (
            "#000FVerne, I was wondering if I could\x01",
            "ask you something.\x02\x03",

            "#000FIs it true that the people from the\x01",
            "magazine company are staying here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "Well, you're certainly right\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "Did you have some business with\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#010FActually, we're here representing\x01",
            "the guild to cooperate with them\x01",
            "on getting a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        "Really? Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Then I regret to inform you that the\x01",
            "both of them are out at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#004FOh. Well, do you know where\x01",
            "they went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "That reporter fellow said something\x01",
            "about heading over to the bar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "How about you try asking there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#001FThe bar? Got it! Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        "#010FWe appreciate the help.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_E14")

    label("loc_DA5")


    ChrTalk(    #38
        0x8,
        (
            "That reporter fellow said something\x01",
            "about heading over to the bar...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        "How about you try asking there?\x02",
    )

    CloseMessageWindow()

    label("loc_E14")

    Jump("loc_1538")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_E9D")

    ChrTalk(    #40
        0x8,
        (
            "Today, we've got a reservation for\x01",
            "a magazine reporter from the\x01",
            "Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "He should be arriving any time\x01",
            "now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_F5A")

    ChrTalk(    #42
        0x8,
        (
            "Have you two ever met some of the other bracers\x01",
            "that have stayed here in this very hotel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "We often have bracers registered at\x01",
            "other branches dispatched here, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1075")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100E")
    OP_A2(0x0)

    ChrTalk(    #44
        0x8,
        (
            "Things have just settled down here\x01",
            "at the front desk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "We get a lot of guests coming in\x01",
            "and out of here when the airliners\x01",
            "are landing and departing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1072")

    label("loc_100E")


    ChrTalk(    #46
        0x8,
        (
            "We get a lot of guests coming in\x01",
            "and out of here when the airliners\x01",
            "are landing and departing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1072")

    Jump("loc_1538")

    label("loc_1075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_1192")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112C")
    OP_A2(0x0)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #47
        0x8,
        "Estelle, I heard the news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "It seems like you've finally become\x01",
            "a bracer, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "I'm praying for your success.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#501FOh, thanks...\x02",
    )

    CloseMessageWindow()
    Jump("loc_118F")

    label("loc_112C")


    ChrTalk(    #51
        0x8,
        (
            "It seems like you've finally become\x01",
            "a bracer, haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "I'm praying for your success.\x02",
    )

    CloseMessageWindow()

    label("loc_118F")

    Jump("loc_1538")

    label("loc_1192")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_12D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1259")
    OP_A2(0x0)

    ChrTalk(    #53
        0x8,
        (
            "We've got an unusual guest staying\x01",
            "here at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "She appears to be a student from\x01",
            "THE Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "I've heard she's come here to study\x01",
            "about Rolent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12D4")

    label("loc_1259")


    ChrTalk(    #56
        0x8,
        (
            "We've got an unusual guest staying\x01",
            "here at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "She appears to be a student from\x01",
            "THE Jenis Royal Academy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D4")

    Jump("loc_1538")

    label("loc_12D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #58
        0x8,
        "Welcome to the Hotel Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "Are you here to spend the night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#008FUh...Verne?\x01",
            "It's us, don't you remember?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #61
        0x8,
        (
            "Ha ha, I know.\x01",
            "I was just joking, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        "I was practicing my greeting just now.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #63
        0x101,
        "#008FOh, really...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 500)

    ChrTalk(    #64
        0x101,
        (
            "#007F(Did you ever notice that Verne teases people with a\x01",
            "straight face while being courteous at the same time?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        "#010F(That's probably because he can...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_1538")

    label("loc_149A")


    ChrTalk(    #66
        0x8,
        (
            "You know, Estelle, if you pass your exam, you'll be the\x01",
            "second female bracer here in Rolent after Scherazard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "Oh, and good luck to you too, Joshua.\x02",
    )

    CloseMessageWindow()

    label("loc_1538")

    OP_A2(0x229)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    # Function_9_3E1 end

    def Function_10_1541(): pass

    label("Function_10_1541")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15DF")
    OP_A2(0x1)

    NpcTalk(    #68
        0x9,
        "Josette",
        (
            "#217FWell, good afternoon, Estelle\x01",
            "and Joshua...\x02\x03",

            "Did you by any chance come for\x01",
            "a visit?\x02\x03",

            "Would you like a spot of tea?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1646")

    label("loc_15DF")


    NpcTalk(    #69
        0x9,
        "Josette",
        (
            "#217FWell, good afternoon, Estelle\x01",
            "and Joshua...\x02\x03",

            "Did you by any chance come for\x01",
            "a visit?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1646")

    Jump("loc_1883")

    label("loc_1649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_16AC")

    ChrTalk(    #70
        0x9,
        (
            "#217FI should be in the church right now,\x01",
            "so if you're reading this, this is a bug.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1883")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_16FF")

    ChrTalk(    #71
        0x9,
        (
            "Let's see, first I'll need to make an\x01",
            "appointment with the mayor...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1883")

    label("loc_16FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_179D")

    ChrTalk(    #72
        0x9,
        (
            "The mayor's residence is east of\x01",
            "town...and the Bracer Guild is\x01",
            "south of the clock tower.\x02\x03",

            "I think I've got the basic layout\x01",
            "of this town now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1883")

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_1817")

    ChrTalk(    #73
        0x9,
        (
            "Whew, I've finally arrived here\x01",
            "in Rolent.\x02\x03",

            "I think the first thing I'm going to\x01",
            "do is have a look around.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1883")

    label("loc_1817")


    ChrTalk(    #74
        0x9,
        (
            "#217FI'm not supposed to have arrived \x01",
            "in Rolent just yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        "#217FSo pretend we never met...okay?\x02",
    )

    CloseMessageWindow()

    label("loc_1883")

    TalkEnd(0x9)
    Return()

    # Function_10_1541 end

    def Function_11_1887(): pass

    label("Function_11_1887")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1939")

    ChrTalk(    #76
        0xFE,
        (
            "We're scheduled to head to\x01",
            "Bose on the next airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "It looks like there have been a\x01",
            "number of incidents going on in\x01",
            "Bose recently, so I'm a bit worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A9")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_19A9")

    ChrTalk(    #78
        0xFE,
        (
            "Though we came here on a pilgrimage,\x01",
            "Rolent has a wonderful locale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "I think I like this place.\x02",
    )

    CloseMessageWindow()

    label("loc_19A9")

    TalkEnd(0xA)
    Return()

    # Function_11_1887 end

    def Function_12_19AD(): pass

    label("Function_12_19AD")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4F")
    OP_A2(0x2)

    ChrTalk(    #80
        0xFE,
        "Next is the Bose region for us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Speaking of Bose, the Bose Market\x01",
            "is what I'm most looking forward to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I hear there are a lot of rare items\x01",
            "from the Empire displayed in the\x01",
            "stores.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "I've been stashing money away in\x01",
            "anticipation of this day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Preparation is a go, shopping spirit\x01",
            "is a go, and loads of money in the\x01",
            "wallet is a GOOOO!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Onward to the Bose Market we go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BD5")

    label("loc_1B4F")


    ChrTalk(    #86
        0xFE,
        (
            "Preparation is a go, shopping spirit\x01",
            "is a go, and loads of money in the\x01",
            "wallet is a GOOOO!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Onward to the Bose Market we go!\x02",
    )

    CloseMessageWindow()

    label("loc_1BD5")

    Jump("loc_1D92")

    label("loc_1BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1D92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE9")
    OP_A2(0x2)

    ChrTalk(    #88
        0xFE,
        (
            "I'm impressed. This is a much nicer\x01",
            "hotel than I had anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "The manager is extremely courteous,\x01",
            "and the place is relaxed and immaculate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "This is another kind of elegance\x01",
            "quite different from the luxurious\x01",
            "hotels in the Royal City.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1CE9")


    ChrTalk(    #91
        0xFE,
        (
            "I'm impressed. This is a much nicer\x01",
            "hotel than I had anticipated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "This is another kind of elegance\x01",
            "quite different from the luxurious\x01",
            "hotel in the Royal City.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D92")

    TalkEnd(0xB)
    Return()

    # Function_12_19AD end

    def Function_13_1D96(): pass

    label("Function_13_1D96")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #93
        (
            "\x07\x05Linen Room\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_1D96 end

    SaveToFile()

Try(main)
