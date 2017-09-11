from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4212   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4212.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Helmuth',                              # 9
        'Dayan',                                # 10
        'Tooker',                               # 11
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH01220 ._CH',             # 03
        'ED6_DT07/CH01570 ._CH',             # 04
        'ED6_DT07/CH01560 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH01220P._CP',             # 03
        'ED6_DT07/CH01570P._CP',             # 04
        'ED6_DT07/CH01560P._CP',             # 05
    )

    DeclNpc(
        X                   = -70580,
        Z                   = 0,
        Y                   = -37370,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -61220,
        Z                   = 0,
        Y                   = -35100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -67090,
        Z                   = 0,
        Y                   = -31900,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_13A",          # 00, 0
        "Function_1_218",          # 01, 1
        "Function_2_222",          # 02, 2
        "Function_3_238",          # 03, 3
        "Function_4_3E6",          # 04, 4
        "Function_5_769",          # 05, 5
    )


    def Function_0_13A(): pass

    label("Function_0_13A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_164")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_178")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_1A7")

    label("loc_178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_182")
    Jump("loc_1A7")

    label("loc_182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_18C")
    Jump("loc_1A7")

    label("loc_18C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_196")
    Jump("loc_1A7")

    label("loc_196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_1A0")
    Jump("loc_1A7")

    label("loc_1A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_1A7")

    label("loc_1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_1B6")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_217")

    label("loc_1B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_1C0")
    Jump("loc_217")

    label("loc_1C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_1CA")
    Jump("loc_217")

    label("loc_1CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_1D4")
    Jump("loc_217")

    label("loc_1D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_1DE")
    Jump("loc_217")

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_217")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_1F2")
    Jump("loc_217")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FC")
    Jump("loc_217")

    label("loc_1FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_206")
    Jump("loc_217")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_210")
    Jump("loc_217")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_217")

    label("loc_217")

    Return()

    # Function_0_13A end

    def Function_1_218(): pass

    label("Function_1_218")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_218 end

    def Function_2_222(): pass

    label("Function_2_222")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_237")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_222")

    label("loc_237")

    Return()

    # Function_2_222 end

    def Function_3_238(): pass

    label("Function_3_238")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_245")
    Jump("loc_3E2")

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_2F1")

    ChrTalk(    #0
        0xFE,
        (
            "The other officials who were sent\x01",
            "away on forced vacation should be\x01",
            "rolling back in right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Things are about to get very busy\x01",
            "for us, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E2")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_2FB")
    Jump("loc_3E2")

    label("loc_2FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_3E2")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_32C")

    ChrTalk(    #2
        0xFE,
        "Another long workday...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E2")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_3E2")

    ChrTalk(    #3
        0xFE,
        (
            "With so few people, we can't\x01",
            "possibly finish all this work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "All the other officials were sent away\x01",
            "'on vacation' by the duke, and forcibly\x01",
            "removed from the castle. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2")

    TalkEnd(0xFE)
    Return()

    # Function_3_238 end

    def Function_4_3E6(): pass

    label("Function_4_3E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3F3")
    Jump("loc_765")

    label("loc_3F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_495")

    ChrTalk(    #5
        0xFE,
        (
            "Stupid coup. We have so much\x01",
            "re-organizing to do, and so\x01",
            "much left-over work...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Another late night, huh? Working\x01",
            "for the court is the pits...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_765")

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_765")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_4A9")
    Jump("loc_765")

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_53B")

    ChrTalk(    #7
        0xFE,
        (
            "Can't even imagine what things would've been\x01",
            "like if the duke had taken over. Brrr, gives\x01",
            "me chills just thinking about it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60E")

    label("loc_53B")

    OP_A2(0x2)

    ChrTalk(    #8
        0xFE,
        (
            "Even though the duke was Her Majesty's\x01",
            "representative, the Intelligence Division\x01",
            "was pretty much calling all the shots.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "If Colonel Richard weren't around,\x01",
            "I shudder to think what might have\x01",
            "been...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60E")

    Jump("loc_765")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6AF")

    ChrTalk(    #10
        0xFE,
        (
            "This is where most of the actual\x01",
            "'ruling' of Liberl takes place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "With Her Majesty ill, we're taking\x01",
            "orders from...*sigh* the duke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_765")

    label("loc_6AF")

    OP_A2(0x2)

    ChrTalk(    #12
        0xFE,
        "This is the Administrative Room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "This is where most of the actual\x01",
            "'ruling' of Liberl takes place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "With Her Majesty ill, we're taking\x01",
            "orders from...*sigh* the duke.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_765")

    TalkEnd(0xFE)
    Return()

    # Function_4_3E6 end

    def Function_5_769(): pass

    label("Function_5_769")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_88E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7C8")

    ChrTalk(    #15
        0xFE,
        (
            "*sigh* Looks like I won't be\x01",
            "getting much fishing done for\x01",
            "a while...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_88B")

    label("loc_7C8")

    OP_A2(0x0)

    ChrTalk(    #16
        0xFE,
        "I've got to get back to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "The duke claimed there was nothing\x01",
            "to do and put us on forced vacation,\x01",
            "but...well, look at all of this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "It'll take us eons to clean up\x01",
            "this mess!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88B")

    Jump("loc_8EF")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 2)), scpexpr(EXPR_END)), "loc_898")
    Jump("loc_8EF")

    label("loc_898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_8A2")
    Jump("loc_8EF")

    label("loc_8A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 7)), scpexpr(EXPR_END)), "loc_8AC")
    Jump("loc_8EF")

    label("loc_8AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8B6")
    Jump("loc_8EF")

    label("loc_8B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 6)), scpexpr(EXPR_END)), "loc_8C0")
    Jump("loc_8EF")

    label("loc_8C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_8CA")
    Jump("loc_8EF")

    label("loc_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_8D4")
    Jump("loc_8EF")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_8DE")
    Jump("loc_8EF")

    label("loc_8DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 0)), scpexpr(EXPR_END)), "loc_8E8")
    Jump("loc_8EF")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_8EF")

    label("loc_8EF")

    TalkEnd(0xFE)
    Return()

    # Function_5_769 end

    SaveToFile()

Try(main)
