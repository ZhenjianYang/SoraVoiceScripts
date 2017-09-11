from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2410   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2410.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Matron Theresa',                       # 9
        'Daniel',                               # 10
        'Mary',                                 # 11
        'Clem',                                 # 12
        'Polly',                                # 13
        'Pot',                                  # 14
        'Black tea',                            # 15
        'Black tea',                            # 16
        'Black tea',                            # 17
        'Black tea',                            # 18
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
        'ED6_DT07/CH02570 ._CH',             # 00
        'ED6_DT07/CH02640 ._CH',             # 01
        'ED6_DT07/CH02630 ._CH',             # 02
        'ED6_DT07/CH02590 ._CH',             # 03
        'ED6_DT07/CH02500 ._CH',             # 04
        'ED6_DT07/CH00003 ._CH',             # 05
        'ED6_DT07/CH00013 ._CH',             # 06
        'ED6_DT07/CH00043 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT06/CH20021 ._CH',             # 09
        'ED6_DT07/CH02573 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02570P._CP',             # 00
        'ED6_DT07/CH02640P._CP',             # 01
        'ED6_DT07/CH02630P._CP',             # 02
        'ED6_DT07/CH02590P._CP',             # 03
        'ED6_DT07/CH02500P._CP',             # 04
        'ED6_DT07/CH00003P._CP',             # 05
        'ED6_DT07/CH00013P._CP',             # 06
        'ED6_DT07/CH00043P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT06/CH20021P._CP',             # 09
        'ED6_DT07/CH02573P._CP',             # 0A
    )

    DeclNpc(
        X                   = -3700,
        Z                   = 0,
        Y                   = 14600,
        Direction           = 0,
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
        X                   = 35100,
        Z                   = 0,
        Y                   = 2300,
        Direction           = 180,
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
        X                   = 35300,
        Z                   = 0,
        Y                   = -35300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 32500,
        Z                   = 0,
        Y                   = -34400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 1703944,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638408,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_2B0",          # 01, 1
        "Function_2_2B1",          # 02, 2
        "Function_3_2C7",          # 03, 3
        "Function_4_372",          # 04, 4
        "Function_5_3CC",          # 05, 5
        "Function_6_434",          # 06, 6
        "Function_7_48D",          # 07, 7
        "Function_8_505",          # 08, 8
        "Function_9_1246",         # 09, 9
    )


    def Function_0_242(): pass

    label("Function_0_242")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_24C")
    Jump("loc_28A")

    label("loc_24C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_256")
    Jump("loc_28A")

    label("loc_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_END)), "loc_260")
    Jump("loc_28A")

    label("loc_260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_26A")
    Jump("loc_28A")

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_279")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_28A")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_283")
    Jump("loc_28A")

    label("loc_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_28A")

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_298")
    OP_A3(0x3FA)
    Event(0, 8)

    label("loc_298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_2AF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FB)
    Event(0, 9)

    label("loc_2AF")

    Return()

    # Function_0_242 end

    def Function_1_2B0(): pass

    label("Function_1_2B0")

    Return()

    # Function_1_2B0 end

    def Function_2_2B1(): pass

    label("Function_2_2B1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B1")

    label("loc_2C6")

    Return()

    # Function_2_2B1 end

    def Function_3_2C7(): pass

    label("Function_3_2C7")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_36E")

    ChrTalk(    #0
        0x8,
        (
            "#750FDo come back soon. The\x01",
            "children would be delighted\x01",
            "to see you again.\x02\x03",

            "There isn't much here for them\x01",
            "to do, you see. All we have is\x01",
            "tea and candy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E")

    TalkEnd(0x8)
    Return()

    # Function_3_2C7 end

    def Function_4_372(): pass

    label("Function_4_372")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_3C8")

    ChrTalk(    #1
        0xFE,
        (
            "#770FCome back to see us sometime,\x01",
            "okay, Miss Kloe?\x02\x03",

            "We'll be waiting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C8")

    TalkEnd(0xB)
    Return()

    # Function_4_372 end

    def Function_5_3CC(): pass

    label("Function_5_3CC")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_430")

    ChrTalk(    #2
        0xFE,
        (
            "Miss Kloe makes the best\x01",
            "apple pie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I could eat it three times a\x01",
            "day forever!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_430")

    TalkEnd(0x9)
    Return()

    # Function_5_3CC end

    def Function_6_434(): pass

    label("Function_6_434")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_489")

    ChrTalk(    #4
        0xFE,
        (
            "'Stelle and Joshy, you gotta\x01",
            "come an' play some more\x01",
            "again, okaaaaay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_489")

    TalkEnd(0xC)
    Return()

    # Function_6_434 end

    def Function_7_48D(): pass

    label("Function_7_48D")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_501")

    ChrTalk(    #5
        0xFE,
        (
            "I'm sorry for all the trouble that\x01",
            "Clem caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "He's just always like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "What a pain...\x02",
    )

    CloseMessageWindow()

    label("loc_501")

    TalkEnd(0xA)
    Return()

    # Function_7_48D end

    def Function_8_505(): pass

    label("Function_8_505")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x136, 0x4)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x136, 7)
    SetChrPos(0x101, -5240, 200, 7350, 90)
    SetChrPos(0x102, -5240, 200, 6050, 90)
    SetChrPos(0x136, -2550, 200, 6100, 270)
    SetChrPos(0x8, -2550, 200, 7350, 270)
    SetChrChipByIndex(0x8, 10)
    OP_4A(0x8, 255)
    SetChrPos(0xD, -4100, 750, 5310, 0)
    SetChrPos(0xE, -4550, 700, 6860, 0)
    SetChrPos(0xF, -4530, 700, 6060, 0)
    SetChrPos(0x10, -3810, 700, 6860, 0)
    SetChrPos(0x11, -3710, 700, 6060, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_6D(-2580, 0, 14700, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05Estelle introduced herself and explained about the recent events over a\x01",
            "veritable feast of tea and pie.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1500, 0)
    OP_6D(-3770, 100, 7530, 3000)

    ChrTalk(    #9
        0x8,
        (
            "#756FI see...\x02\x03",

            "He really isn't a mean-spirited\x01",
            "child, but he can be quite the\x01",
            "little trickster.\x02\x03",

            "#754FAs his guardian, I must apologize.\x01",
            "I am truly sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#000FOh, it's okay.\x01",
            "I got my emblem back.\x02\x03",

            "#001FPlus I got some tasty herbal\x01",
            "tea and apple pie out of it, \x01",
            "so we're square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "#750FHa ha... Thank you both.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FThe tea was really the best part,\x01",
            "though.\x02\x03",

            "It's just like the kind they brew\x01",
            "in the tavern.\x02\x03",

            "Is it grown locally?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#750FYes... Gardening is one of my\x01",
            "hobbies, actually.\x02\x03",

            "I give some to the barkeep at the\x01",
            "tavern whenever I have extra.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#501FNeat.\x02\x03",

            "I'm gonna have to give my vote\x01",
            "to the apple pie though. It was\x01",
            "just plain amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#751FHa ha... Well, I can't take\x01",
            "credit for that. She made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#004FShe? Who? You, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x136,
        (
            "#045FThis is still so embarrassing...\x02\x03",

            "#043FI was really rude earlier.\x02\x03",

            "To think, I could be so mistaken...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#006FOh, don't worry about it.\x01",
            "Apple pie heals all wounds,\x01",
            "or something like that.\x02\x03",

            "Besides, I wasn't acting like any\x01",
            "kind of saint myself!\x02\x03",

            "That white hawk sure surprised\x01",
            "the hell out of me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x136,
        (
            "#040FOh, that was Sieg.\x02\x03",

            "He's a gyrfalcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#010FA gyrfalcon... That's Liberl's\x01",
            "national bird, isn't it?\x02\x03",

            "You seemed really comfortable\x01",
            "with him. Is he your pet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x136,
        (
            "#041FNo, I don't keep him.\x02\x03",

            "He's a close friend, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#004FWow! As friends go, he's pretty\x01",
            "awesome! \x02\x03",

            "#000FThat reminds me. Aren't you a\x01",
            "student at the royal academy?\x02\x03",

            "But you live here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x136,
        (
            "#040FNo... I stay in the girls' dorm on\x01",
            "campus.\x02\x03",

            "It's not that far away, so I like\x01",
            "to come and visit when I can.\x02\x03",

            "#045FI sometimes worry I might be\x01",
            "kind of a bother, though...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)

    ChrTalk(    #24
        0x8,
        (
            "#751FOh, dear. Please don't think that.\x02\x03",

            "You're always so helpful when\x01",
            "you come by.\x02\x03",

            "And the children are always\x01",
            "happy to see you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x136, 2)

    ChrTalk(    #25
        0x136,
        "#040FMatron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#750FI personally worry that you might be\x01",
            "neglecting your duties at school\x01",
            "in favor of us.\x02\x03",

            "I know that's a silly concern to\x01",
            "have about you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x136,
        "#045FI won't let you down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#501FHmm... You live on campus, huh?\x02\x03",

            "I've always kind of wanted to\x01",
            "know what that was like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010FI imagine that we got a weekly taste\x01",
            "of it at the church lessons.\x02\x03",

            "But isn't the entrance exam for\x01",
            "the academy pretty hard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#007FI think my head would explode if\x01",
            "I had to take an exam like that...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)
    SetChrSubChip(0x136, 0)

    ChrTalk(    #31
        0x136,
        (
            "#040FHa ha... It's not so hard.\x02\x03",

            "I think it must be far more\x01",
            "difficult to become a bracer.\x02\x03",

            "#041FYou know... I've always kind of\x01",
            "wanted to be one, ever since\x01",
            "I was a little girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#008FHa ha ha... I don't even know what to\x01",
            "say to that.\x02\x03",

            "You call me a bracer, but I'm\x01",
            "still just an apprentice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#010FWe have to travel all over the\x01",
            "kingdom before we can advance.\x02\x03",

            "I think we'll be in Ruan for a\x01",
            "little while, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#750FIn that case, perhaps I'll have\x01",
            "a chance to repay you.\x02\x03",

            "#751FPlus, the children would love for\x01",
            "you to come back and play again.\x02\x03",

            "I'll prepare a whole mountain of\x01",
            "tea and baked goods.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_505 end

    def Function_9_1246(): pass

    label("Function_9_1246")

    EventBegin(0x0)
    OP_A2(0x41C)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x9, 37220, 0, -33090, 180)
    SetChrPos(0xA, 37310, 1700, -33090, 180)
    SetChrPos(0xC, 37220, 0, -36830, 180)
    SetChrPos(0xB, 37220, 1700, -36830, 180)
    SetChrPos(0x8, 36300, 0, 42360, 270)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    OP_4A(0xC, 255)
    OP_4A(0xB, 255)
    OP_4A(0x8, 255)
    OP_6D(38522, 0, -31220, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    FadeToBright(500, 0)
    OP_6D(35522, 0, -34220, 3000)
    Sleep(2000)
    Fade(1000)
    OP_6D(36570, 0, 42820, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #35
        0x8,
        (
            "#750FHa ha... I suppose having this much sewing to do\x01",
            "is proof that the children are full of energy.\x02\x03",

            "Well, it'll all wait till morning.\x01",
            "For now, I'd best get some sleep,\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrPos(0x8, 35780, 0, 42330, 270)
    OP_0D()
    Sleep(500)

    def lambda_1424():
        OP_6D(35930, 0, 43280, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1424)
    OP_8E(0x8, 0x87DC, 0x0, 0xA546, 0x3E8, 0x0)
    OP_8E(0x8, 0x864C, 0x0, 0xAA50, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #36
        0x8,
        (
            "#754FPlease watch over them tomorrow,\x01",
            "Aidios, and keep them safe...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x07\x05The crackling and popping sound\x01",
            "of a fire can be heard. #\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x8,
        (
            "#753FWhat's that noise? Sounds like\x01",
            "someone put wood on the fire...\x02\x03",

            "#753FThat smell...\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 180, 500)

    ChrTalk(    #39
        0x8,
        "#755F...It can't be!!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T2400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1246 end

    SaveToFile()

Try(main)
