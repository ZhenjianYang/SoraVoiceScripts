from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0610   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0610.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
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
        'CWO Robin',                            # 9
        'Warrant Officer Graves',               # 10
        'Private Anden',                        # 11
        'Sam',                                  # 12
        'Emily',                                # 13
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
        Unknown_3A              = 17,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
    )

    DeclNpc(
        X                   = -19380,
        Z                   = 0,
        Y                   = -980,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -111940,
        Z                   = 0,
        Y                   = 21850,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -7220,
        Z                   = 0,
        Y                   = 2820,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -90130,
        Z                   = 0,
        Y                   = -22320,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -57740,
        Z                   = 0,
        Y                   = -21510,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    DeclActor(
        TriggerX            = -7430,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = -7220,
        ActorZ              = 1500,
        ActorY              = 2820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -109840,
        TriggerZ            = 0,
        TriggerY            = 21450,
        TriggerRange        = 1000,
        ActorX              = -111940,
        ActorZ              = 1500,
        ActorY              = 21850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92220,
        TriggerZ            = 0,
        TriggerY            = -22040,
        TriggerRange        = 1000,
        ActorX              = -90130,
        ActorZ              = 1500,
        ActorY              = -22320,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_218",          # 01, 1
        "Function_2_232",          # 02, 2
        "Function_3_248",          # 03, 3
        "Function_4_26C",          # 04, 4
        "Function_5_271",          # 05, 5
        "Function_6_B04",          # 06, 6
        "Function_7_160B",         # 07, 7
        "Function_8_1610",         # 08, 8
        "Function_9_2332",         # 09, 9
        "Function_10_2337",        # 0A, 10
        "Function_11_2DFB",        # 0B, 11
        "Function_12_3AFD",        # 0C, 12
        "Function_13_3CD0",        # 0D, 13
        "Function_14_3F90",        # 0E, 14
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_217")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1F2")
    Jump("loc_217")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1FC")
    Jump("loc_217")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_206")
    Jump("loc_217")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_210")
    Jump("loc_217")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_217")

    label("loc_217")

    Return()

    # Function_0_1DE end

    def Function_1_218(): pass

    label("Function_1_218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_227")
    OP_1B(0x0, 0x0, 0xC)
    Jump("loc_22C")

    label("loc_227")

    OP_1B(0x1, 0x0, 0xD)

    label("loc_22C")

    OP_1C(0x5, 0x0, 0xE)
    Return()

    # Function_1_218 end

    def Function_2_232(): pass

    label("Function_2_232")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_247")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_232")

    label("loc_247")

    Return()

    # Function_2_232 end

    def Function_3_248(): pass

    label("Function_3_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_26B")
    OP_8D(0xFE, -22660, -4810, -14730, 1940, 3000)
    Jump("Function_3_248")

    label("loc_26B")

    Return()

    # Function_3_248 end

    def Function_4_26C(): pass

    label("Function_4_26C")

    Call(0, 5)
    Return()

    # Function_4_26C end

    def Function_5_271(): pass

    label("Function_5_271")

    TalkBegin(0xB)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_2D2")
    OP_A9(0x66)
    Jump("loc_2D4")

    label("loc_2D2")

    OP_A9(0x64)

    label("loc_2D4")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_2DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE")
    TalkEnd(0xB)
    Return()

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_357")

    ChrTalk(    #0
        0xB,
        (
            "The soldiers were talking with\x01",
            "pretty scary faces...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xB,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_3F3")

    ChrTalk(    #2
        0xB,
        (
            "The Martial Arts Competition ends\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xB,
        (
            "With the queen's birthday celebration\x01",
            "approaching, I'm sure customers will\x01",
            "start to filter in.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_47D")

    ChrTalk(    #4
        0xB,
        (
            "While the soldiers seem busy,\x01",
            "I'm stuck with nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xB,
        (
            "With no entertainment here,\x01",
            "what's a person to do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_544")

    label("loc_47D")

    OP_A2(0x4)

    ChrTalk(    #6
        0xB,
        "*yawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "While the soldiers seem busy,\x01",
            "I'm stuck with nothing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xB,
        (
            "I even cleaned almost all there\x01",
            "is to be cleaned too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xB,
        (
            "No customers, no entertainment,\x01",
            "what's a person to do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_544")

    Jump("loc_B00")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_609")

    ChrTalk(    #10
        0xB,
        (
            "When the Martial Arts Competition\x01",
            "is underway, the customers here\x01",
            "drastically decrease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        (
            "I'd like to close up shop and go\x01",
            "watch the competition myself,\x01",
            "but I can't afford it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_6A8")

    ChrTalk(    #12
        0xB,
        (
            "And then we've got those acts of\x01",
            "terrorism by the Royal Guard.\x01",
            "It's unbelievable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "I'm sure the Royal City is probably\x01",
            "crazy at the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_6A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_72E")

    ChrTalk(    #14
        0xB,
        (
            "All the customers who were here\x01",
            "earlier took off for Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "Well, I guess I should get to\x01",
            "cleaning while I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_7EB")

    ChrTalk(    #16
        0xB,
        (
            "It seems like the number of people\x01",
            "passing through the checkpoint\x01",
            "suddenly increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xB,
        (
            "The queen's birthday celebration is\x01",
            "still a little way off, so I wonder\x01",
            "what's up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_7EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_87D")

    ChrTalk(    #18
        0xB,
        "Welcome, valued customers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        (
            "I've been pretty bored with the recent\x01",
            "lack of customers. You're a sight for\x01",
            "sore eyes, I tell ya.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_87D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_913")

    ChrTalk(    #20
        0xB,
        (
            "There are hardly any customers\x01",
            "today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xB,
        (
            "Guess I should make myself useful and\x01",
            "get to the cleaning I normally don't\x01",
            "have time for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_913")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_96D")

    ChrTalk(    #22
        0xB,
        "Welcome, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        (
            "If you'd like to spend the night,\x01",
            "give me a holler.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_96D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_A2C")

    ChrTalk(    #24
        0xB,
        (
            "Maybe I should wash and dry all the\x01",
            "sheets while the weather's clear...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        (
            "I want my customers to be able\x01",
            "to sleep well if they're going to\x01",
            "come all the way here. Yes siree.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B00")

    label("loc_A2C")


    ChrTalk(    #26
        0xB,
        (
            "Welcome, valued customers.\x01",
            "This is a traveler's inn where\x01",
            "anyone can stay the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "We've also got a mess hall\x01",
            "next to us as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xB,
        (
            "If you're ever up for it,\x01",
            "feel free to come and spend the\x01",
            "night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B00")

    TalkEnd(0xB)
    Return()

    # Function_5_271 end

    def Function_6_B04(): pass

    label("Function_6_B04")

    TalkBegin(0xC)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B64")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x65)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_B64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7E")
    FadeToBright(300, 0)
    TalkEnd(0xC)
    Return()

    label("loc_B7E")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_C0B")

    ChrTalk(    #29
        0xC,
        (
            "When the soldiers are frantic,\x01",
            "I get a bit anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xC,
        (
            "I hope we can see in this year's\x01",
            "festival without incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_D7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_CA7")

    ChrTalk(    #31
        0xC,
        (
            "I tried to cook a new recipe, but\x01",
            "it didn't turn out that well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xC,
        (
            "I figured if things went well then\x01",
            "I could add it to the menu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_CA7")

    OP_A2(0x5)

    ChrTalk(    #33
        0xC,
        (
            "I tried to cook a new recipe, but\x01",
            "it didn't turn out that well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xC,
        (
            "I figured if things went well then\x01",
            "I could add it to the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xC,
        (
            "I'll try out some other recipes when\x01",
            "I get some more free time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7A")

    Jump("loc_1607")

    label("loc_D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DFB")

    ChrTalk(    #36
        0xC,
        (
            "I'm sad that there aren't more\x01",
            "customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xC,
        (
            "But it's also a good opportunity\x01",
            "to enjoy my own time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E93")

    label("loc_DFB")

    OP_A2(0x5)

    ChrTalk(    #38
        0xC,
        (
            "I'm sad that there aren't more\x01",
            "customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xC,
        (
            "But it's also a good opportunity\x01",
            "to enjoy my own time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xC,
        "Maybe I'll try a new recipe today.\x02",
    )

    CloseMessageWindow()

    label("loc_E93")

    Jump("loc_1607")

    label("loc_E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_F77")

    ChrTalk(    #41
        0xC,
        (
            "Now that I've got some time, maybe I'll\x01",
            "try baking some cookies. With luck, no\x01",
            "one will get food poisoning this time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xC,
        (
            "Maybe I'll even try making an extra\x01",
            "something for the soldiers who seem\x01",
            "to be so busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_F77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_10D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1006")

    ChrTalk(    #43
        0xC,
        (
            "As a woman, I really look up to\x01",
            "Julia Schwarz of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xC,
        (
            "She's cool, well-mannered,\x01",
            "and incredibly strong.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D2")

    label("loc_1006")

    OP_A2(0x5)

    ChrTalk(    #45
        0xC,
        (
            "As a woman, I really look up to\x01",
            "Julia Schwarz of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xC,
        (
            "She's cool, well-mannered,\x01",
            "and incredibly strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xC,
        (
            "I've heard that she trained with the\x01",
            "sword under some Cassius fellow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D2")

    Jump("loc_1607")

    label("loc_10D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1161")

    ChrTalk(    #48
        0xC,
        (
            "Did you all come from the\x01",
            "Royal City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xC,
        (
            "It's awfully rare to see anyone coming\x01",
            "here from Grancel during this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FE")

    label("loc_1161")

    OP_A2(0x5)

    ChrTalk(    #50
        0xC,
        "How may I help you today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "Did you all come from the\x01",
            "Royal City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        (
            "It's awfully rare to see anyone coming\x01",
            "here from Grancel during this time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FE")

    Jump("loc_1607")

    label("loc_1201")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1316")

    ChrTalk(    #53
        0xFE,
        (
            "Recently it seems like Eastern food\x01",
            "has gotten popular as a side dish to\x01",
            "food from Liberl and the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Maybe I'll buy a book with Eastern\x01",
            "recipes next time I head to the\x01",
            "Royal City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I'm really interested to see what\x01",
            "kinds of dishes they have there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_1316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_13FA")

    ChrTalk(    #56
        0xFE,
        (
            "All of the soldiers here are kind and even if my\x01",
            "cooking sometimes sends them to the hospital,\x01",
            "they always tell me that it's delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "In some ways I'm glad, but I'd like\x01",
            "to hear their honest opinion too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_13FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1488")

    ChrTalk(    #58
        0xFE,
        "This time is a bit boring for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Though, I suppose I could take advantage\x01",
            "of the downtime and try working\x01",
            "on a new menu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_1488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_14BB")

    ChrTalk(    #60
        0xFE,
        (
            "Welcome.\x01",
            "What would you like today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_14BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_15A9")

    ChrTalk(    #61
        0xFE,
        (
            "The more you use a frying pan,\x01",
            "the more beautiful it becomes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "I couldn't be happier than when the\x01",
            "black luster gets burned into the\x01",
            "metal with each dish I prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "For a cook, it's like making\x01",
            "your mark on a pan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1607")

    label("loc_15A9")


    ChrTalk(    #64
        0xFE,
        (
            "Welcome to the Gurune Gate\x01",
            "Mess Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Please go ahead and order\x01",
            "something you like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1607")

    TalkEnd(0xC)
    Return()

    # Function_6_B04 end

    def Function_7_160B(): pass

    label("Function_7_160B")

    Call(0, 8)
    Return()

    # Function_7_160B end

    def Function_8_1610(): pass

    label("Function_8_1610")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_16B1")

    ChrTalk(    #66
        0xA,
        (
            "All checkpoints throughout the\x01",
            "Liberl Kingdom are closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xA,
        (
            "I really apologize, but this is in\x01",
            "order to seal off the terrorists'\x01",
            "movements.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(    #68
        0xA,
        (
            "The Intelligence Division is different from\x01",
            "the Royal Guard. They use strong arm\x01",
            "tactics and are arrogant to the core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "It makes me wonder who the\x01",
            "real terrorists are here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1860")

    label("loc_1778")

    OP_A2(0x3)

    ChrTalk(    #70
        0xA,
        (
            "The Intelligence Division has\x01",
            "begun to patrol this area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "But they're different from the Royal\x01",
            "Guard. They use strong arm tactics\x01",
            "and are arrogant to the core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        (
            "It makes me wonder who the\x01",
            "real terrorists are here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1860")

    Jump("loc_232E")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1994")

    ChrTalk(    #73
        0xA,
        (
            "All those passing through here starting today\x01",
            "will have to show some form of identification or\x01",
            "must turn around and leave the way they came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "I'm sorry to say this, but if you wish to pass\x01",
            "through here, you'll need to show documentation\x01",
            "or some other verifiable form of identification.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1A69")

    ChrTalk(    #75
        0xA,
        (
            "I'm sure you've already noticed\x01",
            "that this place was made using\x01",
            "a part of the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "Sure, it's got a historic feel to it,\x01",
            "and a unique sort of charm...but\x01",
            "it's inconvenient, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1B81")

    ChrTalk(    #77
        0xA,
        (
            "Those passing through this gate are not nearly\x01",
            "as great in number as those passing through\x01",
            "the Sanktheim Gate on the other side.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "Although we do see a small spike in numbers for\x01",
            "events like the queen's birthday celebration,\x01",
            "Martial Arts Competition, and so on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1C1B")

    ChrTalk(    #79
        0xA,
        (
            "Huh...? You aren't leaving\x01",
            "Grancel, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "Almost nobody goes to Rolent\x01",
            "during the time the Martial Arts\x01",
            "Competition is being held.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1D1D")

    ChrTalk(    #81
        0xA,
        (
            "With the airliners being stopped,\x01",
            "this place has seen an increase\x01",
            "in travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "Those with urgent business in the\x01",
            "Royal City pass through this\x01",
            "checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "It almost feels like we've gone\x01",
            "back to the era when there were\x01",
            "no airliners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1E01")

    ChrTalk(    #84
        0xA,
        (
            "The forest of Mistwald is a little \x01",
            "further to the north than here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "There is a small path leading to it which branches\x01",
            "off to the east of the highway. Make sure to keep\x01",
            "your eyes peeled so you don't miss it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1EA7")

    ChrTalk(    #86
        0xA,
        (
            "The forest of Mistwald to the\x01",
            "north of here is the center of\x01",
            "Rolent's timber industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "Sometimes, those in the timber\x01",
            "business come here to rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_1EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_201F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F98")
    OP_A2(0x3)

    ChrTalk(    #88
        0xA,
        (
            "Bracers can choose which branch\x01",
            "they want to be registered at?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "How lucky. Soldiers have no say\x01",
            "in where they're assigned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "Then again, if we could, the base\x01",
            "contingents would probably be a\x01",
            "little lopsided.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_201C")

    label("loc_1F98")


    ChrTalk(    #91
        0xA,
        (
            "Bracers can choose which branch\x01",
            "they want to be registered at?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "How lucky. Soldiers have no say\x01",
            "in where they're assigned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_201C")

    Jump("loc_232E")

    label("loc_201F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2145")

    ChrTalk(    #93
        0xA,
        (
            "There are checkpoints on all regional\x01",
            "borders within the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "That's because we began checking all\x01",
            "travelers entering or leaving the\x01",
            "regions after the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "It's basically the same as\x01",
            "checking your identification\x01",
            "when you buy an airliner ticket.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_2145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2273")
    OP_A2(0x3)

    ChrTalk(    #96
        0xA,
        "Oh, are you heading to Grancel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#000FUh, no. Not exactly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "I should have figured as much. Recently,\x01",
            "pretty much everybody who wants to go\x01",
            "to Grancel from Rolent takes the airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "People passing through here on foot\x01",
            "like the old days have become almost\x01",
            "nonexistent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_232E")

    label("loc_2273")


    ChrTalk(    #100
        0xA,
        (
            "Recently, pretty much everybody\x01",
            "who wants to go to Grancel from\x01",
            "Rolent takes the airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "People passing through here on foot\x01",
            "like the old days have become almost\x01",
            "nonexistent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232E")

    TalkEnd(0xA)
    Return()

    # Function_8_1610 end

    def Function_9_2332(): pass

    label("Function_9_2332")

    Call(0, 10)
    Return()

    # Function_9_2332 end

    def Function_10_2337(): pass

    label("Function_10_2337")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2411")

    ChrTalk(    #102
        0x9,
        (
            "Yesterday we received a transmission from\x01",
            "headquarters indicating that the checkpoint\x01",
            "was to be completely sealed off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "I'm sorry, but no one besides military\x01",
            "personnel will be permitted to pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_2411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(    #104
        0x9,
        (
            "The Martial Arts Competition ends\x01",
            "today, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "I'm sure we'll get some new orders\x01",
            "from the royal castle any time now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_252F")

    ChrTalk(    #106
        0x9,
        (
            "We will be on heightened alert\x01",
            "from today on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "Those travelers whose backgrounds\x01",
            "cannot be confirmed will not be\x01",
            "allowed to pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_252F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_26BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_25D9")

    ChrTalk(    #108
        0x9,
        (
            "Airliners are now the major form\x01",
            "of transit in the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "Clamping down on air travel means\x01",
            "that people and goods are unable\x01",
            "to move.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BB")

    label("loc_25D9")

    OP_A2(0x2)

    ChrTalk(    #110
        0x9,
        (
            "Many places have been affected\x01",
            "by the Royal Army's restrictions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "Airliners are now the major form\x01",
            "of transit in the Liberl Kingdom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "Clamping down on air travel means\x01",
            "that people and goods are unable\x01",
            "to move.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BB")

    Jump("loc_2DF7")

    label("loc_26BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_27AF")

    ChrTalk(    #113
        0x9,
        (
            "I met some members of the Royal Guard during\x01",
            "training and I must say, they are indeed worthy\x01",
            "of the title of those who protect Her Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        (
            "I just can't believe that they\x01",
            "had anything to do with the\x01",
            "terrorist incident...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_27AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_28F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_284C")

    ChrTalk(    #115
        0x9,
        (
            "If I remember correctly, some\x01",
            "new recruits were enlisted at\x01",
            "the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "I'm sure they've got their work\x01",
            "cut out for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EE")

    label("loc_284C")

    OP_A2(0x2)

    ChrTalk(    #117
        0x9,
        (
            "With security being heightened,\x01",
            "all training has been canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "The Gurune Gate has a number\x01",
            "of veteran soldiers working here,\x01",
            "so we're not worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EE")

    Jump("loc_2DF7")

    label("loc_28F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2A08")

    ChrTalk(    #119
        0x9,
        (
            "I've heard that an airliner vanished\x01",
            "somewhere over Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x9,
        (
            "I'm worried about the safety\x01",
            "of those on-board...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "However, the border garrison in\x01",
            "Bose boasts some of the elite in\x01",
            "the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x9,
        (
            "I'm fairly confident that they'll\x01",
            "find the missing airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_2A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_2B09")

    ChrTalk(    #123
        0x9,
        (
            "Well...I guess it's time to put in\x01",
            "another hard day's work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        (
            "It's during peaceful times such\x01",
            "as these when we need to prepare\x01",
            "for any number of situations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "I thought those words sounded\x01",
            "good, so I borrowed that phrase\x01",
            "off the chief.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_2B09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2BB2")

    ChrTalk(    #126
        0x9,
        (
            "This year marks a decade since\x01",
            "the end of the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x9,
        (
            "When I look at the peaceful state\x01",
            "our country is in now, those days\x01",
            "feel so far off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_2BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_2CA9")

    ChrTalk(    #128
        0x9,
        (
            "The mayor of Rolent came to observe\x01",
            "this place before and I must say,\x01",
            "he's certainly a nice fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "More than a mayor, he felt like the\x01",
            "caring old man who lives next-door\x01",
            "type.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "I can see why the citizens like\x01",
            "him so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_2D84")

    ChrTalk(    #131
        0x9,
        (
            "It seems as though a new organization\x01",
            "popped up in the Royal City made up\x01",
            "entirely of people who love to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x9,
        (
            "I'm kinda interested in what type of\x01",
            "organization it is too, since I also\x01",
            "love to fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DF7")

    label("loc_2D84")


    ChrTalk(    #133
        0x9,
        (
            "Good afternoon.\x01",
            "Have you come to take a tour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "Anyone can use these facilities,\x01",
            "so make yourself at home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF7")

    TalkEnd(0x9)
    Return()

    # Function_10_2337 end

    def Function_11_2DFB(): pass

    label("Function_11_2DFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_2EE9")

    ChrTalk(    #135
        0xFE,
        (
            "Finally all the checkpoints have\x01",
            "been sealed off and all flights\x01",
            "are grounded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "Even for someone like Colonel Richard, I don't\x01",
            "know if this is something appropriate to order\x01",
            "without the approbation of Her Majesty...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_2EE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_2FE0")

    ChrTalk(    #137
        0xFE,
        (
            "According to the rumors, the terrorist\x01",
            "that claims to be a bracer is quite\x01",
            "skilled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Since we wouldn't stand a chance in a one on one\x01",
            "battle, I've got to think of a security measure\x01",
            "so that the soldiers can coordinate together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_3239")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30E3")

    ChrTalk(    #139
        0xFE,
        (
            "From what I've heard, the terrorists\x01",
            "who appeared in Zeiss were dressed\x01",
            "in the uniforms of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Supposing that the criminals actually were\x01",
            "the Royal Guard, would they really wear\x01",
            "their own uniforms during the attack...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_30E3")

    OP_A2(0x1)

    ChrTalk(    #141
        0xFE,
        (
            "From what I've heard, the terrorists\x01",
            "who appeared in Zeiss were dressed\x01",
            "in the uniforms of the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "The Royal Guard is a group of the\x01",
            "most talented individuals the Royal\x01",
            "Army has to offer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Supposing that the criminals actually were\x01",
            "the Royal Guard, would they really wear\x01",
            "their own uniforms during the attack...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3236")

    Jump("loc_3AF9")

    label("loc_3239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_33F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32DF")

    ChrTalk(    #144
        0xFE,
        (
            "For the time being, no big incidents\x01",
            "have occurred in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "However, in the event that something\x01",
            "does happen, we are poised to\x01",
            "mobilize.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F0")

    label("loc_32DF")

    OP_A2(0x1)

    ChrTalk(    #146
        0xFE,
        (
            "It seems that there is a very capable\x01",
            "female bracer working at the Bracer\x01",
            "Guild's Rolent branch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "And it's probably for that reason\x01",
            "that no big incidents have occurred\x01",
            "in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "However, in the event that something\x01",
            "does happen, we are poised to\x01",
            "mobilize.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F0")

    Jump("loc_3AF9")

    label("loc_33F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_352C")

    ChrTalk(    #149
        0xFE,
        (
            "We've received reports that the\x01",
            "Royal Guard was involved in a\x01",
            "terrorist incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "But it's also been rumored that the\x01",
            "terrorists have been dressing up like\x01",
            "the Royal Guard and bracers to boot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "I wonder who's telling the truth.\x01",
            "I'd really like to receive some\x01",
            "accurate information ASAP.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_352C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_35E5")

    ChrTalk(    #152
        0xFE,
        (
            "This is the first time the army has\x01",
            "heightened security in all regions\x01",
            "since the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "This makes me remember a lot of\x01",
            "things that happened back then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_35E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_370F")

    ChrTalk(    #154
        0xFE,
        (
            "It seems that a suspicious aircraft\x01",
            "was seen flying over the airspace\x01",
            "above Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "Per our investigation, it appears that\x01",
            "there were marks of something landing\x01",
            "there on several occasions in the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "We'd better report this to headquarters\x01",
            "at the Leiston Fortress ASAP.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_370F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_3803")

    ChrTalk(    #157
        0xFE,
        (
            "Rolent is a region with few incidents\x01",
            "to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "But that doesn't guarantee that there\x01",
            "won't be problems in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "No matter which garrison for whatever\x01",
            "region, we cannot allow ourselves to\x01",
            "let down our guard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_3803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_38D3")

    ChrTalk(    #160
        0xFE,
        (
            "No big incidents have happened\x01",
            "today either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "It's at peaceful times like these that\x01",
            "we should prepare contingency plans\x01",
            "and conduct intensive training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "All part of the job, you know.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_38D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_39DF")

    ChrTalk(    #163
        0xFE,
        (
            "This checkpoint leads to the Royal\x01",
            "City and has a number of veteran\x01",
            "soldiers stationed here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "But on the other hand, it appears that\x01",
            "the Verte Bridge Checkpoint has all\x01",
            "new recruits stationed there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "I wonder if the chief will\x01",
            "be all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_39DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3A76")

    ChrTalk(    #166
        0xFE,
        (
            "The Royal City is slowly but surely\x01",
            "making preparations for the queen's\x01",
            "birthday celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "I'm certainly looking forward to it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_3A76")


    ChrTalk(    #168
        0xFE,
        (
            "Oh, you're bracers, aren't you?\x01",
            "Thanks for all your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "Let's make sure to work together\x01",
            "if any incidents happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF9")

    TalkEnd(0xFE)
    Return()

    # Function_11_2DFB end

    def Function_12_3AFD(): pass

    label("Function_12_3AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_3CCF")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B8F")
    TurnDirection(0x102, 0x101, 400)

    def lambda_3B28():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3B28)

    ChrTalk(    #170
        0x102,
        (
            "#010FThis leads to Rolent.\x02\x03",

            "But it doesn't look like we'll be\x01",
            "returning for a while...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB4")

    label("loc_3B8F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C23")

    ChrTalk(    #171
        0x104,
        (
            "#030FSo this is good ol' Rolent, huh?\x02\x03",

            "I've always wanted to visit there,\x01",
            "but this doesn't appear to be the\x01",
            "best time for that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CB4")

    label("loc_3C23")


    ChrTalk(    #172
        0x108,
        (
            "#070FNow just hold up a sec.\x01",
            "This way leads to another region.\x02\x03",

            "Let's quietly turn around before we\x01",
            "have some soldiers start yelling at\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB4")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3CCF")

    Return()

    # Function_12_3AFD end

    def Function_13_3CD0(): pass

    label("Function_13_3CD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3DEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D73")
    OP_A2(0x0)
    TurnDirection(0x102, 0x101, 400)

    def lambda_3D07():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3D07)

    ChrTalk(    #173
        0x102,
        (
            "#010FThis leads to Grancel.\x02\x03",

            "I don't think we'll be able to go\x01",
            "through here without a pass.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DE9")

    label("loc_3D73")

    TurnDirection(0x102, 0x101, 400)

    def lambda_3D80():
        TurnDirection(0x101, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3D80)

    ChrTalk(    #174
        0x102,
        (
            "#010FThis leads to Grancel.\x02\x03",

            "I don't think we'll be able to go\x01",
            "through here without a pass.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE9")

    Jump("loc_3F74")

    label("loc_3DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EAD")
    TurnDirection(0x103, 0x101, 400)

    def lambda_3E01():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3E01)

    def lambda_3E0F():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3E0F)

    ChrTalk(    #175
        0x103,
        (
            "#020FThis goes to Grancel. We'll need a\x01",
            "pass to get through the checkpoint.\x02\x03",

            "Then again, that's not where we're\x01",
            "supposed to be headed anyway.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F74")

    label("loc_3EAD")

    TurnDirection(0x103, 0x101, 400)

    def lambda_3EBA():
        TurnDirection(0x102, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3EBA)

    def lambda_3EC8():
        TurnDirection(0x101, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3EC8)

    ChrTalk(    #176
        0x103,
        (
            "#020FThis goes to Grancel. We'll need a\x01",
            "pass to get through the checkpoint.\x02\x03",

            "The Verte Bridge is going to need\x01",
            "a pass too, so make sure to take\x01",
            "a mental note.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F74")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3F8F")

    Return()

    # Function_13_3CD0 end

    def Function_14_3F90(): pass

    label("Function_14_3F90")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_14_3F90 end

    SaveToFile()

Try(main)
