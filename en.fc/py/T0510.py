from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0510   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0510.x',
        MapIndex            = 18,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T0510   ._SN',
            'ED6_DT01/T0510_1 ._SN',
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
        'CWO Ashton',                           # 9
        'Warrant Officer Dyne',                 # 10
        'Target Camera',                        # 11
    )

    DeclEntryPoint(
        Unknown_00              = 24000,
        Unknown_04              = 0,
        Unknown_08              = 52000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56200,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 24100,
        Unknown_04              = 0,
        Unknown_08              = 56200,
        Unknown_0C              = 4,
        Unknown_0E              = 180,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 45,
        Unknown_34              = 45,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 18,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = 29850,
        Z                   = 0,
        Y                   = -73420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 26800,
        Z                   = 0,
        Y                   = 29900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 28310,
        TriggerZ            = 0,
        TriggerY            = -73420,
        TriggerRange        = 500,
        ActorX              = 29850,
        ActorZ              = 1500,
        ActorY              = -73420,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 28250,
        TriggerZ            = 0,
        TriggerY            = 29800,
        TriggerRange        = 500,
        ActorX              = 26800,
        ActorZ              = 1500,
        ActorY              = 29900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20640,
        TriggerZ            = 0,
        TriggerY            = 33000,
        TriggerRange        = 1000,
        ActorX              = 20640,
        ActorZ              = 1000,
        ActorY              = 33000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_20E",          # 00, 0
        "Function_1_233",          # 01, 1
        "Function_2_27D",          # 02, 2
        "Function_3_293",          # 03, 3
        "Function_4_298",          # 04, 4
        "Function_5_1B7C",         # 05, 5
        "Function_6_1B81",         # 06, 6
        "Function_7_24F6",         # 07, 7
    )


    def Function_0_20E(): pass

    label("Function_0_20E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (101, "loc_21A"),
        (SWITCH_DEFAULT, "loc_232"),
    )


    label("loc_21A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_22F")
    OP_28(0x8, 0x2, 0x4000)
    Event(1, 1)

    label("loc_22F")

    Jump("loc_232")

    label("loc_232")

    Return()

    # Function_0_20E end

    def Function_1_233(): pass

    label("Function_1_233")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_233 end

    def Function_2_27D(): pass

    label("Function_2_27D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_292")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_27D")

    label("loc_292")

    Return()

    # Function_2_27D end

    def Function_3_293(): pass

    label("Function_3_293")

    Call(0, 4)
    Return()

    # Function_3_293 end

    def Function_4_298(): pass

    label("Function_4_298")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_A6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_51(0xA, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xA, 0x3E8)

    ChrTalk(    #0
        0x8,
        (
            "Well, if it isn't Estelle...\x01",
            "and Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#000FHello, Mr. Ashton.\x02",
    )

    CloseMessageWindow()

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500")
    OP_A2(0x281)
    OP_A2(0x1)

    ChrTalk(    #2
        0x102,
        "#010FIt's been a while since we last met.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "Yes, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "So I've heard my boy, Luke, caused\x01",
            "you a lot of trouble, did he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "I'm absolutely ashamed as a father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#001FI'm sure it's perfectly normal for a\x01",
            "boy his age to be naughty like that.\x02\x03",

            "I mean, even I ran around outside\x01",
            "of town when I was young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#017FYeah, and you're supposed to\x01",
            "be a girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Ha ha, you're certainly full of\x01",
            "energy as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E6")

    ChrTalk(    #9
        0x8,
        (
            "And this is...Scherazard, if\x01",
            "I remember correctly, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        (
            "#020FGood afternoon, sir.\x02\x03",

            "We'd like to cross over into the\x01",
            "Bose region, so we were wondering\x01",
            "about getting a pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "Let me guess...this has something\x01",
            "to do with the Linde, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#003FYeah...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #13
        "\x07\x05Estelle explains that Cassius was aboard the missing airliner.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #14
        0x8,
        "Goodness, Cassius was aboard...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "This is major.\x01",
            "I'll issue you a pass right away.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)
    Sleep(500)
    TurnDirection(0x8, 0x0, 400)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_3E(0x32F, 1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #16
        "\x07\x00Received \x07\x02Gate Pass\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #17
        0x101,
        (
            "#001FThank you, sir.\x02\x03",

            "#000FBut is it all right if you issue us\x01",
            "a pass just like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "What are you talking about?\x01",
            "I know you kids by face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "And as a member of the Royal Army,\x01",
            "I should do my best to cooperate\x01",
            "with the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "Oh, but one other thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "Be careful if you have any errands\x01",
            "at the Haken Gate north of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "You might want to hide your\x01",
            "identities as bracers there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#012FWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "I'm sorry, but I can't say any more\x01",
            "about the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "But if you do intend to investigate\x01",
            "the incident, please do so with\x01",
            "discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "I pray to Aidios for Cassius'\x01",
            "safe return.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    OP_A2(0x303)
    Jump("loc_A6B")

    label("loc_9E6")


    ChrTalk(    #28
        0x8,
        (
            "But if you do intend to investigate\x01",
            "the incident, please do so with\x01",
            "discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "I pray to Aidios for Cassius'\x01",
            "safe return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6B")

    Jump("loc_1B78")

    label("loc_A6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1258")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x50, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E25")
    OP_A2(0x281)
    OP_A2(0x1)

    ChrTalk(    #30
        0x8,
        (
            "Well, if it isn't Estelle...\x01",
            "and Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#000FHello, Mr. Ashton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        "#010FIt's been a while since we last met.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "Yes, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "So I've heard my boy, Luke, caused\x01",
            "you a lot of trouble, did he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "I'm absolutely ashamed as a father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#001FI'm sure it's perfectly normal for a\x01",
            "boy his age to be naughty like that.\x02\x03",

            "#001FI mean, even I ran around outside\x01",
            "of town when I was young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x102,
        (
            "#017FYeah, and you're supposed to\x01",
            "be a girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "Ha ha, you're certainly full of\x01",
            "energy as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "That aside, it seems that the\x01",
            "Bose region has been hit by\x01",
            "a string of burglaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#002FBose has?\x01",
            "That's troubling to hear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x8,
        (
            "Yes it is. And it's for that reason\x01",
            "the garrison troops here need to get\x01",
            "it together as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "However, my men are entirely\x01",
            "too lax. There's no danger, so\x01",
            "they've gotten complacent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "It's unquestionably going to be a\x01",
            "chore instilling any values in my\x01",
            "men...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D8")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F43")
    OP_A2(0x0)

    ChrTalk(    #44
        0x8,
        (
            "It seems that the Bose region has\x01",
            "recently been hit by a string of\x01",
            "burglaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "And it's for that reason the garrison\x01",
            "troops here need to get it together\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "However, my men are entirely\x01",
            "too lax. There's no danger, so\x01",
            "they've gotten complacent.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_100C")

    label("loc_F43")


    ChrTalk(    #47
        0x8,
        (
            "With the sky bandit incident in Bose,\x01",
            "my garrison troops are really going\x01",
            "to need to get it together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "However, my men are entirely\x01",
            "too lax. There's no danger, so\x01",
            "they've gotten complacent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100C")

    Jump("loc_10D8")

    label("loc_100F")


    ChrTalk(    #49
        0x8,
        (
            "With the sky bandit incident in Bose,\x01",
            "my garrison troops are really going\x01",
            "to need to get it together...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "However, my men are entirely\x01",
            "too lax. There's no danger, so\x01",
            "they've gotten complacent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D8")

    Jump("loc_1255")

    label("loc_10DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BE")
    OP_A2(0x0)

    ChrTalk(    #51
        0x8,
        (
            "It seems that the Bose region has\x01",
            "been hit by a string of burglaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "We're really going to need to\x01",
            "get it together here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "I really want my men to use the\x01",
            "experience they've gained in\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1255")

    label("loc_11BE")


    ChrTalk(    #54
        0x8,
        (
            "It seems that the Bose region has\x01",
            "been hit by a string of burglaries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "I really want my men to use the\x01",
            "experience they've gained in\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1255")

    Jump("loc_1B78")

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1513")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1279")
    Call(1, 0)
    Jump("loc_1510")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1324")

    ChrTalk(    #56
        0x8,
        (
            "Though our positions may be\x01",
            "different, we are both here to\x01",
            "serve the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "Although I can't do much else,\x01",
            "I'll pray for success for the both\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_1324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1481")
    OP_A2(0x0)

    ChrTalk(    #58
        0x8,
        (
            "Thank you for your help with\x01",
            "the training. I'm sure it's been\x01",
            "a wake up call for my men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "I'm sorry to ask this, but when you\x01",
            "get back to town, please make sure\x01",
            "Luke stays out of trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "He's naughtier than the\x01",
            "typical boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "I'm sure his mother has her\x01",
            "hands full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "Maybe I should have raised\x01",
            "him more strictly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_1481")


    ChrTalk(    #63
        0x8,
        (
            "Luke's naughtier than the\x01",
            "typical boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "His mother probably has her\x01",
            "hands full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "I sorry to ask this, but please\x01",
            "look after Luke.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1510")

    Jump("loc_1B78")

    label("loc_1513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_1780")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x8, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1534")
    Call(1, 0)
    Jump("loc_177D")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15DF")

    ChrTalk(    #66
        0x8,
        (
            "Though our positions may be\x01",
            "different, we are both here to\x01",
            "serve the public.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "Although I can't do much else,\x01",
            "I'll pray for success for the both\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177D")

    label("loc_15DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CF")
    OP_A2(0x0)

    ChrTalk(    #68
        0x8,
        (
            "I had felt anxiety in the new\x01",
            "recruits, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "It looks like this training has done\x01",
            "some good to relieve a bit of that\x01",
            "uneasiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "It looks like I'll have to\x01",
            "shake up my men from time\x01",
            "to time to keep 'em sharp.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177D")

    label("loc_16CF")


    ChrTalk(    #71
        0x8,
        (
            "It looks like this training has done\x01",
            "some good to relieve a bit of that\x01",
            "uneasiness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "It looks like I'll have to\x01",
            "shake up my men from time\x01",
            "to time to keep 'em sharp.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177D")

    Jump("loc_1B78")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A26")
    OP_A2(0x281)
    OP_A2(0x0)

    ChrTalk(    #73
        0x8,
        (
            "Well, if it isn't Estelle...\x01",
            "and Joshua, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#000FHello, Mr. Ashton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        "#010FIt's been a while since we last met.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "Yes, it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "So I've heard my boy, Luke, caused\x01",
            "you a lot of trouble, did he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "I'm absolutely ashamed as a father.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#001FI'm sure it's perfectly normal for a\x01",
            "boy his age to be naughty like that.\x02\x03",

            "#001FI mean, even I ran around outside\x01",
            "of town when I was young.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x102,
        (
            "#017FYeah, and you're supposed to\x01",
            "be a girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "Ha ha, you're certainly full of\x01",
            "energy as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "I wish I could get back to Rolent\x01",
            "more often...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "It hasn't been long since I took\x01",
            "this post, and for the moment\x01",
            "there's a lot to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B78")

    label("loc_1A26")


    ChrTalk(    #84
        0x8,
        (
            "In the war ten years ago, the checkpoints\x01",
            "played an important role in dividing the\x01",
            "Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "Although few travelers come through\x01",
            "nowadays, we can't neglect our\x01",
            "defenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "Yet, the attitude of my new recruits\x01",
            "is less than desirable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "But since I've taken the post, I'll\x01",
            "need to whip them into shape at\x01",
            "least once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B78")

    TalkEnd(0x8)
    Return()

    # Function_4_298 end

    def Function_5_1B7C(): pass

    label("Function_5_1B7C")

    Call(0, 6)
    Return()

    # Function_5_1B7C end

    def Function_6_1B81(): pass

    label("Function_6_1B81")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1CC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C7E")
    OP_A2(0x2)

    ChrTalk(    #88
        0x9,
        (
            "I heard the missing airliner has\x01",
            "been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "It seems as though the Intelligence\x01",
            "Division and border garrison worked\x01",
            "together to resolve the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "Thank heavens, now I can finally\x01",
            "get back to my normal duties.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CC2")

    label("loc_1C7E")


    ChrTalk(    #91
        0x9,
        (
            "Thank heavens, now I can finally\x01",
            "get back to my normal duties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CC2")

    Jump("loc_24F2")

    label("loc_1CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1E5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD4")
    OP_A2(0x2)

    ChrTalk(    #92
        0x9,
        (
            "Although this hasn't been confirmed, it seems\x01",
            "that the border garrison AND the newly formed\x01",
            "Intelligence Division are on the move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "If this goes on much longer,\x01",
            "it'll look bad for the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "I guess we'll have to let them\x01",
            "do their work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E5C")

    label("loc_1DD4")


    ChrTalk(    #95
        0x9,
        (
            "Although this hasn't been confirmed, it seems\x01",
            "that the border garrison AND the newly formed\x01",
            "Intelligence Division are on the move.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E5C")

    Jump("loc_24F2")

    label("loc_1E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F40")
    OP_A2(0x2)

    ChrTalk(    #96
        0x9,
        (
            "It looks like the missing airliner\x01",
            "has finally been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "But we still haven't received a\x01",
            "command to cancel security\x01",
            "checks here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "What's going on? I really need\x01",
            "some concrete information.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCD")

    label("loc_1F40")


    ChrTalk(    #99
        0x9,
        (
            "It looks like the missing airliner\x01",
            "has finally been found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "But we still haven't received a\x01",
            "command to cancel security\x01",
            "checks here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCD")

    Jump("loc_24F2")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_21E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213C")
    OP_A2(0x2)

    ChrTalk(    #101
        0x9,
        (
            "Anyway, how does an entire\x01",
            "airliner just disappear...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        "Bizarre things happen I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "Although it seems like something\x01",
            "that big should be easy to find,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "I wonder if old General Morgan is\x01",
            "growing senile or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "Oh, I'd better not be caught talking\x01",
            "like that or the chief's gonna\x01",
            "have a field day with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E5")

    label("loc_213C")


    ChrTalk(    #106
        0x9,
        (
            "I wonder if old General Morgan is\x01",
            "growing senile or something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "Oh, I'd better not be caught talking\x01",
            "like that or the chief's gonna\x01",
            "have a field day with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E5")

    Jump("loc_24F2")

    label("loc_21E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 2)), scpexpr(EXPR_END)), "loc_22BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2279")
    OP_A2(0x2)

    ChrTalk(    #108
        0x9,
        (
            "It seems like the blockade on\x01",
            "the Eisen Road has been lifted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "The airliner hasn't been found,\x01",
            "so what's going on?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22BB")

    label("loc_2279")


    ChrTalk(    #110
        0x9,
        (
            "At any rate, I wonder when flights\x01",
            "are gonna start up again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22BB")

    Jump("loc_24F2")

    label("loc_22BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_END)), "loc_2460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B8")
    OP_A2(0x2)

    ChrTalk(    #111
        0x9,
        (
            "Still, what's up with prohibiting flights for\x01",
            "the entire region as well as blockading\x01",
            "the Eisen Road?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "Seems like they're really pulling\x01",
            "out all the stops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "It looks to me as if the border\x01",
            "garrison is in a big rush.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_245D")

    label("loc_23B8")


    ChrTalk(    #114
        0x9,
        (
            "Still, what's up with prohibiting flights for\x01",
            "the entire region as well as blockading\x01",
            "the Eisen Road?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "Seems like they're really pulling\x01",
            "out all the stops.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_245D")

    Jump("loc_24F2")

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_24F2")

    ChrTalk(    #116
        0x9,
        (
            "What do we have here this time?\x01",
            "Bracers? Traveling the roads on\x01",
            "foot is a bit of a hassle, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        "Well, be careful out there.\x02",
    )

    CloseMessageWindow()

    label("loc_24F2")

    TalkEnd(0x9)
    Return()

    # Function_6_1B81 end

    def Function_7_24F6(): pass

    label("Function_7_24F6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #118
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2711")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 20640, 1000, 33000, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x32)
    OP_73(0x1)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, 21970, 0, 33230, 269)
    SetChrPos(0x1, 21970, 0, 33230, 269)
    SetChrPos(0x2, 21970, 0, 33230, 269)
    SetChrPos(0x3, 21970, 0, 33230, 269)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 20640, 1000, 33000, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_272B")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_272B")

    Return()

    # Function_7_24F6 end

    SaveToFile()

Try(main)
