from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2600   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'Anton',                                # 9
        'Ricky',                                # 10
        'Mickey',                               # 11
        'Target Camera',                        # 12
        'Academy - Back Road',                  # 13
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
        'ED6_DT07/CH02900 ._CH',             # 00
        'ED6_DT26/CH20783 ._CH',             # 01
        'ED6_DT07/CH01080 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02900P._CP',             # 00
        'ED6_DT26/CH20783P._CP',             # 01
        'ED6_DT07/CH01080P._CP',             # 02
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 170,
        Z                   = 0,
        Y                   = -16239,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1000,
        TriggerY            = 9720,
        TriggerRange        = 800,
        ActorX              = 0,
        ActorZ              = 2000,
        ActorY              = 9720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_186",          # 00, 0
        "Function_1_24B",          # 01, 1
        "Function_2_270",          # 02, 2
        "Function_3_3ED",          # 03, 3
        "Function_4_411",          # 04, 4
        "Function_5_991",          # 05, 5
        "Function_6_DB3",          # 06, 6
        "Function_7_F47",          # 07, 7
        "Function_8_135E",         # 08, 8
    )


    def Function_0_186(): pass

    label("Function_0_186")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1C8")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 200, 500, 4560, 180)
    SetChrPos(0x11, -640, 750, 5900, 180)
    Jump("loc_24A")

    label("loc_1C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1D2")
    Jump("loc_24A")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1E1")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_24A")

    label("loc_1E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_217")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 200, 500, 4560, 0)
    SetChrPos(0x11, -640, 750, 5900, 180)
    Jump("loc_24A")

    label("loc_217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_24A")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 200, 500, 4560, 0)
    SetChrPos(0x11, -550, 750, 5900, 180)

    label("loc_24A")

    Return()

    # Function_0_186 end

    def Function_1_24B(): pass

    label("Function_1_24B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE61F0, 0x23004E)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_71(0x2, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    Return()

    # Function_1_24B end

    def Function_2_270(): pass

    label("Function_2_270")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3D7")

    label("loc_295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3D7")

    label("loc_2AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3D7")

    label("loc_2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3D7")

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3D7")

    label("loc_2F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_312")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3D7")

    label("loc_312")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3D7")

    label("loc_32B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3D7")

    label("loc_344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3D7")

    label("loc_35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_376")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3D7")

    label("loc_376")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3D7")

    label("loc_38F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3D7")

    label("loc_3A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3D7")

    label("loc_3C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3D7")

    label("loc_3EC")

    Return()

    # Function_2_270 end

    def Function_3_3ED(): pass

    label("Function_3_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_410")
    OP_8D(0xFE, -1300, 1420, 1300, -1760, 2000)
    Jump("Function_3_3ED")

    label("loc_410")

    Return()

    # Function_3_3ED end

    def Function_4_411(): pass

    label("Function_4_411")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_5AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_47F")

    ChrTalk(    #0
        0xFE,
        "I'm feeling really bright today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Good morning, sunlight! Good morning, new day!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A7")

    label("loc_47F")


    ChrTalk(    #2
        0xFE,
        "Last night, I found a tiny flower in the moonlight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Seeing it try its hardest to bloom despite its\x01",
            "small size just made me feel like my worries\x01",
            "are all so silly. Weird, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "It made me feel...at ease with the world.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "What have I been wasting all this time worrying\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_5A7")

    Jump("loc_98D")

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_5B4")
    Jump("loc_98D")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_5BE")
    Jump("loc_98D")

    label("loc_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_7F2")
    OP_8C(0xFE, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_65E")

    ChrTalk(    #6
        0xFE,
        (
            "Ricky's always trying to find ways to avoid\x01",
            "answering my questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I bet deep down, he finds all my woes funny\x01",
            "or something!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF")

    label("loc_65E")


    ChrTalk(    #8
        0xFE,
        "Why won't you say anything, Ricky?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Are you okay with the two of us staying like\x01",
            "this forever?! Well?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        "Give it a rest, Anton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        "Nothing you're saying makes any sense.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "That's what you always say, Ricky!\x01",
            "You're always trying to avoid answering\x01",
            "my questions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Refusing to face up to things isn't going\x01",
            "to get you anywhere in life, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "You'll just end up a loser!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7EF")

    Jump("loc_98D")

    label("loc_7F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_98D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_END)), "loc_989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8CB")

    ChrTalk(    #15
        0xFE,
        (
            "I should've known me being able to come\x01",
            "here was too good to be true...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "*sigh* All I was being set up for was a fall.\x01",
            "I almost wish I hadn't passed the exam to\x01",
            "come here after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_986")

    label("loc_8CB")


    ChrTalk(    #17
        0xFE,
        (
            "*sigh* I was so excited when I found out\x01",
            "I could attend here, and look at me now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "I feel like I'm being toyed with at this point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Fate just has it in for me... *sigh*\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_986")

    Jump("loc_98D")

    label("loc_989")

    Call(0, 7)

    label("loc_98D")

    TalkEnd(0xFE)
    Return()

    # Function_4_411 end

    def Function_5_991(): pass

    label("Function_5_991")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A52")

    ChrTalk(    #20
        0xFE,
        "Anton ran off somewhere, but he's back now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "He says he's fine, but I'm not sure I buy it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Haha. I've heard that a whooole lot of times\x01",
            "before this, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AAA")

    label("loc_A52")


    ChrTalk(    #23
        0xFE,
        "*yaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Hey there. Nice weather, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Wonder what I should do today?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_AAA")

    Jump("loc_DAF")

    label("loc_AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_AB7")
    Jump("loc_DAF")

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_AC1")
    Jump("loc_DAF")

    label("loc_AC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B20")

    ChrTalk(    #26
        0xFE,
        "Calm down, Anton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Whining like this isn't going to change anything.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA7")

    label("loc_B20")


    ChrTalk(    #28
        0xFE,
        "Anton's started whining again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "He doesn't seem to realize that won't help his\x01",
            "situation any...and he probably never will.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BA7")

    Jump("loc_DAF")

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_DAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C96")

    ChrTalk(    #30
        0xFE,
        (
            "For some bizarre reason, Anton decided to major\x01",
            "in social studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Haha. I told him enrolling in a course where you\x01",
            "have to do that much memorization was only\x01",
            "going to end badly for him, but he didn't listen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAF")

    label("loc_C96")


    ChrTalk(    #32
        0xFE,
        "Hey there! You look like you're in a hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Oh, you're looking for social studies students?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "There's one standing right here: Anton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Personally, I think he made a major mistake\x01",
            "picking that course in the first place, though.\x01",
            "He's not built for all that work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DAF")

    TalkEnd(0xFE)
    Return()

    # Function_5_991 end

    def Function_6_DB3(): pass

    label("Function_6_DB3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E5C")

    ChrTalk(    #36
        0xFE,
        (
            "It feels like wherever I go lately, Mr. Effort\x01",
            "isn't far behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Eeep... I hope it's just a coincidence and he isn't\x01",
            "onto me or something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F43")

    label("loc_E5C")


    ChrTalk(    #38
        0xFE,
        (
            "There was me thinking I'd be able to enjoy taking\x01",
            "it easy back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "But now Mr. Effort's on the road out front,\x01",
            "so now I'm actually stuck here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Ugh... It's not as fun when you're here\x01",
            "just 'cause you have to be.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_F43")

    TalkEnd(0xFE)
    Return()

    # Function_6_DB3 end

    def Function_7_F47(): pass

    label("Function_7_F47")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    OP_8C(0x10, 0, 0)
    Fade(1000)
    SetChrSubChip(0x10, 0)
    OP_6D(1330, 250, 4710, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(252, 0)
    SetChrPos(0x105, 200, 250, 3320, 0)
    Sleep(1000)

    ChrTalk(    #41
        0x10,
        "#11PHey, Ricky...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        "#11PWhy are we here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#11PSpring has come, and yet in my heart,\x01",
            "it's still the middle of winter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "#11P*sigh* Why does everything in my life\x01",
            "have to go wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        "#044F#12PUmm... Excuse me...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 180, 400)
    Sleep(300)

    ChrTalk(    #46
        0x10,
        "#5POh, I know you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#5PYou're the transfer student, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#5P*sigh* I wish I was smart like you...\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #49
        0x105,
        (
            "#043F#12PU-Umm...\x02\x03",

            "#045FMs. Wiola told me to deliver this to you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #50
        "\x07\x05Kloe handed Anton a printout.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #51
        0x10,
        "#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#5P*sigh* I shouldn't even need this. I should\x01",
            "have graduated...but here I am redoing the\x01",
            "year again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        "#044F#12PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#5PI can't believe I have to do my third year all\x01",
            "over again... This is the worst...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        (
            "#5PI was so full of hope when I first enrolled here,\x01",
            "and look at me now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x105,
        (
            "#043F#12PU-Umm...\x02\x03",

            "#540F(I-I'm not sure what to say in this situation...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F66)
    EventEnd(0x0)
    Return()

    # Function_7_F47 end

    def Function_8_135E(): pass

    label("Function_8_135E")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #57
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_135E end

    SaveToFile()

Try(main)
