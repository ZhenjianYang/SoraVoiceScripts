from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1130   ._SN',
        MapName             = 'Bose',
        Location            = 'T1130.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 1,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1130_1 ._SN',
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
        'Father Holstein',                      # 9
        'Sister Rosa',                          # 10
        'Hardt',                                # 11
        'Lyril',                                # 12
        'Claire',                               # 13
        'Corna',                                # 14
        'Jacob',                                # 15
        'Sarah',                                # 16
        'Lila',                                 # 17
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
        'ED6_DT07/CH01120 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01000 ._CH',             # 06
        'ED6_DT07/CH01350 ._CH',             # 07
        'ED6_DT07/CH02370 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01400P._CP',             # 00
        'ED6_DT07/CH01410P._CP',             # 01
        'ED6_DT07/CH01120P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01000P._CP',             # 06
        'ED6_DT07/CH01350P._CP',             # 07
        'ED6_DT07/CH02370P._CP',             # 08
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 63070,
        Z                   = 0,
        Y                   = 48320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 56670,
        Z                   = 0,
        Y                   = 43550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 60350,
        Z                   = 0,
        Y                   = 45170,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 58930,
        Z                   = 0,
        Y                   = 44670,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 59980,
        Z                   = 0,
        Y                   = 46900,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 58180,
        Z                   = 0,
        Y                   = 45750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 61740,
        Z                   = 0,
        Y                   = 46550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 57200,
        Z                   = 0,
        Y                   = 47070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
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
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16410,
        TriggerZ            = 4000,
        TriggerY            = 43010,
        TriggerRange        = 800,
        ActorX              = 16410,
        ActorZ              = 5200,
        ActorY              = 43010,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_2F1",          # 01, 1
        "Function_2_344",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_FFC",          # 04, 4
        "Function_5_174A",         # 05, 5
        "Function_6_1929",         # 06, 6
        "Function_7_19B7",         # 07, 7
        "Function_8_1C35",         # 08, 8
        "Function_9_1CAA",         # 09, 9
        "Function_10_1E67",        # 0A, 10
        "Function_11_1F71",        # 0B, 11
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_269")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_2F0")

    label("loc_269")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_278")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_2F0")

    label("loc_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_282")
    Jump("loc_2F0")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_291")
    SetChrFlags(0x9, 0x80)
    Jump("loc_2F0")

    label("loc_291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2A5")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_2F0")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2DD")
    OP_64(0x0, 0x1)
    SetChrPos(0x8, 59100, 0, 48100, 180)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_2F0")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2F0")
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x9, 0xA, 0)

    label("loc_2F0")

    Return()

    # Function_0_25A end

    def Function_1_2F1(): pass

    label("Function_1_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_303")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)

    label("loc_303")

    OP_64(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x80)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x1, 0x100)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x78, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32E")
    OP_65(0x1, 0x1)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_343")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_343")
    OP_64(0x0, 0x1)

    label("loc_343")

    Return()

    # Function_1_2F1 end

    def Function_2_344(): pass

    label("Function_2_344")

    Call(0, 3)
    Return()

    # Function_2_344 end

    def Function_3_349(): pass

    label("Function_3_349")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_462")

    ChrTalk(    #0
        0x8,
        (
            "It seems some light has finally come\x01",
            "to shine upon the faces of the people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "The steps of the people passing\x01",
            "by seem to have grown lighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "Ha! A good sign, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "It is the strength of this city to\x01",
            "recover quickly from difficult times.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4D1")

    label("loc_462")


    ChrTalk(    #4
        0x8,
        (
            "It seems some light has finally come\x01",
            "to shine upon the faces of the people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "Ha! A good sign, indeed.\x02",
    )

    CloseMessageWindow()

    label("loc_4D1")

    Jump("loc_FF8")

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_644")

    ChrTalk(    #6
        0x8,
        (
            "No, indeed. It was quite the terrible\x01",
            "time last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "The troubled citizens burst into the guild\x01",
            "and mayor's house alike, and spent the\x01",
            "entire night making quite the fuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Mayor Maybelle's powers of persuasion\x01",
            "thankfully averted further turmoil, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "I've come to realize anew the immense\x01",
            "effect orbments have on our lives.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_6D1")

    label("loc_644")


    ChrTalk(    #10
        0x8,
        (
            "No, indeed, it was quite the terrible\x01",
            "time last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "I've come to appreciate anew the immense\x01",
            "effect orbments have on our lives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D1")

    Jump("loc_FF8")

    label("loc_6D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_774")

    ChrTalk(    #12
        0x8,
        "Finally, peace has returned to the Bose region.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "From what I hear, even Ravennue's orchards\x01",
            "are recovering. This is a great blessing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A6")

    label("loc_774")


    ChrTalk(    #14
        0x8,
        "Finally, peace has returned to the Bose region.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "The market has reopened safely, and\x01",
            "Ravennue's orchards are recovering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "While it will take time to restore our lives,\x01",
            "we will succeed. There's no doubt of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "After all, we recovered so wonderfully\x01",
            "even from the tragedy of that war.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8A6")

    Jump("loc_FF8")

    label("loc_8A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9D7")

    ChrTalk(    #18
        0x8,
        "Mayor Maybelle is working herself ragged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "It is slightly concerning that she does not\x01",
            "seem to acknowledge the considerable burden\x01",
            "she's placed upon herself, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "But, all people are like that when they're\x01",
            "young. Even I did some crazy things in my\x01",
            "youth! Ho ho ho...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B4D")

    label("loc_9D7")


    ChrTalk(    #21
        0x8,
        "Mayor Maybelle is working herself ragged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "She is living up to the heritage established\x01",
            "by her father, through and through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "It is slightly concerning that she does not\x01",
            "seem to acknowledge the considerable burden\x01",
            "she's placed upon herself, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "But, all people are like that when they're\x01",
            "young. Even I did some crazy things in my\x01",
            "youth! Ho ho ho...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B4D")

    Jump("loc_FF8")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_CE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BFB")

    ChrTalk(    #25
        0x8,
        (
            "It seems the maid from the mayor's household\x01",
            "still hasn't regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "I've treated her with every medicine I know,\x01",
            "but to no avail.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE6")

    label("loc_BFB")


    ChrTalk(    #27
        0x8,
        (
            "Unfortunately, the maid from the mayor's household\x01",
            "still hasn't regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "I've treated her with every medicine I know,\x01",
            "but to no avail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "All we can do is wait for good news from\x01",
            "the sister in attendance.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CE6")

    Jump("loc_FF8")

    label("loc_CE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_DEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D5B")

    ChrTalk(    #30
        0x8,
        "Everyone, please, calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "The Goddess shall protect you\x01",
            "until the Royal Army comes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DE8")

    label("loc_D5B")


    ChrTalk(    #32
        0x8,
        "Everyone, please, calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "The Royal Army will surely be arriving shortly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        "Until then, the Goddess shall protect us all!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_DE8")

    Jump("loc_FF8")

    label("loc_DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_FF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EA3")

    ChrTalk(    #35
        0x8,
        (
            "Thanks to the market, anyone who can get\x01",
            "permission can have a shop of their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        (
            "Ho ho, I understand why so many entrepreneurial\x01",
            "spirits come to this land.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FF8")

    label("loc_EA3")


    ChrTalk(    #37
        0x8,
        (
            "The city of merchants, Bose, has taken great care\x01",
            "to protect its business for many generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "And the market here is easily the greatest\x01",
            "example of that nurturing care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "After all, anyone who can get permission\x01",
            "can start a shop of their own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "Ho ho, I understand why so many entrepreneurial\x01",
            "spirits come to this land.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FF8")

    TalkEnd(0x8)
    Return()

    # Function_3_349 end

    def Function_4_FFC(): pass

    label("Function_4_FFC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_11D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1137")

    ChrTalk(    #41
        0xFE,
        "The market's back to how it used to be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "When I pass by it, I can hear a hum\x01",
            "of joyous voices coming from within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I'm sure Mayor Maybelle feels her efforts\x01",
            "overseeing things were well rewarded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I should hope so, anyway, since she skipped\x01",
            "church services to direct things.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_11D0")

    label("loc_1137")


    ChrTalk(    #45
        0xFE,
        (
            "To leave a church service partway through\x01",
            "is an inexcusable affront.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "If the mayor is so faithless, it sets\x01",
            "a bad example for the whole church.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D0")

    Jump("loc_1746")

    label("loc_11D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134C")

    ChrTalk(    #47
        0xFE,
        (
            "...To think, simply having orbments fail\x01",
            "could cause so much chaos...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "As we who possess faith in the Goddess,\x01",
            "we should be ashamed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "To rely on something like orbments so heavily\x01",
            "is a sign of great weakness. Faith in the\x01",
            "Goddess should be more than enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "I hope that people take this as an epiphany\x01",
            "of sorts, and come to their senses!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1422")

    label("loc_134C")


    ChrTalk(    #51
        0xFE,
        (
            "To rely on something like orbments so heavily\x01",
            "is a sign of great weakness. Faith in the\x01",
            "Goddess should be more than enough!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I hope that people take this as an epiphany\x01",
            "of sorts, and come to their senses!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1422")

    Jump("loc_1746")

    label("loc_1425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_15DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14BE")

    ChrTalk(    #53
        0xFE,
        (
            "The market reopens today, and Bose\x01",
            "returns to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Shopping is a luxury which may only be\x01",
            "truly enjoyed in times of peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15DC")

    label("loc_14BE")


    ChrTalk(    #55
        0xFE,
        (
            "The market reopens today, and Bose\x01",
            "returns to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It's somewhat troubling that so few people\x01",
            "have come to offer prayers of thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "Shopping is a luxury which may only be\x01",
            "truly enjoyed in times of peace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "...I suppose I can overlook it, though.\x01",
            "Just this once.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_15DC")

    Jump("loc_1746")

    label("loc_15DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1746")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_169C")

    ChrTalk(    #59
        0xFE,
        (
            "Many come to our church to pray\x01",
            "for success in business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "*sigh* Such selfish 'prayers.' Do they not\x01",
            "think it a rude thing to request of our\x01",
            "Goddess? Our creator?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1746")

    label("loc_169C")


    ChrTalk(    #61
        0xFE,
        "The person over there, praying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "He came to petition the Goddess\x01",
            "for success in business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Does he not think it is rude to offer up\x01",
            "such crude prayers?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1746")

    TalkEnd(0x9)
    Return()

    # Function_4_FFC end

    def Function_5_174A(): pass

    label("Function_5_174A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_182A")

    ChrTalk(    #64
        0xFE,
        (
            "I came to offer prayers, and wish for\x01",
            "success in my new business venture.\x02\x03",

            "But that sister's been glaring\x01",
            "over at me for a while now. She\x01",
            "seems astoundingly unwelcoming.\x02\x03",

            "D-Did I do something wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1925")

    label("loc_182A")


    ChrTalk(    #65
        0xFE,
        (
            "I'm going to get back to work\x01",
            "at the market shortly.\x02\x03",

            "But right now, I'm praying here to ask\x01",
            "for success in business.\x02\x03",

            "But that sister's been glaring\x01",
            "over at me for a while now. She\x01",
            "seems astoundingly unwelcoming.\x02\x03",

            "D-Did I do something wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1925")

    TalkEnd(0xA)
    Return()

    # Function_5_174A end

    def Function_6_1929(): pass

    label("Function_6_1929")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_19B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_194F")

    ChrTalk(    #66
        0xFE,
        "*sniffle*...\x02",
    )

    CloseMessageWindow()
    Jump("loc_19B3")

    label("loc_194F")


    ChrTalk(    #67
        0xFE,
        "Suddenly it got super dark in the market...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "It...was really scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "*sniffle*...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_19B3")

    TalkEnd(0xB)
    Return()

    # Function_6_1929 end

    def Function_7_19B7(): pass

    label("Function_7_19B7")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A9A")

    ChrTalk(    #70
        0xFE,
        (
            "I've come for the first time in a while\x01",
            "to offer prayers to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Somehow, my feet just didn't\x01",
            "lead me to the market...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "I can't find it in me to enjoy\x01",
            "shopping at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1B0F")

    label("loc_1A9A")


    ChrTalk(    #73
        0xFE,
        (
            "I've come for the first time in a while\x01",
            "to offer prayers to the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "I need to quiet my heart a bit...\x02",
    )

    CloseMessageWindow()

    label("loc_1B0F")

    Jump("loc_1C31")

    label("loc_1B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1B7E")

    ChrTalk(    #75
        0xFE,
        (
            "Apparently it was a terrifying monster\x01",
            "that attacked the market, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "How awful!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C31")

    label("loc_1B7E")


    ChrTalk(    #77
        0xFE,
        (
            "Apparently it was a terrifying monster\x01",
            "that attacked the market, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "To think that something like that is still\x01",
            "flying around at this very moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "How awful!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1C31")

    TalkEnd(0xC)
    Return()

    # Function_7_19B7 end

    def Function_8_1C35(): pass

    label("Function_8_1C35")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1CA6")

    ChrTalk(    #80
        0xFE,
        (
            "To think a giant monster like that\x01",
            "would attack the market...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Ahh, I hope that girl is safe.\x02",
    )

    CloseMessageWindow()

    label("loc_1CA6")

    TalkEnd(0xD)
    Return()

    # Function_8_1C35 end

    def Function_9_1CAA(): pass

    label("Function_9_1CAA")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1E63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1D59")

    ChrTalk(    #82
        0xFE,
        "So...what the heck was that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "It looked almost like a dragon. Like the\x01",
            "kind they talk about in ancient legends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "But...there's no way, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E63")

    label("loc_1D59")


    ChrTalk(    #85
        0xFE,
        "That thing flew in from the east.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Just as I caught a glimpse of it, whoosh,\x01",
            "there it was, right above the market!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "The wind coming off of it was really\x01",
            "intense, too. I felt like I was going\x01",
            "to get blown away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I hope the mayor's maid is okay...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1E63")

    TalkEnd(0xE)
    Return()

    # Function_9_1CAA end

    def Function_10_1E67(): pass

    label("Function_10_1E67")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1F6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1ED9")

    ChrTalk(    #89
        0xFE,
        "I came to pray while I was out shopping.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "...Specifically, for Lila to wake up soon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F6D")

    label("loc_1ED9")


    ChrTalk(    #91
        0xFE,
        "I came to pray while I was out shopping.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "...Specifically, for Lila to wake up soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "*sigh* I hope my prayers reach the Goddess...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1F6D")

    TalkEnd(0xF)
    Return()

    # Function_10_1E67 end

    def Function_11_1F71(): pass

    label("Function_11_1F71")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2088")

    ChrTalk(    #94
        0x10,
        (
            "#620FMiss Maybelle is overseeing things\x01",
            "at the market.\x02\x03",

            "In other words, as always, she's\x01",
            "skipping out on her prayers.\x02\x03",

            "Given the current situation, I can't\x01",
            "really scold her too much, but...\x02\x03",

            "...when everything settled, I intend\x01",
            "to have her pay these debts.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2103")

    label("loc_2088")


    ChrTalk(    #95
        0x10,
        (
            "#620FMiss Maybelle is overseeing things\x01",
            "at the market.\x02\x03",

            "In other words, as always, she's\x01",
            "skipping out on her prayers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2103")

    TalkEnd(0x10)
    Return()

    # Function_11_1F71 end

    SaveToFile()

Try(main)
