from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1130   ._SN',
        MapName             = 'Bose',
        Location            = 'T1130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0130   ._SN',
            'ED6_DT01/T1130_1 ._SN',
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
        'Father Holstein',                      # 9
        'Sister Rosa',                          # 10
        'Seagaro',                              # 11
        'Edel',                                 # 12
        'Lila',                                 # 13
        'Sarah',                                # 14
        'Target Camera',                        # 15
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
        'ED6_DT07/CH01400 ._CH',             # 00
        'ED6_DT07/CH01410 ._CH',             # 01
        'ED6_DT07/CH01043 ._CH',             # 02
        'ED6_DT07/CH01213 ._CH',             # 03
        'ED6_DT07/CH01350 ._CH',             # 04
        'ED6_DT07/CH02370 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01043P._CP',             # 02
        'ED6_DT07/CH01213P._CP',             # 03
        'ED6_DT07/CH01350P._CP',             # 04
        'ED6_DT07/CH02370P._CP',             # 05
    )

    DeclNpc(
        X                   = 59100,
        Z                   = 1000,
        Y                   = 52100,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 15690,
        Z                   = 4000,
        Y                   = 43180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 63600,
        Z                   = 90,
        Y                   = 46000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 62600,
        Z                   = 90,
        Y                   = 46000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 58950,
        Z                   = 0,
        Y                   = 48260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 58920,
        Z                   = 0,
        Y                   = 48170,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TriggerX            = 58950,
        TriggerZ            = 1000,
        TriggerY            = 50250,
        TriggerRange        = 400,
        ActorX              = 59100,
        ActorZ              = 2500,
        ActorY              = 52100,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_247",          # 01, 1
        "Function_2_248",          # 02, 2
        "Function_3_25E",          # 03, 3
        "Function_4_27C",          # 04, 4
        "Function_5_CEC",          # 05, 5
        "Function_6_160A",         # 06, 6
        "Function_7_168C",         # 07, 7
        "Function_8_173A",         # 08, 8
        "Function_9_17F1",         # 09, 9
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1E8")
    Jump("loc_235")

    label("loc_1E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1F7")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_235")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_206")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_235")

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_210")
    Jump("loc_235")

    label("loc_210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_235")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_224")
    Jump("loc_235")

    label("loc_224")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_235")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_246")
    ClearChrFlags(0xC, 0x80)

    label("loc_246")

    Return()

    # Function_0_1DE end

    def Function_1_247(): pass

    label("Function_1_247")

    Return()

    # Function_1_247 end

    def Function_2_248(): pass

    label("Function_2_248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_248")

    label("loc_25D")

    Return()

    # Function_2_248 end

    def Function_3_25E(): pass

    label("Function_3_25E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_277")
    Call(1, 0)
    Jump("loc_27B")

    label("loc_277")

    Call(0, 4)

    label("loc_27B")

    Return()

    # Function_3_25E end

    def Function_4_27C(): pass

    label("Function_4_27C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_345")

    ChrTalk(    #0
        0x8,
        (
            "You must be tired after having made\x01",
            "the trip all the way from Rolent today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        "Oh Aidios, who art in heaven...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Please bestow thy blessings and\x01",
            "thy guidance upon these souls...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_443")
    OP_A2(0x0)

    ChrTalk(    #3
        0x8,
        (
            "Although a lot has happened,\x01",
            "the city seems to be returning\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Well, I guess the fact that no one lost their\x01",
            "spirit despite the numerous incidents is one\x01",
            "of the strong points of the citizens of Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "Ho ho ho.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D1")

    label("loc_443")


    ChrTalk(    #6
        0x8,
        (
            "Well, I guess the fact that no one lost their\x01",
            "spirit despite the numerous incidents is one\x01",
            "of the strong points of the citizens of Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1")

    Jump("loc_CE8")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EA")
    OP_A2(0x0)

    ChrTalk(    #7
        0x8,
        (
            "There sure seems to have been a\x01",
            "wave of incidents occurring lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Maybe I should raise my voice to the\x01",
            "heavens on behalf of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Oh Aidios, who art in heaven...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "Please bestow thy blessings and\x01",
            "thy guidance upon these souls...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680")

    label("loc_5EA")


    ChrTalk(    #11
        0x8,
        (
            "There sure seems to have been a\x01",
            "wave of incidents occurring lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Maybe I should raise my voice to the\x01",
            "heavens on behalf of the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_680")

    Jump("loc_CE8")

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_6DC")

    ChrTalk(    #13
        0x8,
        "It seems to be rather noisy outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_89B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E0")
    OP_A2(0x0)

    ChrTalk(    #15
        0x8,
        (
            "To the northwest of here there is\x01",
            "a village that cultivates fruit called\x01",
            "Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "Unfortunately, there is no chapel\x01",
            "in the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I'd be most delighted to have the\x01",
            "children from there come here\x01",
            "for Sunday School.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_898")

    label("loc_7E0")


    ChrTalk(    #18
        0x8,
        (
            "To the northwest of here there is\x01",
            "a village that cultivates fruit called\x01",
            "Ravennue Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "I'd be most delighted to have the\x01",
            "children from there come here\x01",
            "for Sunday School.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_898")

    Jump("loc_CE8")

    label("loc_89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F5")
    OP_A2(0x0)

    ChrTalk(    #20
        0x8,
        (
            "Sister Rosa is an extremely serious\x01",
            "and dedicated individual...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "Ho ho, I think it would do her some\x01",
            "good though if she wasn't so uptight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "The local tone of the people of Bose\x01",
            "carries an air of freedom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "While doctrine and commandments\x01",
            "are important, I'd like this church to\x01",
            "be more involved in the region.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A27")

    label("loc_9F5")


    ChrTalk(    #24
        0x8,
        (
            "Ho ho, because not everyone\x01",
            "sees eye to eye.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A27")

    Jump("loc_CE8")

    label("loc_A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_AFB")

    ChrTalk(    #25
        0x8,
        (
            "Mayor Maybelle is the daughter of\x01",
            "the late mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "She may be young and a little\x01",
            "rough around the edges...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "But she isn't the type of person to let\x01",
            "herself be limited by her own father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_CE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24")
    OP_A2(0x0)

    ChrTalk(    #28
        0x8,
        (
            "During the war 10 years ago, the city\x01",
            "of Bose was reduced to a pile of\x01",
            "rubble, for the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "However, the merchants at that time\x01",
            "used their fortunes as capital to\x01",
            "rebuild the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "And though they had been pursuing\x01",
            "their own interests, they united as one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE8")

    label("loc_C24")


    ChrTalk(    #31
        0x8,
        (
            "During the war 10 years ago, the city\x01",
            "of Bose was reduced to a pile of\x01",
            "rubble, for the most part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "However, the merchants at that time\x01",
            "used their fortunes as capital to\x01",
            "rebuild the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE8")

    TalkEnd(0x8)
    Return()

    # Function_4_27C end

    def Function_5_CEC(): pass

    label("Function_5_CEC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E43")
    OP_A2(0x2)

    ChrTalk(    #33
        0xFE,
        (
            "Let's see...the cleaning and the\x01",
            "laundry are done...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "And the materials for the discourse\x01",
            "and preparations for the sacrament\x01",
            "have been made...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Oh right, now what should I do about\x01",
            "the next lesson for Sunday School...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I'll feel as though I'm being slothful if\x01",
            "I don't get this decided ahead of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9A")

    label("loc_E43")


    ChrTalk(    #37
        0xFE,
        (
            "I'll feel as though I'm being slothful if\x01",
            "I don't get this decided ahead of time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9A")

    Jump("loc_1606")

    label("loc_E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_FE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4D")
    OP_A2(0x2)

    ChrTalk(    #38
        0xFE,
        (
            "It's unbelievable to think that normal\x01",
            "homes were burglarized too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Maybe I should go visit the victims\x01",
            "of these incidents later on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_F4D")


    ChrTalk(    #41
        0xFE,
        (
            "I can't believe the shops on Bose's\x01",
            "commercial avenue were burglarized...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Maybe I should go visit the victims\x01",
            "of these incidents later on...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE4")

    Jump("loc_1606")

    label("loc_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1085")

    ChrTalk(    #43
        0xFE,
        (
            "Although we're trying to conduct\x01",
            "worship services in here, it\x01",
            "certainly is loud outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "This town never stops being noisy\x01",
            "all year long.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1606")

    label("loc_1085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_125F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11B3")
    OP_A2(0x2)

    ChrTalk(    #45
        0xFE,
        (
            "We get a lot of people coming to\x01",
            "the chapel to pray for the success\x01",
            "of their businesses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "But Aidios, the Goddess of all creation,\x01",
            "is not a deity of fortune!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I wonder if I should post a note on\x01",
            "the door to tell people that this kind\x01",
            "of sacrilege is unacceptable...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125C")

    label("loc_11B3")


    ChrTalk(    #48
        0xFE,
        (
            "We get a lot of people coming to\x01",
            "the chapel to pray for the success\x01",
            "of their businesses...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "But Aidios, the Goddess of all creation,\x01",
            "is not a deity of fortune!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125C")

    Jump("loc_1606")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_1305")

    ChrTalk(    #50
        0xFE,
        (
            "Father Holstein's a man of his word\x01",
            "and has a magnetic personality\x01",
            "about him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "But I have trouble dealing with the\x01",
            "pace at which he does things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1606")

    label("loc_1305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_1568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_146C")
    OP_A2(0x2)

    ChrTalk(    #52
        0xFE,
        (
            "The mayor leaving her maid to do the\x01",
            "worshiping for her is something I've never\x01",
            "heard of in all my years in the ministry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Father Holstein doesn't seem to\x01",
            "take any offense at it, but for\x01",
            "me it's deplorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "And the mayor, of all people, is the one\x01",
            "person who I think should show their\x01",
            "face around here above anybody else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1565")

    label("loc_146C")


    ChrTalk(    #55
        0xFE,
        (
            "The mayor leaving her maid to do the\x01",
            "worshiping for her is something I've never\x01",
            "heard of in all my years in the ministry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "And the mayor, of all people, is the one\x01",
            "person who I think should show their\x01",
            "face around here above anybody else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1565")

    Jump("loc_1606")

    label("loc_1568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_1606")

    ChrTalk(    #57
        0xFE,
        "Welcome to the Septian Church.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Are you here to worship? I'm impressed\x01",
            "to see people as young as yourselves\x01",
            "concerned with spiritual matters.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1606")

    TalkEnd(0x9)
    Return()

    # Function_5_CEC end

    def Function_6_160A(): pass

    label("Function_6_160A")

    TalkBegin(0xA)

    ChrTalk(    #59
        0xFE,
        (
            "As we were arriving in Bose the\x01",
            "airliner flights were canceled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "And right in the middle of my\x01",
            "pilgrimage, too...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_6_160A end

    def Function_7_168C(): pass

    label("Function_7_168C")

    TalkBegin(0xB)

    ChrTalk(    #61
        0xFE,
        "La la la, we're finally here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "This day has finally arrived...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "After my husband is done worshiping here,\x01",
            "it's off to the Bose Market to buy, buy, buy!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_7_168C end

    def Function_8_173A(): pass

    label("Function_8_173A")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BB")
    OP_A2(0x5)

    ChrTalk(    #64
        0xFE,
        (
            "Why do military personnel have\x01",
            "to be so arrogant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Bracers are much nicer, and that's\x01",
            "why I like them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17ED")

    label("loc_17BB")


    ChrTalk(    #66
        0xFE,
        (
            "I'm here to pray in the mayor's\x01",
            "place today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17ED")

    TalkEnd(0xD)
    Return()

    # Function_8_173A end

    def Function_9_17F1(): pass

    label("Function_9_17F1")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1897")

    ChrTalk(    #67
        0xFE,
        (
            "#620FThe mayor has been working into the\x01",
            "night day after day and now she has\x01",
            "these burglaries to deal with.\x02\x03",

            "I've got to look out for her health...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F70")

    label("loc_1897")

    EventBegin(0x0)
    OP_A2(0x30A)
    Fade(1000)
    SetChrPos(0x101, 58910, 0, 46930, 0)
    SetChrPos(0x102, 58250, 0, 46000, 0)
    SetChrPos(0x103, 59540, 0, 46030, 0)
    TurnDirection(0xFE, 0x101, 0)
    OP_69(0xC, 0x3E8)

    ChrTalk(    #68
        0x101,
        (
            "#001FOh, there you are! You're the maid\x01",
            "we've been looking for.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #69
        0xC,
        "#620FAnd you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        (
            "#017FEstelle, that wasn't very polite.\x02\x03",

            "#010FMy apologies, we're with the\x01",
            "Bracer Guild.\x02\x03",

            "We're looking for the mayor so we\x01",
            "can confirm the details of a job\x01",
            "she requested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xC,
        (
            "#621FOh, I see...\x02\x03",

            "Please let me introduce myself.\x01",
            "I am her maid, Lila.\x02\x03",

            "I see to the mayor's daily needs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#000FBeing served hand and foot, huh...?\x01",
            "The worlds we live in are really different.\x02\x03",

            "So where is the mayor, if you don't\x01",
            "mind me asking? Didn't she come\x01",
            "here to pray?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xC,
        (
            "#623FShe's playing hooky from her\x01",
            "religious duties...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#008FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xC,
        (
            "#620FI'm sure she's probably in the middle of\x01",
            "inspecting the situation in the market.\x02\x03",

            "She took off after telling me to pray\x01",
            "for her too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x102,
        (
            "#019FI don't know how I should say this...but\x01",
            "the mayor seems like she has quite a\x01",
            "unique personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x103,
        (
            "#027F#4PHaha. Well, doesn't she sound\x01",
            "interesting. Even if she weren't the\x01",
            "mayor I'd be kind of intrigued.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        (
            "#620FThere is no doubt she's a capable person.\x01",
            "Although she does have a bit of an\x01",
            "unrestrained aspect to her at times.\x02\x03",

            "Anyway, I'm on my way to meet\x01",
            "her right now.\x02\x03",

            "I don't mean to sound impolite,\x01",
            "but would you mind waiting at\x01",
            "her residence?\x02\x03",

            "I will let her know you're there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#000FUm, I don't know how I feel about\x01",
            "going back there empty-handed...\x02\x03",

            "Would it be all right if we came\x01",
            "along with you instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xC,
        (
            "#622FCome with me to meet the mayor?\x01",
            "Well, I guess it's okay...\x02\x03",

            "#621FLet's make our way over to\x01",
            "the Bose Market, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x35, 0x1, 0x10)
    SetChrFlags(0xC, 0x40)
    OP_92(0xC, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    EventEnd(0x0)
    AddParty(0x33, 0xFF)
    SetMapFlags(0x1)

    label("loc_1F70")

    TalkEnd(0xC)
    Return()

    # Function_9_17F1 end

    SaveToFile()

Try(main)
