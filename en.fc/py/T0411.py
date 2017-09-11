from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0411   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0411.x',
        MapIndex            = 13,
        MapDefaultBGM       = "ed60084",
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
        'Tio',                                  # 9
        'Will',                                 # 10
        'Chere',                                # 11
        'Franz',                                # 12
        'Hannah',                               # 13
        'Target Camera',                        # 14
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
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
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
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
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02480 ._CH',             # 00
        'ED6_DT07/CH01060 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02480P._CP',             # 00
        'ED6_DT07/CH01060P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 24300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -39050,
        Z                   = 0,
        Y                   = 33240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 1270,
        Z                   = 0,
        Y                   = 37600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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


    ScpFunction(
        "Function_0_1DE",          # 00, 0
        "Function_1_30A",          # 01, 1
        "Function_2_30B",          # 02, 2
        "Function_3_321",          # 03, 3
        "Function_4_377",          # 04, 4
        "Function_5_430",          # 05, 5
        "Function_6_470",          # 06, 6
        "Function_7_551",          # 07, 7
        "Function_8_5B0",          # 08, 8
        "Function_9_620",          # 09, 9
        "Function_10_6CE",         # 0A, 10
        "Function_11_16EB",        # 0B, 11
        "Function_12_16FA",        # 0C, 12
        "Function_13_170C",        # 0D, 13
        "Function_14_191C",        # 0E, 14
    )


    def Function_0_1DE(): pass

    label("Function_0_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_END)), "loc_218")
    SetChrPos(0x9, -77350, 0, -1160, 270)
    SetChrPos(0xA, -71660, 0, 2710, 0)
    SetChrPos(0x8, 2700, 0, 34460, 180)

    label("loc_218")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_22C"),
        (112, "loc_2F1"),
        (113, "loc_2F1"),
        (SWITCH_DEFAULT, "loc_309"),
    )


    label("loc_22C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_294")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x101, -70500, 0, -32040, 287)
    SetChrPos(0x102, -70500, 0, -32040, 287)
    OP_6D(-77800, 0, -31130, 0)
    Event(0, 14)
    Jump("loc_2EE")

    label("loc_294")

    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x101, -74500, 0, 2590, 0)
    SetChrPos(0x102, 735, 0, 23000, 0)
    OP_6D(700, 0, 30000, 0)
    TurnDirection(0xA, 0x1, 0)
    TurnDirection(0x9, 0x1, 0)
    FadeToBright(1000, 0)
    Event(0, 10)

    label("loc_2EE")

    Jump("loc_309")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_306")
    OP_A2(0x232)
    OP_28(0x2, 0x1, 0x20)
    Event(0, 13)

    label("loc_306")

    Jump("loc_309")

    label("loc_309")

    Return()

    # Function_0_1DE end

    def Function_1_30A(): pass

    label("Function_1_30A")

    Return()

    # Function_1_30A end

    def Function_2_30B(): pass

    label("Function_2_30B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_320")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_30B")

    label("loc_320")

    Return()

    # Function_2_30B end

    def Function_3_321(): pass

    label("Function_3_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_END)), "loc_34E")

    label("loc_328")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_8D(0xFE, 560, 22800, 2860, 25700, 3000)
    Jump("loc_328")

    label("loc_34B")

    Jump("loc_376")

    label("loc_34E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0x640)
    Sleep(1000)
    Jump("loc_34E")

    label("loc_376")

    Return()

    # Function_3_321 end

    def Function_4_377(): pass

    label("Function_4_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_END)), "loc_3A4")

    label("loc_37E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A1")
    OP_8D(0xFE, -1400, 22900, 2600, 25700, 4000)
    Jump("loc_37E")

    label("loc_3A1")

    Jump("loc_42F")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42F")
    OP_8E(0xFE, 0x0, 0x0, 0x5EEC, 0xBB8, 0x0)
    OP_8E(0xFE, 0x0, 0x0, 0x5B04, 0xBB8, 0x0)
    OP_8E(0xFE, 0x0, 0x0, 0x5EEC, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x102, 0)
    OP_96(0xFE, 0x6C2, 0x0, 0x5EEC, 0x258, 0x640)
    TurnDirection(0xFE, 0x102, 300)
    OP_96(0xFE, 0x0, 0x0, 0x5EEC, 0x258, 0x640)
    TurnDirection(0xFE, 0x102, 300)
    Jump("loc_3A4")

    label("loc_42F")

    Return()

    # Function_4_377 end

    def Function_5_430(): pass

    label("Function_5_430")

    TalkBegin(0x8)

    ChrTalk(    #0
        0xFE,
        "It's dark outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Please be careful, you two.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_5_430 end

    def Function_6_470(): pass

    label("Function_6_470")

    TalkBegin(0xA)
    TurnDirection(0xFE, 0x102, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "Umm, um...are you gonna kill\x01",
            "the bad monsters, Joshua?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Aren't you scared?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        (
            "#010FNo, I'm fine.\x01",
            "This is what bracers do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "You're so brave, Joshua...\x02",
    )

    CloseMessageWindow()
    Jump("loc_54D")

    label("loc_52D")


    ChrTalk(    #6
        0xFE,
        "You're so brave, Joshua...\x02",
    )

    CloseMessageWindow()

    label("loc_54D")

    TalkEnd(0xA)
    Return()

    # Function_6_470 end

    def Function_7_551(): pass

    label("Function_7_551")

    TalkBegin(0x9)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #7
        0xFE,
        (
            "It was really fun playing with\x01",
            "you, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Let's play again sometime.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_7_551 end

    def Function_8_5B0(): pass

    label("Function_8_5B0")

    TalkBegin(0xB)

    ChrTalk(    #9
        0xFE,
        (
            "The monsters we saw before didn't\x01",
            "seem vicious, just quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "At any rate, be careful out there.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xB)
    Return()

    # Function_8_5B0 end

    def Function_9_620(): pass

    label("Function_9_620")

    TalkBegin(0xC)

    ChrTalk(    #11
        0xFE,
        (
            "I had heard from Tio that you were\x01",
            "training to become bracers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "But I never imagined that it would\x01",
            "be you who were dispatched here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Please be careful.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_9_620 end

    def Function_10_6CE(): pass

    label("Function_10_6CE")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_1D(0x54)
    EventBegin(0x0)
    OP_6D(460, 0, 35390, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    TurnDirection(0x102, 0xA, 0)
    OP_6D(460, 0, 24000, 5000)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x8, 0x101, 0)
    Fade(1000)
    SetChrChipByIndex(0x101, 5)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, -74100, 350, 2590, 270)
    OP_6D(-75700, 0, 3000, 0)
    OP_6B(2800, 0)
    OP_44(0x102, 0xFF)
    Sleep(1000)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)

    ChrTalk(    #14
        0x101,
        (
            "#001FOh, that was delicious!\x02\x03",

            "#001FYour mom's cooking is as good\x01",
            "as ever, Tio!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#5PHa ha. That's because she gets\x01",
            "excited to cook whenever we have\x01",
            "guests over for meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#5PI feel really bad for Joshua,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#5P...with the little ones jumping\x01",
            "all over him like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#000FAh ha ha.\x01",
            "It's probably a good thing.\x02\x03",

            "#000FSurprisingly enough, kids tend\x01",
            "to latch on to him a lot.\x02\x03",

            "#000FIf anything, I'm more blown away by the\x01",
            "fact that the children enjoy playing\x01",
            "with such a stick-in-the-mud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#5PI think that's a bit of an over-\x01",
            "exaggeration, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#5PHe's definitely courteous and\x01",
            "maybe even a tad reserved, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#5PIf you get to know him,\x01",
            "he's really a caring young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#5PThe fact that he's not self-conscious\x01",
            "about it, too, gives him points in\x01",
            "my book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#505FYou really think so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "#5PThink about it. With those striking\x01",
            "facial features, mysterious amber\x01",
            "eyes and lush black hair...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#5PIt's only natural that he'd be a\x01",
            "target for all the young girls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#004F...\x02\x03",

            "#004FIs Joshua really that popular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "#5P...Are you blind, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "#5PRumor has it that more than just\x01",
            "a few girls have asked to go out\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "#5PI hear that he turned them all\x01",
            "down though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#007FI-I had no idea...\x02\x03",

            "#509FJoshua never said a word to me\x01",
            "about it...\x02\x03",

            "#509FI don't know how I should even begin to describe\x01",
            "his secretive nature after hearing this, but\x01",
            "how utterly cruel of him not to confide in me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#5PIf you were a boy, I imagine it would be a\x01",
            "different story, but as a girl, I don't think\x01",
            "that's something he would talk to you about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#5PAnd the fact that you haven't\x01",
            "fallen for him yourself is\x01",
            "beyond me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#004FHuh? Why would I?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x102, -37400, 0, -3350, 0)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #34
        0x102,
        (
            "Estelle, you're in there,\x01",
            "aren't you?\x02\x03",

            "It's about time to do our rounds.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #35
        0x101,
        "#004FA-All right! I'm coming!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(100)
    SetChrChipByIndex(0x101, 65535)
    OP_96(0x101, 0xFFFEDBB2, 0x0, 0x8D4, 0x258, 0x1770)
    ClearChrFlags(0x101, 0x4)

    ChrTalk(    #36
        0x101,
        (
            "#2P#006FI'll be back after Joshua and\x01",
            "I get the job done, Tio.\x02\x03",

            "I'd like to continue this\x01",
            "conversation then, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#5POh, all right.\x01",
            "Be careful out there, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFEDBF8, 0x0, 0x500, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFEE7CE, 0x0, 0xFFFFFD03, 0xBB8, 0x0)
    OP_8E(0x101, 0xFFFEF3A4, 0x0, 0xFFFFFB14, 0xBB8, 0x0)
    SetChrPos(0x101, -37500, 0, -1980, 0)
    OP_22(0x6, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #38
        0x8,
        (
            "#5PThat girl... She's either completely\x01",
            "out of touch with matters of the\x01",
            "heart or just plain dense...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#5PPoor Joshua. He really has\x01",
            "his work cut out for him.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x0, 0x1, 0)
    TurnDirection(0x1, 0x0, 0)
    Fade(1000)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_6D(-37800, 0, -2850, 0)
    OP_6B(2600, 0)
    Sleep(1000)

    ChrTalk(    #40
        0x102,
        (
            "#010FIt seems as though the monsters\x01",
            "always show up at about this time.\x02\x03",

            "#010FWe'd better get outside\x01",
            "and take a look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#509F... (Grrr...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#014FWh-What's going on, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#009FI've gotta ask, Joshua.\x02\x03",

            "#009FYou don't happen to...have any\x01",
            "secrets you're not telling me\x01",
            "about, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#014FCome on now.\x02\x03",

            "#014FWhere are you coming up\x01",
            "with this stuff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#003FSince you came to live with us...\x01",
            "we've always done everything\x01",
            "together, right?\x02\x03",

            "#003FEven though we've had our fair\x01",
            "share of fights...they're all good\x01",
            "memories for me now and...\x02\x03",

            "#003FWhat I mean to say is, I've come\x01",
            "to think of you as 'family' in every\x01",
            "sense of the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        "#010FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#002FSo...if there's ever anything on\x01",
            "your mind you'd like to talk about,\x01",
            "I'm available to lend an ear!\x02\x03",

            "#007FYou know, about things like...\x02\x03",

            "#503FTrouble with your love life and\x01",
            "whatnot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#018F...What are you trying to say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#008FN-Nothing! I just wanted to let you\x01",
            "know that I'm here to listen if you\x01",
            "need someone to talk to, that's all!\x02\x03",

            "Let's hurry up and get out there\x01",
            "so we can kick some monster butt!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1, 0x1, 0x0, 0xB)
    OP_8E(0x101, 0xFFFF6AB4, 0x0, 0xFFFFF2B8, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFF68E8, 0x0, 0xFFFFD012, 0x1770, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(    #50
        0x102,
        (
            "#017FWhat kind of nonsense is Tio\x01",
            "putting into that girl's head?\x02\x03",

            "#013F...\x02\x03",

            "#013F...Secrets, huh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x230)
    OP_28(0x2, 0x1, 0x8)
    FadeToDark(1000, 0, -1)
    NewScene("ED6_DT01/T0401   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_10_6CE end

    def Function_11_16EB(): pass

    label("Function_11_16EB")

    OP_8C(0x102, 315, 400)
    OP_8C(0x102, 180, 400)
    Return()

    # Function_11_16EB end

    def Function_12_16FA(): pass

    label("Function_12_16FA")

    OP_6D(-2800, 0, 22400, 8000)
    Return()

    # Function_12_16FA end

    def Function_13_170C(): pass

    label("Function_13_170C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1750")
    SetChrPos(0x101, 42290, 0, 5450, 270)
    SetChrPos(0x102, 43520, 0, 4400, 270)
    OP_6D(38110, 0, 5520, 2000)
    Jump("loc_1783")

    label("loc_1750")

    SetChrPos(0x101, 42150, 0, 35430, 270)
    SetChrPos(0x102, 43340, 0, 34350, 270)
    OP_6D(37700, 0, 35640, 2000)

    label("loc_1783")


    ChrTalk(    #51
        0x102,
        (
            "#012F#1P...\x02\x03",

            "#012FI should have figured monsters\x01",
            "wouldn't bother coming in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#501F#1PThe glow of the orbments sure give\x01",
            "this place a romantic ambiance.\x02\x03",

            "#001FIt makes me feel like it was all\x01",
            "worthwhile just setting foot in\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#017F#1PYou are definitely a ditz,\x01",
            "Estelle...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #54
        0x101,
        (
            "#509F#1PAt least it's better than being\x01",
            "dense like someone I know!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_13_170C end

    def Function_14_191C(): pass

    label("Function_14_191C")

    EventBegin(0x0)
    OP_6D(-76360, 0, -31950, 0)
    OP_6B(2600, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x102, 0x80)

    def lambda_1971():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1971)

    def lambda_1983():
        OP_8E(0xFE, 0xFFFED630, 0x0, 0xFFFF8364, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1983)
    Sleep(1600)
    ClearChrFlags(0x101, 0x80)

    def lambda_19A8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19A8)
    OP_8E(0x101, 0xFFFEDDD8, 0x0, 0xFFFF8364, 0x7D0, 0x0)

    ChrTalk(    #55
        0x101,
        (
            "#007FMan, I'm beat.\x02\x03",

            "#007FIt's really late, so how about\x01",
            "we hit the sack?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        "#015F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#000FJoshua?\x02\x03",

            "#000FWhat's wrong...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#013FI'm sorry...\x02\x03",

            "#013FI made the situation really\x01",
            "awkward for everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#004FHuh? Are you talking about what\x01",
            "happened back outside?\x02\x03",

            "#001FDon't sweat it. I guarantee you\x01",
            "nobody thought anything of it.\x02\x03",

            "#001FReally, your judgment was the\x01",
            "most sound of anyone's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#013FNo, it wasn't...\x01",
            "I'm just cold-hearted and\x01",
            "indifferent is all.\x02\x03",

            "#013FEven now, I still think we shouldn't\x01",
            "have shown any mercy and simply put\x01",
            "those creatures out of their misery.\x02\x03",

            "#013FUnlike you and Tio, I don't feel\x01",
            "any compassion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#002F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x102,
        (
            "#013FIt's at times like this that...\x01",
            "I really begin to loathe myself...\x02\x03",

            "#013FIt's almost as if there's something\x01",
            "wrong with me as a person.\x02\x03",

            "#019FHa ha... Maybe some part of my\x01",
            "heart is broken or something...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_1D5A():
        OP_8E(0xFE, 0xFFFED9DC, 0x0, 0xFFFF8364, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D5A)
    OP_6D(-77400, 0, -31900, 1000)

    ChrTalk(    #63
        0x101,
        "#005F#4SJoshua!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#005FDon't you dare say things like\x01",
            "that about yourself!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x102, 0x101, 400)
    OP_8F(0x102, 0xFFFED52C, 0x0, 0xFFFF8364, 0xBB8, 0x0)

    ChrTalk(    #65
        0x102,
        "#014F#3PE-Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#009FI've watched almost everything you've\x01",
            "done for the past five years!\x02\x03",

            "#009FAnd I'm confident in saying that\x01",
            "I know your strengths and weak-\x01",
            "nesses better than anyone else.\x02\x03",

            "#009FProbably even more than you,\x01",
            "yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        "#014F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#005FI won't allow you to just disregard\x01",
            "everything with a bunch of nonsense!\x02\x03",

            "#005FI don't ever want to hear you\x01",
            "say you're 'broken' again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#013F#3P...\x02\x03",

            "#013FI'm sorry. It was foolish of me\x01",
            "to say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#002FAs long as you understand what\x01",
            "I said, that's what really matters.\x02\x03",

            "#002F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        "#013F#3P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#501FBut you know what?\x01",
            "Believe it or not...\x02\x03",

            "...I was happy to hear you admit\x01",
            "how you felt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x102,
        "#014F#3PWhy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#003FYour real problem, Joshua, is\x01",
            "that you always try to keep your\x01",
            "feelings locked up inside.\x02\x03",

            "#003FWhenever you're troubled\x01",
            "or worried...\x02\x03",

            "#003FYou just go around with this\x01",
            "nonchalant look and try to fix\x01",
            "everything by yourself.\x02\x03",

            "#500FThat's a little upsetting for\x01",
            "someone who's supposed to be\x01",
            "your family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#013F#3P...\x02\x03",

            "#013FEstelle, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#006FJoshua, you were able to lay\x01",
            "bare your own weakness today.\x02\x03",

            "#006FYou learned to trust in someone\x01",
            "other than yourself.\x02\x03",

            "#001FAnd for that, I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#018F#3PI-I don't know what your point\x01",
            "is, but...\x02\x03",

            "#018FI'm amazed that you can just\x01",
            "stand there and say something\x01",
            "as embarrassing as that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#502FHa! I've got a whole lot more\x01",
            "where that came from! ♪\x02\x03",

            "#006FBut how about we call it a night?\x01",
            "After all this endless running\x01",
            "around, I'm ready to drop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#015F#3PAll right then.\x01",
            "Have a good night, Estelle.\x02\x03",

            "#010FAnd thanks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#506FYou're welcome, Joshua.\x02\x03",

            "#000FSleep tight.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    NewScene("ED6_DT01/T0400   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_14_191C end

    SaveToFile()

Try(main)
