from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0121_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_161",          # 01, 1
        "Function_2_1A5B",         # 02, 2
        "Function_3_1AA8",         # 03, 3
        "Function_4_1EC0",         # 04, 4
        "Function_5_3B06",         # 05, 5
        "Function_6_4F52",         # 06, 6
        "Function_7_4FBD",         # 07, 7
        "Function_8_6F78",         # 08, 8
        "Function_9_6FA8",         # 09, 9
        "Function_10_6FD8",        # 0A, 10
        "Function_11_7008",        # 0B, 11
        "Function_12_7038",        # 0C, 12
        "Function_13_7A83",        # 0D, 13
        "Function_14_7AB4",        # 0E, 14
        "Function_15_7AEE",        # 0F, 15
        "Function_16_7B28",        # 10, 16
        "Function_17_7B62",        # 11, 17
        "Function_18_7B9C",        # 12, 18
        "Function_19_8EDF",        # 13, 19
        "Function_20_8F38",        # 14, 20
        "Function_21_9531",        # 15, 21
        "Function_22_9646",        # 16, 22
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_BB")
    OP_2A(0xB7, 0xB8, 0xFFFF)
    Jump("loc_15D")

    label("loc_BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_DC")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0x74, 0x75, 0x76, 0x77, 0xAF, 0xB0, 0xFFFF)
    Jump("loc_15D")

    label("loc_DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_F7")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0x74, 0xAF, 0xB0, 0xFFFF)
    Jump("loc_15D")

    label("loc_F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_10E")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0x74, 0xFFFF)
    Jump("loc_15D")

    label("loc_10E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_123")
    OP_2A(0x72, 0x73, 0xAD, 0xAE, 0xFFFF)
    Jump("loc_15D")

    label("loc_123")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05No jobs are available.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_15D")

    TalkEnd(0xFF)
    Return()

    # Function_0_AA end

    def Function_1_161(): pass

    label("Function_1_161")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 46210, 0, -1330, 90)
    SetChrPos(0x103, 45510, 0, -550, 90)
    SetChrPos(0xF8, 45070, 0, -1770, 90)
    SetChrPos(0xF9, 44550, 0, -830, 90)
    OP_8C(0xFE, 270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2")
    SetChrPos(0xF9, 45070, 0, -1770, 90)
    SetChrPos(0xF8, 44550, 0, -830, 90)

    label("loc_1E2")

    OP_6D(47260, 0, -210, 0)
    OP_67(0, 5030, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #1
        0x101,
        (
            "#1011F#6PUmm, hello there. Could we have\x01",
            "a moment of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "#2PWhat is it? Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1015F#6PNo, nothing like that. I just have\x01",
            "a quick question.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Estelle told Bloom that she was looking for a certain stew\x01",
            "recipe on Radford's behalf.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #5
        0xFE,
        "#2PYes, I know the one. \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#2PIt used to be very popular around here.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_410")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_44E")

    label("loc_410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_44E")

    label("loc_437")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_44E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4B3")

    label("loc_475")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4B3")

    label("loc_49C")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4B3")

    Sleep(1000)

    ChrTalk(    #7
        0x101,
        "#1004F#6PReally?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50F")

    ChrTalk(    #8
        0x107,
        "#064FCould you tell us anything about it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E4")

    label("loc_50F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_560")

    ChrTalk(    #9
        0x105,
        (
            "#044FThat's a relief. Could you tell us\x01",
            "anything about it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4")

    label("loc_560")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A4")

    ChrTalk(    #10
        0x104,
        (
            "#033FWould you mind telling us more\x01",
            "about it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E4")

    label("loc_5A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E4")

    ChrTalk(    #11
        0x108,
        "#3P#073FCould you tell us anything about it?\x02",
    )

    CloseMessageWindow()

    label("loc_5E4")


    ChrTalk(    #12
        0xFE,
        "#2POh, I could tell you plenty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "#2PIt was your standard dish in every\x01",
            "household back in my day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1011F#6PYeah, Densel said something like that,\x01",
            "too.\x02\x03",

            "#1001FThis HAS to be the one!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        (
            "#020F#3PWe've been looking for the recipe\x01",
            "to that particular dish, ma'am.\x02\x03",

            "Would you happen to know the\x01",
            "ingredients?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "#2PWell, yes and no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "#2PThe recipe I know is probably a little\x01",
            "different than what you're looking for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "#2PI don't mind telling you my version.\x01",
            "I just want to make sure you're\x01",
            "aware of that before you pass it on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1011F#6PDifferent? Different how?\x02\x03",

            "I thought it'd be the same recipe.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_87A")

    ChrTalk(    #20
        0x106,
        "#555FWhaddaya mean?\x02",
    )

    CloseMessageWindow()
    Jump("loc_915")

    label("loc_87A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AA")

    ChrTalk(    #21
        0x108,
        "#3P#070FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    Jump("loc_915")

    label("loc_8AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DB")

    ChrTalk(    #22
        0x104,
        "#033FWhatever do you mean?\x02",
    )

    CloseMessageWindow()
    Jump("loc_915")

    label("loc_8DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_915")

    ChrTalk(    #23
        0x105,
        "#044FSorry, I'm not sure I understand.\x02",
    )

    CloseMessageWindow()

    label("loc_915")


    ChrTalk(    #24
        0xFE,
        (
            "#2PMy recipe's one that's been passed\x01",
            "down in my family for generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "#2PAs with any family recipe, it's been\x01",
            "tweaked here and there over the years.\x01",
            "The flavor's likely not what it used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "#2PThough as I said before, I'd be happy to\x01",
            "give you my version of the recipe if that's\x01",
            "fine by you. What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1002F#6PHmm... It's been updated a bit, but\x01",
            "maybe that's okay?\x02\x03",

            "#1003FI'd like to find the original if we can...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#027F#3PThe original version would be ideal,\x01",
            "yes, but we can't afford to be picky.\x02\x03",

            "A slightly different version beats\x01",
            "handing the client nothing at all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BE0")

    ChrTalk(    #29
        0x104,
        (
            "#030FI agree.\x02\x03",

            "And it would hardly do to turn her\x01",
            "down after she so kindly offered.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_BE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C58")

    ChrTalk(    #30
        0x108,
        (
            "#3P#070FYou've got a point.\x02\x03",

            "Besides, she was kind enough to\x01",
            "offer, so why not take her up on it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_C58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #31
        0x105,
        (
            "#040FYes, I agree.\x02\x03",

            "Besides, it's only right that we take\x01",
            "her up on her kind offer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D35")

    label("loc_CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D35")

    ChrTalk(    #32
        0x106,
        (
            "#051FSchera's right.\x02\x03",

            "Besides, she's saying she'll tell us,\x01",
            "so let's shut up and listen to her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D35")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #33
        0x101,
        "#1006F#4PYeah, I see what you guys mean.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "#2PYou'd like it, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "#2PWonderful! Wait right here;\x01",
            "I'll go grab my recipe book.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        "#020F#3PThank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0xFE, 44800, 0, 2410, 0)
    OP_43(0xFE, 0x0, 0x1, 0x2)
    SetChrPos(0x101, 44360, 0, -280, 0)
    SetChrPos(0x103, 43020, 0, 160, 45)
    SetChrPos(0xF8, 45040, 0, -1020, 0)
    SetChrPos(0xF9, 46250, 0, -820, 315)
    OP_6D(45660, 0, 1500, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(3000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #37
        0x101,
        (
            "#2P#1015F...\x02\x03",

            "(She sure is taking her sweet time...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        "#026F(Now, now. Don't be so impatient.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F62")

    ChrTalk(    #39
        0x106,
        (
            "#051F(Give her a damn minute, would you?)\x02\x03",

            "(In case you forgot, she's kinda old.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F2")

    label("loc_F62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FED")

    ChrTalk(    #40
        0x108,
        (
            "#070F(Give her a little more time, Estelle.)\x02\x03",

            "(She looks plenty spry for her age,\x01",
            "but she's still an elderly woman.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F2")

    label("loc_FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107E")

    ChrTalk(    #41
        0x104,
        (
            "#031F(She may be quite spry for her age, but\x01",
            "she is many, MANY years our elder.)\x02\x03",

            "(We should practice tolerance and wait.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F2")

    label("loc_107E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10F2")

    ChrTalk(    #42
        0x105,
        (
            "#040F(She may be in good health, but she\x01",
            "is quite elderly.)\x02\x03",

            "(I'm sure it won't be much longer.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F2")

    OP_4A(0xFE, 255)
    OP_8C(0xFE, 0, 400)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)

    ChrTalk(    #43
        0xFE,
        "#4POoh, goodness. That's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "#4PWell, no wonder I can't find it!\x02",
    )

    CloseMessageWindow()
    OP_8E(0xFE, 0xAF00, 0x0, 0x96A, 0x3E8, 0x0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #45
        0xFE,
        (
            "I'm sorry, children. I kept you waiting\x01",
            "much longer than I'd meant to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "I'd simply be fuming were I in your shoes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#2P#1016FN-No way, you didn't take THAT long.\x02\x03",

            "#1011FSo, um, did you find your recipe book?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "About that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "I hadn't thought about it until\x01",
            "I'd started looking, but I actually\x01",
            "gave it away a while back.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x101,
        "#2P#1020FWhaaat?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1331")

    ChrTalk(    #51
        0x107,
        "#561FAwww...\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_1331")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1354")

    ChrTalk(    #52
        0x105,
        "#043FOh, my.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_1354")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_138A")

    ChrTalk(    #53
        0x106,
        "#055FYou've gotta be kidding...\x02",
    )

    CloseMessageWindow()
    Jump("loc_13B6")

    label("loc_138A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6")

    ChrTalk(    #54
        0x108,
        "#074FThat's unfortunate.\x02",
    )

    CloseMessageWindow()

    label("loc_13B6")


    ChrTalk(    #55
        0xFE,
        (
            "It completely slipped my mind.\x01",
            "I'm so sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "He'd said he made a hobby of\x01",
            "keeping older books and asked\x01",
            "if he could add it to his collection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "I hadn't cracked it open in years,\x01",
            "so I thought nothing of handing it\x01",
            "over to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "*siiigh* If only I weren't always so\x01",
            "generous...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#2P#1007FTrust me, I feel like sighing, too.\x02\x03",

            "We'll never be able to find out who\x01",
            "got it, either. Man, what a pain...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #60
        0x103,
        (
            "#027FNo point in cursing our luck.\x01",
            "What's done is done.\x02\x03",

            "Our time would be better spent\x01",
            "figuring out what else we can do.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15E3():
        TurnDirection(0xF8, 0x103, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_15E3)
    Sleep(150)
    TurnDirection(0xF9, 0x103, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1670")

    ChrTalk(    #61
        0x105,
        (
            "#042FExactly.\x02\x03",

            "Maybe we really could ask around\x01",
            "and see if anyone knows the man\x01",
            "who took the book?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E6")

    label("loc_1670")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16EE")

    ChrTalk(    #62
        0x104,
        (
            "#035FExactly.\x02\x03",

            "Perhaps we really could ask around\x01",
            "and see if anyone knows the man\x01",
            "with the recipe book?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E6")

    label("loc_16EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1757")

    ChrTalk(    #63
        0x108,
        (
            "#070FExactly.\x02\x03",

            "Pain or not, we could always try\x01",
            "finding the guy who took the book.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17E6")

    label("loc_1757")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17E6")

    ChrTalk(    #64
        0x106,
        (
            "#050FI'm with you there.\x02\x03",

            "We could waste time doin' a whole\x01",
            "lot of nothing or try and find the guy\x01",
            "who got the recipe book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17E6")


    ChrTalk(    #65
        0x101,
        (
            "#2P#1015FYeah. Only one thing to do,\x01",
            "so might as well suck it up\x01",
            "and get to it.\x02\x03",

            "You said he liked collecting old books,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#020FIf you have any idea who that might be,\x01",
            "we should try them first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I'm afraid that's about all I can remember.\x01",
            "I wish I could help more, really.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1910():
        TurnDirection(0xF8, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1910)
    Sleep(150)

    def lambda_1923():
        TurnDirection(0xF9, 0x12, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1923)
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #68
        0x101,
        (
            "#2P#1006FHey, no worries!\x02\x03",

            "You gave us a pretty big clue.\x01",
            "Can't be too many guys out there\x01",
            "who collect old books for fun.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #69
        0x103,
        (
            "#020FYes, thank you for your help.\x02\x03",

            "We'll come to you again if we need to,\x01",
            "but in case we don't, you have yourself\x01",
            "a wonderful day, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_28(0x75, 0x1, 0x200)
    EventEnd(0x0)
    OP_43(0x12, 0x0, 0x0, 0x2)
    Return()

    # Function_1_161 end

    def Function_2_1A5B(): pass

    label("Function_2_1A5B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1AA7")
    OP_8E(0xFE, 0xAF00, 0x0, 0x96A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xB306, 0x0, 0x96A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_2_1A5B")

    label("loc_1AA7")

    Return()

    # Function_2_1A5B end

    def Function_3_1AA8(): pass

    label("Function_3_1AA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C6C")
    EventBegin(0x1)
    OP_6D(13410, 0, 139810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToDark(300, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #70
        "\x07\x05You may now reconfigure your party.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #71
        (
            "\x07\x05Please select two members in addition to your mandatory\x01",
            "members.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BF4")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_1BF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C17")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_1C17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C3A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_1C3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C67")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_1C67")

    Sleep(300)

    label("loc_1C6C")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, 1200, 0, 116170, 0)
    SetChrPos(0xF7, 370, 0, 115520, 0)
    SetChrPos(0xF8, 1850, 0, 114800, 0)
    SetChrPos(0xF9, 910, 0, 114140, 0)
    OP_6D(750, 0, 117600, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #72
        0x8,
        (
            "#741F#4PAaaaah! I finally got in some\x01",
            "quality drinking time today.\x02\x03",

            "Circumstances aside, I really\x01",
            "have to thank you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1016F#1PUh... You're welcome, I guess?\x02\x03",

            "#1015FBy the way, what happened to\x01",
            "Olivier afterward?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#740F#4PDon't worry. Father Divine gave him a\x01",
            "clean bill of health.\x02\x03",

            "He's a bit slow on the uptake right now,\x01",
            "but I'm sure he'll be able to do his job\x01",
            "just fine. He's upstairs if you need him. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_3_1AA8 end

    def Function_4_1EC0(): pass

    label("Function_4_1EC0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED3")
    Call(0, 39)

    label("loc_1ED3")

    OP_4A(0x8, 255)
    OP_6D(1310, 0, 112280, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x5, 0xF8, 0xFF)
    AddParty(0x6, 0xF9, 0xFF)
    AddParty(0x3, 0xFA, 0xFF)
    AddParty(0x4, 0xFB, 0xFF)
    AddParty(0x7, 0xFC, 0xFF)
    SetChrPos(0x101, 540, 0, 116590, 0)
    SetChrPos(0x103, 1740, 0, 116600, 0)
    SetChrPos(0x108, -60, 0, 114490, 0)
    SetChrPos(0x104, 3390, 0, 114890, 0)
    SetChrPos(0x106, 2040, 0, 115240, 0)
    SetChrPos(0x107, 1100, 0, 115100, 0)
    SetChrPos(0x105, 110, 0, 115560, 0)

    def lambda_1FA9():
        OP_6D(80, -200, 117460, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FA9)

    def lambda_1FC1():
        OP_67(0, 6590, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FC1)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #75
        0x8,
        (
            "#741FHaha. I certainly wasn't expecting you\x01",
            "all to show up now, of all times!\x02\x03",

            "#740FYou were heading to Bose, last I heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#025F#6PWe WERE, yes.\x02\x03",

            "#524FThe paranoid little part of me can't help\x01",
            "but wonder if this is intentional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        (
            "#741FWell, I'm not going to complain about\x01",
            "having you around.\x02\x03",

            "#740FAnyway. I do believe this is the first\x01",
            "time we've seen each other since you\x01",
            "went off to train, Estelle.\x02\x03",

            "You look right at home in that new outfit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1025F#6PAww, Aina, you'll make me blush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#740FMr. Vathek, Milady Klaudia, Miss Russell,\x01",
            "I believe this is the first we've met.\x02\x03",

            "I'm Aina, the receptionist for the Rolent\x01",
            "branch.\x02\x03",

            "A pleasure to meet you all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x105,
        "#048F#6PThe pleasure is mine, Miss Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x107,
        "#560F#5PUm, um, nice to meet you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x108,
        (
            "#3P#071FHaha! Good to meet you at last, Aina.\x01",
            "I've heard a lot about you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        "#743FReally? I wonder.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)
    Sleep(500)

    ChrTalk(    #84
        0x8,
        (
            "#740FOh, and Olivier's here, too.\x01",
            "What ARE you doing over there, Olivier?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_91(0x104, 0xFFFFFED4, 0x0, 0x0, 0x3E8, 0x0)

    ChrTalk(    #85
        0x104,
        (
            "#031F#5PHa-ha-ha! Don't, ah, mind me!\x02\x03",

            "I was certainly not flashing back to\x01",
            "memories of the destruction of my liver.\x01",
            "Just...for the record.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        "#743FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#021F#6PHeehee... Just let him be, Aina.\x02\x03",

            "#020FOh, and I'm guessing you know\x01",
            "Agate, Aina.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #88
        0x106,
        (
            "#051FWe've met, yeah.\x02\x03",

            "I don't come up by Rolent much, so\x01",
            "we've only met, like, once or twice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#741FIt's still good to see you again,\x01",
            "though, Agate.\x02\x03",

            "#742FSo with the pleasantries out of the way...\x01",
            "I'm sorry, but do you mind if we get\x01",
            "straight to business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        "#022F#6POf course, Aina. Go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#742FThis...'fog' appeared suddenly today\x01",
            "around dawn.\x02\x03",

            "At first it seemed to be little more than\x01",
            "the usual light mist we get here at times.\x02\x03",

            "But...you could literally stand outside\x01",
            "and watch it grow thicker. It was eerie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x105,
        "#043F#6PDo we have any idea what's causing it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#742FNone, I'm afraid.\x02\x03",

            "It's definitely covering all of the city,\x01",
            "but we're not sure of its full extent or\x01",
            "source yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x108,
        (
            "#3P#074FFog and mist have several common\x01",
            "sources.\x02\x03",

            "You can get the sort that springs up\x01",
            "off-coast and flows inland, or the kind\x01",
            "that forms in mountain basins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x104,
        (
            "#030F#5PHmm. There are several basins in the\x01",
            "Krone mountains near Rolent, are there not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#740FThere are, yes.\x02\x03",

            "It IS possible this is simply a\x01",
            "freak act of nature...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#026F#6P...But with everything that's been happening\x01",
            "recently, we should be on our guard.\x02\x03",

            "#020FShould we put off heading for Bose and\x01",
            "remain in Rolent for now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x106,
        (
            "#051FThat's the best idea, I think.\x02\x03",

            "Passenger ships sure ain't movin'\x01",
            "till this soup clears, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1003F#6PUm, but...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #100
        0x106,
        "#052FWhat's up, Estelle?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #101
        0x101,
        (
            "#1025F#6PWell, I was just thinking about\x01",
            "the bandits and stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x106,
        (
            "#050FWe were checkin' that out 'cause we had\x01",
            "no other leads, remember?\x02\x03",

            "The Royal Army's on top of that anyway,\x01",
            "so we don't really HAVE to go, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#1026F#6PBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x106,
        (
            "#555FLook, what is it?\x01",
            "Somethin' eating at you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1003F#6PUm, no, but!\x02\x03",

            "It's just, I...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(50)
    TurnDirection(0x105, 0x101, 400)
    Sleep(50)
    TurnDirection(0x104, 0x101, 400)
    Sleep(500)

    ChrTalk(    #106
        0x103,
        (
            "#026F#4PEstelle.\x02\x03",

            "#020FI'm not exactly sure what you're thinking,\x01",
            "but calm down and consider for a moment.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #107
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x103,
        (
            "#020F#4PThe bandit ship theft case is already over,\x01",
            "in a way.\x02\x03",

            "If they'd taken hostages, it'd be different,\x01",
            "but as it is there's no emergency demanding\x01",
            "we take action.\x02\x03",

            "And I can't imagine they'll stay in Bose,\x01",
            "in any event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1026F#6PThat's true, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x103,
        (
            "#026F#4POn the other hand, something bizarre is\x01",
            "happening before our eyes at this very\x01",
            "moment.\x02\x03",

            "If the society is somehow behind this,\x01",
            "there's a good chance Rolent is in danger.\x02\x03",

            "#022FSo...which is the correct choice, here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1003F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x105,
        "#043F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #113
        0x107,
        (
            "#065F#5PUm, Miss Schera!\x02\x03",

            "I think Estelle has a reason she\x01",
            "wants to go! So, um...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(500)

    ChrTalk(    #114
        0x101,
        (
            "#1003F#6P...No, Tita.\x02\x03",

            "#1007FSchera's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x107,
        "#063F#5PEstelle...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #116
        0x101,
        (
            "#1025F#6PSorry, Schera.\x02\x03",

            "I guess I wasn't really paying attention\x01",
            "to what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#524F#4PYou don't need to apologize.\x02\x03",

            "Everyone has times they have\x01",
            "trouble focusing.\x02\x03",

            "#021FEven I do, and I know Agate sure does.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x103, 400)

    ChrTalk(    #118
        0x106,
        "#055FNow hang on a--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#026F#4PBeing able to determine the best path,\x01",
            "without losing sight of yourself,\x01",
            "is a crucial skill for a bracer.\x02\x03",

            "#525FEven if it IS a bit easier to just say\x01",
            "it's important than it is to actually\x01",
            "do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x108,
        (
            "#3P#070FI'm still a student on that front, too,\x01",
            "really.\x02\x03",

            "I can hardly compare to Master Cassius\x01",
            "in that regard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #121
        0x101,
        "#1004F#4PReally, Zin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x108,
        (
            "#3P#074FTo possess perfect clarity and retain one's\x01",
            "good cheer in the face of adversity...\x01",
            "It requires experience.\x02\x03",

            "#070FAnd Master Cassius' ability to do just\x01",
            "that saved us many times when he traveled\x01",
            "to Calvard once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1025F#4PHuh. I didn't know that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #124
        0x106,
        (
            "#051FHey, don't sweat it, all right?\x01",
            "Not as if you can just snap your fingers\x01",
            "and be at the old man's level.\x02\x03",

            "You just gotta put one foot in front of\x01",
            "the other and get better, bit by bit.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #125
        0x101,
        "#1006F#6PYeah... Thanks, guys.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(500)

    ChrTalk(    #126
        0x101,
        "#1007F#6PUm, sorry, Aina. That kinda sidetracked us.\x02",
    )

    CloseMessageWindow()

    def lambda_33F0():
        OP_8C(0x103, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_33F0)
    Sleep(50)

    def lambda_3403():
        OP_8C(0x108, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3403)
    Sleep(50)

    def lambda_3416():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3416)
    Sleep(50)

    def lambda_3429():
        OP_8C(0x106, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3429)
    Sleep(50)

    def lambda_343C():
        OP_8C(0x107, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_343C)
    Sleep(50)

    def lambda_344F():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_344F)
    Sleep(500)

    ChrTalk(    #127
        0x8,
        (
            "#741FHaha. It's fine.\x02\x03",

            "#740FSo getting back to the matter at hand...\x02\x03",

            "At this point, there's nothing really specific\x01",
            "we can ask you to do. You can hardly beat\x01",
            "fog with violence, after all.\x02\x03",

            "I'd simply ask that you be on standby in case\x01",
            "anything does happen.\x02\x03",

            "You can wait at your home, if you'd like,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1011F#6POh, yeah! I was going to head home for\x01",
            "a bit.\x02\x03",

            "Is there anything else we should watch\x01",
            "out for besides that, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#744FHmm. Well.\x02\x03",

            "#742FIf you absolutely want to do SOMETHING...\x01",
            "could I ask you to check the roads for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        "#1004F#6PThe roads? What for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#742FThe fog is covering the entirety of\x01",
            "the city. However...\x02\x03",

            "It also seems to have spread out into the\x01",
            "countryside. The thing is, I don't know\x01",
            "HOW far it's spread yet.\x02\x03",

            "If you could go see how far it's gone,\x01",
            "it would help me consider where we go\x01",
            "from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x104,
        (
            "#030F#5PAh, and we also need to secure land routes\x01",
            "in case the passenger ships continue to\x01",
            "be unusable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "#740FExactly.\x02\x03",

            "There's the Elize Highway to the south,\x01",
            "the Milch Main Road to the west, and the\x01",
            "Malga Trail to the north.\x02\x03",

            "Could you check those three and let me\x01",
            "know the extent of the fog?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1006F#6PSure! That should be pretty easy.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #135
        0x103,
        (
            "#027F#4PWell, then...\x02\x03",

            "For once, this means Estelle and\x01",
            "I will be the guides.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #136
        0x101,
        (
            "#1006F#6PYeah, kind of a change, huh?\x01",
            "We know pretty much everything about\x01",
            "Rolent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x106,
        "#051FWell, who'll be goin' with you, then?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #138
        (
            "\x07\x05Please form your party.\x01",
            "You may choose two other members aside from the\x01",
            "mandatory members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_6D(16980, 0, 120650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    OP_0D()
    OP_A2(0x180C)
    OP_A2(0x10F0)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T0100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1EC0 end

    def Function_5_3B06(): pass

    label("Function_5_3B06")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B26")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_3B26")

    Call(0, 37)
    OP_4A(0x8, 255)
    OP_6D(210, -100, 117420, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(279, 0)
    SetChrPos(0x101, 510, 0, 116600, 0)
    SetChrPos(0x103, 1570, 0, 116600, 0)
    SetChrPos(0x105, -230, 0, 115790, 0)
    SetChrPos(0x106, 2320, 0, 115270, 0)
    SetChrPos(0x108, 250, 0, 114280, 0)
    SetChrPos(0x104, 1850, 0, 114310, 0)
    SetChrPos(0x107, 1070, 0, 115580, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #139
        0x8,
        (
            "#740FGood work, everyone.\x02\x03",

            "Let me pay you for your efforts\x01",
            "before we continue.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x4, 0x10)
    OP_AF(0x3, 0x8F)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #140
        0x8,
        (
            "#744FI have to admit, though, I was expecting\x01",
            "a more...vague report.\x02\x03",

            "If the fog has boundaries THAT clearly\x01",
            "defined... Brrrr.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#022F#6PYes, it's all but impossible to think\x01",
            "of it as natural when you see it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1015F#6PI'm still a little unclear on just how\x01",
            "big the entire, um, 'fog cloud' is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "#742FLet's take a look at it\x01",
            "on a map.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS135._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS220._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetChrName("Aina")
    SetMessageWindowPos(250, 50, -1, -1)

    AnonymousTalk(    #144
        (
            "\x07\x00#744FSo, if it's 60 selge down the Elize Highway,\x01",
            "80 down the Milch Main Road,\x01",
            "and 140 down the Malga Trail...\x02\x03",

            "#740FIt should look something like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_61(0x101)
    SetMessageWindowPos(50, 80, -1, -1)

    AnonymousTalk(    #145
        (
            "#1007FThat's not really as helpful as I thought\x01",
            "it'd be...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 180, -1, -1)
    OP_61(0x105)

    AnonymousTalk(    #146
        (
            "#043FYes, it's strange...\x02\x03",

            "The way fog spreads should change based on its\x01",
            "point of origin and the direction of the wind.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)

    ChrTalk(    #147
        0x106,
        (
            "#555FMeaning we're still completely in the dark\x01",
            "on what's causing this or what it means.\x02\x03",

            "Guess all we can do is stay ready for\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#745FI'm afraid so.\x02\x03",

            "The army's still on the fence about\x01",
            "mobilizing, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1004F#6POh, that reminds me.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Sleep(500)

    ChrTalk(    #150
        0x101,
        (
            "#1018F#7PHey, um, Tita?\x02\x03",

            "I don't suppose your Grandpa has any inventions\x01",
            "that are like, um, a fog remover or something?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41CE():

        label("loc_41CE")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_41CE")

    QueueWorkItem2(0x107, 3, lambda_41CE)

    def lambda_41DF():

        label("loc_41DF")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_41DF")

    QueueWorkItem2(0x103, 3, lambda_41DF)

    def lambda_41F0():

        label("loc_41F0")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_41F0")

    QueueWorkItem2(0x106, 3, lambda_41F0)

    def lambda_4201():

        label("loc_4201")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4201")

    QueueWorkItem2(0x104, 3, lambda_4201)

    def lambda_4212():

        label("loc_4212")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4212")

    QueueWorkItem2(0x105, 3, lambda_4212)

    def lambda_4223():

        label("loc_4223")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_4223")

    QueueWorkItem2(0x108, 3, lambda_4223)
    Sleep(500)

    ChrTalk(    #151
        0x107,
        (
            "#064F#5PA what?\x02\x03",

            "#063FUmmmm...\x02\x03",

            "Grandpa did make something called\x01",
            "a dehumidifier once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1006F#7PA dehumidifier? So it removes water\x01",
            "vapor from the air, right?\x02\x03",

            "That's perfect! Could we use that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x107,
        (
            "#561F#5PUmmm, I don't think so.\x01",
            "It's meant to be used indoors.\x02\x03",

            "#063FYou'd need hundreds to affect a place\x01",
            "as big as Rolent...\x02\x03",

            "And even if we had them all, it wouldn't\x01",
            "fix the actual problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1007F#7P*sigh* Technology fails us, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x108,
        (
            "#3P#074FIt'd also be nice if we had some solid\x01",
            "evidence the society is behind this.\x02\x03",

            "This feels a little...half-cooked,\x01",
            "I think. For them, anyway.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #156
        0x101,
        (
            "#1004F#7PI think you mean 'half-baked'...\x01",
            "and, uh, what makes you say that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x108,
        (
            "#3P#072FSo far, everything they've used their\x01",
            "Gospels for has been sort of world-shaking\x01",
            "phenomena, right? Literally, in one case.\x02\x03",

            "But just producing some fog isn't really\x01",
            "that impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x101,
        (
            "#1002F#7PGood point. You'd think this would be like\x01",
            "a...flesh-eating...doom-fog...thing,\x01",
            "or something, coming from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x104,
        (
            "#035F#5PAh, and let us not forget.\x02\x03",

            "#030FEvery time, they have given us a message\x01",
            "in some form or another.\x02\x03",

            "This time, however, not a murmur.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #160
        0x101,
        "#1004F#6PWait, have they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x104,
        (
            "#035F#5PMy rival's ghostly projections, the wolf\x01",
            "appearing amongst sheep, and our\x01",
            "kitten's lovely letters.\x02\x03",

            "#030FEach time, there were provocative signs\x01",
            "spurring us into action. But here? Silence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        "#1015F#6PThat's true, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x8,
        (
            "#742FHm. Put like that, it does come across\x01",
            "as rather half-baked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        "#522F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        (
            "#743FHmm?\x02\x03",

            "Schera, is something the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x103,
        (
            "#026F#6PA message...\x02\x03",

            "#022FWe may have received one already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x8,
        "#742FWhat...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #168
        0x101,
        "#1020F#6PWhat? When did we--\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xF, 4170, 0, 108710, 0)

    NpcTalk(    #169
        0xF,
        "Man's Voice",
        "#2P#3SH-Help! Someone!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_49D9():

        label("loc_49D9")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_49D9")

    QueueWorkItem2(0x101, 3, lambda_49D9)

    def lambda_49EA():

        label("loc_49EA")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_49EA")

    QueueWorkItem2(0x103, 3, lambda_49EA)

    def lambda_49FB():

        label("loc_49FB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_49FB")

    QueueWorkItem2(0x106, 3, lambda_49FB)

    def lambda_4A0C():

        label("loc_4A0C")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_4A0C")

    QueueWorkItem2(0x104, 3, lambda_4A0C)

    def lambda_4A1D():

        label("loc_4A1D")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_4A1D")

    QueueWorkItem2(0x105, 3, lambda_4A1D)

    def lambda_4A2E():

        label("loc_4A2E")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_4A2E")

    QueueWorkItem2(0x107, 3, lambda_4A2E)

    def lambda_4A3F():

        label("loc_4A3F")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_4A3F")

    QueueWorkItem2(0x108, 3, lambda_4A3F)

    def lambda_4A50():
        OP_6D(2380, 0, 113020, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A50)
    Sleep(1000)
    OP_43(0xF, 0x0, 0x1, 0x6)
    WaitChrThread(0x101, 0x1)

    def lambda_4A79():
        OP_6D(-420, 200, 116820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A79)

    def lambda_4A91():
        OP_6B(2720, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A91)

    def lambda_4AA1():
        OP_8F(0xFE, 0xFFFFFC40, 0x0, 0x1C174, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_4AA1)
    Sleep(100)

    def lambda_4AC1():
        OP_8F(0xFE, 0x80C, 0x0, 0x1BE86, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4AC1)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0x106, 0x3)
    OP_44(0x104, 0x3)
    OP_44(0x105, 0x3)
    OP_44(0x107, 0x3)
    OP_44(0x108, 0x3)

    ChrTalk(    #170
        0x101,
        "#1026F#4PMayor Klaus?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't met Mayor Klaus again yet.\x01",      # 0
            "Set as have met Mayor Klaus again.\x01",             # 1
            "No change\x01",                                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BC3"),
        (1, "loc_4BC9"),
        (SWITCH_DEFAULT, "loc_4BCF"),
    )


    label("loc_4BC3")

    OP_A3(0x1881)
    Jump("loc_4BCF")

    label("loc_4BC9")

    OP_A2(0x1881)
    Jump("loc_4BCF")

    label("loc_4BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB4")

    ChrTalk(    #171
        0xF,
        (
            "#603F*wheeze* *wheeze*\x02\x03",

            "#604FO-Oh, Estelle, hello...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1025F#4POh, Mayor Klaus! Hi...uh...\x02\x03",

            "What's wrong? You look like you just ran\x01",
            "a marathon.\x02\x03",

            "#1015F...Wait, why am I getting the weirdest\x01",
            "sense of deja vu?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D8B")

    label("loc_4CB4")


    ChrTalk(    #173
        0xF,
        (
            "#603F*wheeze* *wheeze*\x02\x03",

            "#604FO-Oh, good, you're all...*wheeze*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1025F#4PMayor Klaus!\x01",
            "What's wrong? You look like you just ran\x01",
            "a marathon.\x02\x03",

            "#1015F...Wait, why am I getting the weirdest\x01",
            "sense of deja vu?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D8B")


    ChrTalk(    #175
        0x103,
        (
            "#022F#2PMayor Klaus, please, catch your breath.\x02\x03",

            "Has something happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xF,
        (
            "#604FHas something... You could say that, yes...\x02\x03",

            "#602FI'm glad to see you're all safe,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x103,
        "#023F#2PMayor, what do you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x8,
        "#743FMayor, if you could explain?\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x51)
    Sleep(300)

    ChrTalk(    #179
        0xF,
        (
            "#602FJust a few moments ago...\x01",
            "Lita collapsed in my home.\x02\x03",

            "Several other citizens have fainted\x01",
            "in the same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        "#1020F#4P*gasp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        "#742FWhat?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 38)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0101   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_5_3B06 end

    def Function_6_4F52(): pass

    label("Function_6_4F52")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)

    def lambda_4F6D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F6D)
    OP_8E(0xFE, 0xF64, 0x0, 0x1B01C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x352, 0x0, 0x1B9E0, 0xBB8, 0x0)
    OP_8E(0xFE, 0x29E, 0x0, 0x1BD78, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_4F52 end

    def Function_7_4FBD(): pass

    label("Function_7_4FBD")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FD4")
    Call(0, 39)
    Call(1, 19)

    label("loc_4FD4")

    OP_4A(0x8, 255)
    SetChrFlags(0x11, 0x80)
    OP_6D(340, 0, 118500, 0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(315000, 0)
    OP_6E(292, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #182
        0x8,
        "#743F#4POh, my...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x101, 3810, 0, 110590, 315)
    SetChrPos(0x102, 3810, 0, 110590, 315)
    SetChrPos(0xF8, 3810, 0, 110590, 315)
    SetChrPos(0xF9, 3810, 0, 110590, 315)

    def lambda_50AB():
        OP_6D(90, 0, 117790, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50AB)

    def lambda_50C3():
        OP_67(0, 6910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_50C3)

    def lambda_50DB():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_50DB)

    def lambda_50EB():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_50EB)
    OP_43(0x101, 0x1, 0x1, 0x8)
    Sleep(400)
    OP_43(0x102, 0x1, 0x1, 0x9)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x1, 0xA)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x1, 0xB)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_538F")

    ChrTalk(    #183
        0x103,
        "#021FHi, Aina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#1006F#5PWe're back!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x102,
        "#1035F#6PAina... Hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x8,
        (
            "#743F#4PSchera, Estelle...Joshua?!\x02\x03",

            "#741FOh, thank Aidios, you're safe!\x02\x03",

            "I was so worried! Something bizarre happened\x01",
            "at the tower while you were there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x103,
        (
            "#025FIt got a bit hairy, yes. But we managed\x01",
            "to come out with MOST of our limbs.\x02\x03",

            "#524FI imagine things have been\x01",
            "no picnic here, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "#745F#4PYes... There's been a lot of frightened\x01",
            "talk, but no one's done anything foolish.\x01",
            "Yet.\x02\x03",

            "#740FFather Divine and Mayor Klaus\x01",
            "have both been working hard to\x01",
            "keep everyone calm. It's helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#1025F#5PI see...\x02",
    )

    CloseMessageWindow()
    Jump("loc_55AB")

    label("loc_538F")


    ChrTalk(    #190
        0x101,
        "#1006F#5PHiya, Aina!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x102,
        "#1035F#6PAina... Hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#741F#4POh, thank Aidios, you're safe!\x02\x03",

            "#740FI was so worried! Something bizarre happened\x01",
            "at the tower while you were there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x101,
        (
            "#1016FUh, bizarre, yeah, that kinda\x01",
            "sums it up. We're okay, though!\x02\x03",

            "#1025FI'm gonna guess it's been\x01",
            "kinda rough here too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x8,
        (
            "#745F#4PYes... There's been a lot of frightened\x01",
            "talk, but no one's done anything foolish.\x01",
            "Yet.\x02\x03",

            "#740FFather Divine and Mayor Klaus\x01",
            "have both been working hard to\x01",
            "keep everyone calm. It's helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#1025FI see...\x02",
    )

    CloseMessageWindow()

    label("loc_55AB")


    ChrTalk(    #196
        0x8,
        (
            "#740F#4PPutting all that aside, though.\x02\x03",

            "#741FJoshua...I'm glad you've come home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        (
            "#1035F#6PYes...\x02\x03",

            "#1043FI'm sorry I caused everyone to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#744F#4PIt's all right.\x02\x03",

            "#740FAs a guild receptionist, you bracers\x01",
            "are a bit like my children.\x02\x03",

            "Especially when it comes to a certain\x01",
            "pair of someones whom I gave their first\x01",
            "Bracer Notebooks to.\x02\x03",

            "#741FThe mother in me is just glad\x01",
            "to see her child return safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#1040F#6PAina...I don't...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57D5")

    ChrTalk(    #200
        0x103,
        "#027FHeehee.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #201
        0x101,
        (
            "#1008F#2PAhaha! Told you everyone still\x01",
            "cares, Joshua!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5818")

    label("loc_57D5")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #202
        0x101,
        (
            "#1008F#2PAhaha! Told you everyone still\x01",
            "cares, Joshua!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5818")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #203
        0x101,
        (
            "#1004F#5PAnyway, Aina!\x02\x03",

            "#1002FThere's, uh, kind of a lot\x01",
            "to talk about, actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x8,
        (
            "#744F#4PThat floating island to start with, yes?\x02\x03",

            "#742FIf you have ANY idea what that\x01",
            "thing is, could you tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        "#1042F#6PRight. It began with...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #206
        (
            "\x07\x05Estelle and company told Aina about how the city\x01",
            "appeared, and about the Zero Field Generator.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #207
        0x8,
        (
            "#744F#4PI see.\x01",
            "So that's the Aureole.\x02\x03",

            "It isn't even close to what\x01",
            "I thought it might be...\x02\x03",

            "#742FIt sounds like there's little\x01",
            "we can do about it for now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AEB")

    ChrTalk(    #208
        0x103,
        (
            "#025FYes... Frustrating, but there it is.\x02\x03",

            "#022FWe need to restore some semblance of\x01",
            "order before worrying about anything else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C23")

    label("loc_5AEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B93")

    ChrTalk(    #209
        0x106,
        (
            "#053FYeah. Pisses me off, but we have\x01",
            "other things to worry about.\x02\x03",

            "#555FFirst we gotta stop runnin' around like\x01",
            "chickens with our heads cut off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C23")

    label("loc_5B93")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C23")

    ChrTalk(    #210
        0x108,
        (
            "#074FYes... It is frustrating, but\x01",
            "other concerns come first.\x02\x03",

            "#070FSuch as making sure all our\x01",
            "guildhouses can communicate!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC9")

    ChrTalk(    #211
        0x8,
        (
            "#744FAnd it'll be nice to have a\x01",
            "working phone, in that case.\x02\x03",

            "#740FCould you go ahead and set up\x01",
            "that 'Zero Field Generator,' then?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D3E")

    label("loc_5CC9")


    ChrTalk(    #212
        0x8,
        (
            "#744FAnd it'll be nice to have a\x01",
            "working phone, in that case.\x02\x03",

            "#740FCould you go ahead and\x01",
            "get us set up, then?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E6A")

    ChrTalk(    #213
        0x107,
        "#560FUh-huh! Just a minute.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 20)
    SetChrPos(0x107, -560, 0, 119000, 0)
    TurnDirection(0x8, 0x107, 0)
    OP_6D(-810, 0, 119530, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(314000, 0)
    OP_6E(309, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #214
        0x107,
        (
            "#061F#6POkay!\x01",
            "It should be all good now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #215
        "\x07\x05Tita flipped the switch on the phone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_5F8C")

    label("loc_5E6A")


    ChrTalk(    #216
        0x102,
        "#1040F#6PYes, just a moment...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(1, 20)
    SetChrPos(0x102, -560, 0, 119000, 0)
    TurnDirection(0x8, 0x102, 0)
    OP_6D(-810, 0, 119530, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2290, 0)
    OP_6C(314000, 0)
    OP_6E(309, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #217
        0x102,
        (
            "#1035F#6PThere we are.\x01",
            "It should work now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #218
        "\x07\x05Joshua flipped the switch on the phone.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5F8C")

    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x83, 0x0, 0x64)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #219
        0x8,
        "#743FIt sounds like it's working!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60B9")
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #220
        0x107,
        (
            "#560F#6PThis phone should work fine now!\x02\x03",

            "You, um, won't be able to call anyone\x01",
            "until their phones work too, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_613A")

    label("loc_60B9")

    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #221
        0x102,
        (
            "#1040F#6PIt should work now.\x02\x03",

            "You won't be able to make calls\x01",
            "until the receiver's phone is\x01",
            "also functional, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_613A")


    ChrTalk(    #222
        0x8,
        (
            "#744FThank you!\x01",
            "This is a big help.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_616E():
        OP_6D(-150, 0, 118340, 1100)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_616E)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #223
        0x8,
        (
            "#740F#4PThank you, everyone.\x01",
            "I'll repay you for this someday.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61E7")
    OP_8C(0x107, 135, 400)
    Jump("loc_61EE")

    label("loc_61E7")

    OP_8C(0x102, 135, 400)

    label("loc_61EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62D4")

    ChrTalk(    #224
        0x103,
        (
            "#021FHmmmmmm, well, in that case, your treat\x01",
            "the next time we go out for drinks, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x8,
        "#741F#4PHaha! All right then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x102,
        (
            "#1052FWell, good to know there are some\x01",
            "constants in the universe...I suppose...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_638D")

    label("loc_62D4")


    ChrTalk(    #227
        0x101,
        (
            "#1016F#5POh, don't worry, Aina. It's only natural\x01",
            "for 'kids' to help around the house, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#1040FAt worst, we're doing our duty.\x01",
            "At best...yes. Don't worry about it, Aina.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_638D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6427")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as fixed all phones\x01",      # 0
            "Set as only fixed here\x01",       # 1
            "No change\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6415"),
        (1, "loc_641E"),
        (SWITCH_DEFAULT, "loc_6427"),
    )


    label("loc_6415")

    OP_A2(0x2001)
    OP_A2(0x2005)
    Jump("loc_6427")

    label("loc_641E")

    OP_A3(0x2001)
    OP_A3(0x2005)
    Jump("loc_6427")

    label("loc_6427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_67BC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_64D3")

    ChrTalk(    #229
        0x108,
        (
            "#070FAnd with that, all the phones\x01",
            "should work now.\x02\x03",

            "We should return to the professor\x01",
            "and Captain Schwarz and inform\x01",
            "them of our success.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_661C")

    label("loc_64D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6587")

    ChrTalk(    #230
        0x103,
        (
            "#020FWell, then!\x01",
            "That's all the phones made functional.\x02\x03",

            "We should let Professor Russell and Captain\x01",
            "Schwarz know about our success\x01",
            "and what's been going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_661C")

    label("loc_6587")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661C")

    ChrTalk(    #231
        0x106,
        (
            "#051FAll right, that's all the phones\x01",
            "workin' again.\x02\x03",

            "We oughtta get back to Gramps and the\x01",
            "captain and let 'em know what's what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_661C")

    OP_59()
    OP_28(0x9B, 0x4, 0x10)
    OP_AF(0x67, 0x9B)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_28(0x9B, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66B2")

    ChrTalk(    #232
        0x8,
        (
            "#741F#4PReally, well done, everyone.\x02\x03",

            "I will be able to get word out\x01",
            "quickly if anything happens.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_670E")

    label("loc_66B2")


    ChrTalk(    #233
        0x8,
        (
            "#741F#4PEveryone, really, fantastic work!\x02\x03",

            "Now I can get word out\x01",
            "if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_670E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6752")

    ChrTalk(    #234
        0x108,
        (
            "#070FIs there anything else\x01",
            "we can help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67B9")

    label("loc_6752")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_678D")

    ChrTalk(    #235
        0x103,
        "#020FNeed a hand with anything else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_67B9")

    label("loc_678D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67B9")

    ChrTalk(    #236
        0x106,
        "#051FNeed anything else?\x02",
    )

    CloseMessageWindow()

    label("loc_67B9")

    Jump("loc_6977")

    label("loc_67BC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_684F")

    ChrTalk(    #237
        0x108,
        (
            "#070FWe must depart soon to assist\x01",
            "the other guildhouses.\x02\x03",

            "Before we leave, though, is there\x01",
            "anything else we can help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6977")

    label("loc_684F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_68C8")

    ChrTalk(    #238
        0x106,
        (
            "#051FWell, we gotta get a move on and\x01",
            "get the rest of the guild going, but...\x02\x03",

            "Need anything else?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6977")

    label("loc_68C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6977")

    ChrTalk(    #239
        0x103,
        (
            "#020FWell, at this point, it's time to\x01",
            "put our weary feet back on the road\x01",
            "to help the other guildhouses.\x02\x03",

            "Need a hand with anything\x01",
            "before we leave, Aina?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6977")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A9A")

    ChrTalk(    #240
        0x8,
        (
            "#744F#4PHmm. Since you offered...\x02\x03",

            "#740FWould you be willing to\x01",
            "check the board for jobs?\x02\x03",

            "Also, if you could make a quick\x01",
            "patrol circuit of the outskirts of\x01",
            "Rolent, I would appreciate it.\x02\x03",

            "I'm rather worried about the Malga Mine\x01",
            "in particular. Ridge went out there...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B8A")

    label("loc_6A9A")


    ChrTalk(    #241
        0x8,
        (
            "#744F#4PHmm.\x02\x03",

            "#740FActually, could you check the\x01",
            "board and see what's posted?\x02\x03",

            "Also...if you could swing by\x01",
            "the outskirts of Rolent and\x01",
            "check on things, I'd be grateful.\x02\x03",

            "I'm a bit worried about Malga Mine,\x01",
            "where Ridge is right now...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8A")


    ChrTalk(    #242
        0x101,
        (
            "#1004F#5PHuh? Did something happen\x01",
            "at the mine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x8,
        (
            "#740F#4PNo, it's nothing serious.\x01",
            "He was just on guard duty.\x02\x03",

            "You remember how the cave-in a while back\x01",
            "opened a tunnel to a monster nest, right?\x02\x03",

            "A few days ago, the mining crew began a\x01",
            "serious effort to close that tunnel off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x102,
        (
            "#1043FAnd then right in the\x01",
            "middle of that...\x02\x03",

            "I can understand your worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x8,
        (
            "#740F#4PYes, if you have some time, it would\x01",
            "be nice if you can check on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#1006F#5POkay, sure.\x02\x03",

            "We'll check all the places outside\x01",
            "town we know're inhabited, like\x01",
            "Tio's place and the mines.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #247
        0x102,
        "#1040FYes, let's keep an eye out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x8,
        "#741F#4PI appreciate it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #249
        (
            "\x07\x05With the phone fixed, you can call the team from\x01",
            "another branch to Rolent. If you wish to call them,\x01",
            "select 'Call Allies' when speaking to Aina.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_4B(0x8, 255)
    OP_A2(0x2003)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6ED7")
    OP_A2(0x2091)
    Jump("loc_6EDA")

    label("loc_6ED7")

    OP_A3(0x2091)

    label("loc_6EDA")

    OP_28(0x9B, 0x2, 0x40)
    OP_28(0x9B, 0x1, 0x80)
    OP_6D(520, 0, 114520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 520, 0, 114520, 135)
    SetChrPos(0x1, 520, 0, 114520, 135)
    SetChrPos(0x2, 520, 0, 114520, 135)
    SetChrPos(0x3, 520, 0, 114520, 135)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_4FBD end

    def Function_8_6F78(): pass

    label("Function_8_6F78")

    OP_8E(0xFE, 0x942, 0x0, 0x1B7D8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x1C6D8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_8_6F78 end

    def Function_9_6FA8(): pass

    label("Function_9_6FA8")

    OP_8E(0xFE, 0x500, 0x0, 0x1B80A, 0x9C4, 0x0)
    OP_8E(0xFE, 0x190, 0x0, 0x1C6D8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_9_6FA8 end

    def Function_10_6FD8(): pass

    label("Function_10_6FD8")

    OP_8E(0xFE, 0x942, 0x0, 0x1B7D8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x5DC, 0x0, 0x1C264, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_6FD8 end

    def Function_11_7008(): pass

    label("Function_11_7008")

    OP_8E(0xFE, 0x500, 0x0, 0x1B80A, 0x9C4, 0x0)
    OP_8E(0xFE, 0x190, 0x0, 0x1C264, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_7008 end

    def Function_12_7038(): pass

    label("Function_12_7038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7052")
    Return()

    label("loc_7052")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7072")
    Call(0, 39)
    Call(1, 19)
    FadeToBright(0, 0)

    label("loc_7072")

    OP_22(0xC3, 0x1, 0x64)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x8, 255)

    ChrTalk(    #250
        0x101,
        "#1004FWhoa!\x02",
    )

    CloseMessageWindow()

    def lambda_70EF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_70EF)

    def lambda_70FD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_70FD)
    Sleep(100)

    def lambda_7110():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_7110)
    OP_8C(0x3, 0, 400)

    ChrTalk(    #251
        0x8,
        (
            "#743F#6PDamn. It starts ringing off the\x01",
            "hook as soon as we turn it back\x01",
            "on. Never fails, I suppose...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-1130, 0, 119950, 0)
    OP_67(0, 5790, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    SetChrPos(0x101, 3810, 0, 110590, 0)
    SetChrPos(0x102, 3810, 0, 110590, 0)
    SetChrPos(0xF8, 3810, 0, 110590, 0)
    SetChrPos(0xF9, 3810, 0, 110590, 0)
    OP_8C(0x8, 315, 0)
    OP_8E(0x8, 0xFFFFFDD0, 0x0, 0x1D0D8, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(700)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    PlayEffect(0x1, 0x1, 0xFF, -290, 1900, 119600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_43(0x101, 0x0, 0x1, 0xD)
    Sleep(500)

    ChrTalk(    #252
        0x8,
        (
            "#742F#6PBracer Guild, Rolent Branch.\x02\x03",

            "#743FOh! Elnan!\x01",
            "So yours is fixed too, then.\x02\x03",

            "#741FYes, ours was just restored\x01",
            "to working order.\x02\x03",

            "#740F...Them? They're still in\x01",
            "front of me, in fact.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x0)

    def lambda_735A():
        OP_6D(-730, 0, 118880, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_735A)

    def lambda_7372():
        OP_67(0, 5820, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7372)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #253
        0x101,
        "#1004F#5P(Does she mean us?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        "#1044F#5P(Sounds like Elnan wants to talk to us.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x8,
        (
            "#744F#6P...Yes... Yes.\x02\x03",

            "...\x02\x03",

            "#740FUnderstood, I'll tell them.\x02\x03",

            "I'll call again in a bit to report\x01",
            "on our situation here.\x02\x03",

            "#741FAll right. Good luck, and I'll\x01",
            "be in touch.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74D5")

    ChrTalk(    #256
        0x103,
        "#023FAina, that was Elnan?\x02",
    )

    CloseMessageWindow()
    Jump("loc_750F")

    label("loc_74D5")


    ChrTalk(    #257
        0x101,
        (
            "#1015F#5PUh, Aina? What's up?\x01",
            "That was Elnan, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_750F")

    OP_8E(0x8, 0x2EE, 0x0, 0x1CF48, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #258
        0x8,
        (
            "#740F#4PYes, that was Elnan in Grancel.\x02\x03",

            "Apparently, Her Majesty the Queen\x01",
            "would like to speak to you.\x02\x03",

            "The message was to stop by Grancel\x01",
            "Castle if you visit the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x101,
        "#1004F#5PThe QUEEN?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7637")

    ChrTalk(    #260
        0x106,
        (
            "#052FKinda outta the blue...\x01",
            "Wonder what's up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76DC")

    label("loc_7637")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_767F")

    ChrTalk(    #261
        0x108,
        (
            "#073FThis is a surprise.\x01",
            "I wonder what she wants.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76DC")

    label("loc_767F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76DC")

    ChrTalk(    #262
        0x103,
        (
            "#023FWell, that's a shot of liquor up the\x01",
            "nose. I wonder what's happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7774")

    ChrTalk(    #263
        0x8,
        (
            "#744F#4PElnan couldn't share any details...\x02\x03",

            "#742FEvidently it's something they would\x01",
            "rather not share over the phone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_77FE")

    label("loc_7774")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77FE")

    ChrTalk(    #264
        0x8,
        (
            "#744F#4PElnan couldn't share any details...\x02\x03",

            "#742FEvidently it's something they would\x01",
            "rather not share over the phone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77FE")


    ChrTalk(    #265
        0x101,
        (
            "#1015F#5PSomething you can't say over the phone...\x02\x03",

            "#1026FI get it. Phone calls run the\x01",
            "risk of being intercepted...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x102,
        "#1042F#5PIt must be something secret, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x8,
        (
            "#740F#4PElnan made it clear that it wasn't\x01",
            "an emergency, however.\x02\x03",

            "It sounded like you should just\x01",
            "stop in when you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        "#1006F#5PHmm. Okay, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7995")

    ChrTalk(    #269
        0x103,
        "#021FWe'll head over there when we can, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_79C6")

    label("loc_7995")


    ChrTalk(    #270
        0x102,
        "#1040F#5PWe'll try to find some time, then.\x02",
    )

    CloseMessageWindow()

    label("loc_79C6")

    OP_A2(0x2004)
    OP_28(0x9B, 0x1, 0x100)
    OP_28(0x9B, 0x1, 0x200)
    OP_28(0x9B, 0x1, 0x400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_6D(520, 0, 114520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 520, 0, 114520, 135)
    SetChrPos(0x1, 520, 0, 114520, 135)
    SetChrPos(0x2, 520, 0, 114520, 135)
    SetChrPos(0x3, 520, 0, 114520, 135)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_12_7038 end

    def Function_13_7A83(): pass

    label("Function_13_7A83")

    OP_43(0x101, 0x1, 0x1, 0x8)
    Sleep(400)
    OP_43(0x102, 0x1, 0x1, 0x9)
    Sleep(600)
    OP_43(0xF8, 0x1, 0x1, 0xA)
    Sleep(400)
    OP_43(0xF9, 0x1, 0x1, 0xB)
    WaitChrThread(0xF8, 0x1)
    Return()

    # Function_13_7A83 end

    def Function_14_7AB4(): pass

    label("Function_14_7AB4")

    OP_8E(0xFE, 0x2E4, 0x0, 0x1B95E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1B8, 0x0, 0x1C76E, 0x7D0, 0x0)

    def lambda_7AE2():

        label("loc_7AE2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_7AE2")

    QueueWorkItem2(0xFE, 2, lambda_7AE2)
    Return()

    # Function_14_7AB4 end

    def Function_15_7AEE(): pass

    label("Function_15_7AEE")

    OP_8E(0xFE, 0x802, 0x0, 0x1B94A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x492, 0x0, 0x1C778, 0x7D0, 0x0)

    def lambda_7B1C():

        label("loc_7B1C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_7B1C")

    QueueWorkItem2(0xFE, 2, lambda_7B1C)
    Return()

    # Function_15_7AEE end

    def Function_16_7B28(): pass

    label("Function_16_7B28")

    OP_8E(0xFE, 0x2E4, 0x0, 0x1B95E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF24, 0x0, 0x1C570, 0x7D0, 0x0)

    def lambda_7B56():

        label("loc_7B56")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_7B56")

    QueueWorkItem2(0xFE, 2, lambda_7B56)
    Return()

    # Function_16_7B28 end

    def Function_17_7B62(): pass

    label("Function_17_7B62")

    OP_8E(0xFE, 0x802, 0x0, 0x1B94A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x78A, 0x0, 0x1C6B0, 0x7D0, 0x0)

    def lambda_7B90():

        label("loc_7B90")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_7B90")

    QueueWorkItem2(0xFE, 2, lambda_7B90)
    Return()

    # Function_17_7B62 end

    def Function_18_7B9C(): pass

    label("Function_18_7B9C")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(-1470, 0, 125030, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 300, 0, 116600, 135)
    SetChrPos(0x101, 1840, 0, 115000, 0)
    SetChrPos(0x102, 710, 0, 115000, 0)
    SetChrPos(0xF8, 1840, 0, 113800, 0)
    SetChrPos(0xF9, 740, 0, 113800, 0)
    Sleep(1000)

    def lambda_7C4E():
        OP_6D(250, 0, 116610, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C4E)

    def lambda_7C66():
        OP_67(0, 6910, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C66)

    def lambda_7C7E():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C7E)

    def lambda_7C8E():
        OP_6E(294, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_7C8E)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x3)
    Sleep(400)

    ChrTalk(    #271
        0x8,
        (
            "#745FBoy, that sounds like some mess.\x02\x03",

            "If things had gone even a little wrong,\x01",
            "everything would have ended in tragedy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x15,
        (
            "#6PYep. It was the missy here and\x01",
            "her friends who saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x15,
        (
            "#6PLast time she came to help us,\x01",
            "she seemed a little...unreliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x15,
        (
            "#6PThis time, though? Night and day. It's\x01",
            "like a whole new person came to help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x15, 400)

    ChrTalk(    #275
        0x101,
        (
            "#1008F#2PHuh? H-Hey, now...\x02\x03",

            "I don't think I've changed,\x01",
            "uh, all THAT much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x15,
        "#6PAin't no cause to be humble, missy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x15,
        "#6PIt's how I feel, and it's the truth.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #278
        0x102,
        (
            "#1048F#1PI'm not entirely sure it's 'humility.'\x02\x03",

            "#1035FGiven that it's Estelle, I think she just\x01",
            "hasn't realized how she's changed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F76")

    ChrTalk(    #279
        0x107,
        "#560FHeehee! Maybe!\x02",
    )

    CloseMessageWindow()

    label("loc_7F76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FA0")

    ChrTalk(    #280
        0x103,
        "#021FI could see that.\x02",
    )

    CloseMessageWindow()

    label("loc_7FA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FF9")

    ChrTalk(    #281
        0x106,
        (
            "#051FHey, it's no big. She's straightforward.\x01",
            "That's a virtue. Sorta.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF9")

    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    OP_8C(0x101, 180, 400)
    Sleep(600)

    ChrTalk(    #282
        0x101,
        (
            "#1019F#2PMan...\x02\x03",

            "I THINK I'm being complimented,\x01",
            "but somehow it doesn't feel all\x01",
            "warm and fuzzy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x8,
        (
            "#741FIt IS hard to notice change\x01",
            "in yourself, Estelle.\x02\x03",

            "Remember, people change little\x01",
            "by little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x15,
        (
            "#6PExactly right. I probably noticed\x01",
            "'cause it's been so darn long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x15,
        (
            "#6PPoint is, missy, you did a hell\x01",
            "of a job in there. Be proud.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822E")

    ChrTalk(    #286
        0x8,
        (
            "#740FYes, Estelle, Joshua...\x02\x03",

            "And Agate, Schera, you too...\x02\x03",

            "You really did a fantastic\x01",
            "job this time.\x02\x03",

            "I'm proud to call you all\x01",
            "guildmates today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_862E")

    label("loc_822E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_82E1")

    ChrTalk(    #287
        0x8,
        (
            "#740FYes, Estelle, Joshua...\x02\x03",

            "And Zin, Schera, you too...\x02\x03",

            "You really did a fantastic\x01",
            "job this time.\x02\x03",

            "I'm proud to call you all\x01",
            "guildmates today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_862E")

    label("loc_82E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83D2")

    ChrTalk(    #288
        0x8,
        (
            "#740FYes, Estelle, Joshua...\x02\x03",

            "And Schera, and even you,\x01",
            "Tita, you little darling...\x02\x03",

            "You really did a fantastic\x01",
            "job this time.\x02\x03",

            "I'm proud to call you all guildmates\x01",
            "today! Even Tita, as far as I'm\x01",
            "concerned!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_862E")

    label("loc_83D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_846F")

    ChrTalk(    #289
        0x8,
        (
            "#740FEstelle, Joshua, Zin, Agate...\x02\x03",

            "You really did a fantastic\x01",
            "job this time.\x02\x03",

            "I'm proud to call you all\x01",
            "guildmates today!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_862E")

    label("loc_846F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_855F")

    ChrTalk(    #290
        0x8,
        (
            "#740FYes, Estelle, Joshua...\x02\x03",

            "And Agate, and even you,\x01",
            "Tita, you little darling...\x02\x03",

            "You really did a fantastic\x01",
            "job this time.\x02\x03",

            "I'm proud to call you all guildmates\x01",
            "today! Even Tita, as far as I'm\x01",
            "concerned!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_862E")

    label("loc_855F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_862E")

    ChrTalk(    #291
        0x8,
        (
            "#740FEstelle, Agate, Zin, and yes,\x01",
            "even you, Tita...\x02\x03",

            "You really did a fantastic\x01",
            "job this time.\x02\x03",

            "I'm proud to call you all guildmates\x01",
            "today! Even Tita, as far as I'm\x01",
            "concerned!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_862E")


    def lambda_8634():
        OP_8C(0x102, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8634)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #292
        0x101,
        "#1017F#5PDon't worry, it was a piece of cake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x102,
        "#1041F#1PWe did the best we could.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86BE")

    ChrTalk(    #294
        0x107,
        "#067FHeehee!\x02",
    )

    CloseMessageWindow()

    label("loc_86BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86F2")

    ChrTalk(    #295
        0x108,
        "#070FIt was all in a day's work.\x02",
    )

    CloseMessageWindow()

    label("loc_86F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8724")

    ChrTalk(    #296
        0x106,
        "#051FHeh. Just doin' our jobs.\x02",
    )

    CloseMessageWindow()

    label("loc_8724")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8884")

    ChrTalk(    #297
        0x103,
        (
            "#021FIf you really think that, Aina,\x01",
            "buy me a drink next time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0x8,
        (
            "#741FOh, just one?\x01",
            "Are you sure?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x103,
        (
            "#525FSo long as you'll throw\x01",
            "in for some Steinrose? Absolutely.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #300
        0x101,
        (
            "#1007F#5PHow does every conversation between\x01",
            "these two come back to alcohol...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x102,
        "#1048F#1PAs inevitable as death and taxes...\x02",
    )

    CloseMessageWindow()

    label("loc_8884")


    ChrTalk(    #302
        0x15,
        (
            "#6PRight, then. You all deserve\x01",
            "a more proper thanks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x15,
        (
            "#6PI really need to get back to\x01",
            "the mine, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x15,
        (
            "#6PDespite everything that happened,\x01",
            "we're gonna keep working.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #305
        0x101,
        "#1004F#2PReally? Wow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x15,
        (
            "#6PYeah, we can still get plenty\x01",
            "done in the upper levels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x15,
        (
            "#6PGive my best to Ridge, too,\x01",
            "will you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x8, 400)

    ChrTalk(    #308
        0x15,
        (
            "#6PHope he ends up okay. Looked like\x01",
            "he got worked over by a Cronocider...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x8,
        (
            "#740FHe's suffered some injury, but\x01",
            "he's a bracer. He'll pull through.\x02\x03",

            "In fact, he's already awake. He should\x01",
            "be resting at the hotel right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x15,
        "#6PThat's a relief.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 135, 400)

    ChrTalk(    #311
        0x15,
        (
            "#6PI'll be heading out then. Thanks again.\x01",
            "You really saved our bacon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        "#1006F#2PTake care, Chief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x102,
        "#1040F#1PGood luck!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x15,
        "#6PSee you!\x02",
    )

    CloseMessageWindow()

    def lambda_8B76():
        OP_6D(-30, 0, 115770, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8B76)

    def lambda_8B8E():

        label("loc_8B8E")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_8B8E")

    QueueWorkItem2(0x8, 1, lambda_8B8E)

    def lambda_8B9F():

        label("loc_8B9F")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_8B9F")

    QueueWorkItem2(0x101, 1, lambda_8B9F)

    def lambda_8BB0():

        label("loc_8BB0")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_8BB0")

    QueueWorkItem2(0x102, 1, lambda_8BB0)

    def lambda_8BC1():

        label("loc_8BC1")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_8BC1")

    QueueWorkItem2(0xF8, 1, lambda_8BC1)

    def lambda_8BD2():

        label("loc_8BD2")

        TurnDirection(0xFE, 0x15, 400)
        OP_48()
        Jump("loc_8BD2")

    QueueWorkItem2(0xF9, 1, lambda_8BD2)
    SetChrFlags(0x15, 0x40)
    OP_8E(0x15, 0xFFFFFEB6, 0x0, 0x1BB5C, 0x7D0, 0x0)
    OP_8E(0x15, 0x104A, 0x0, 0x1AE28, 0x7D0, 0x0)
    OP_8C(0x15, 180, 400)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_8C21():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_8C21)
    OP_8E(0x15, 0x1072, 0x0, 0x1A7DE, 0x7D0, 0x0)
    WaitChrThread(0x15, 0x0)
    SetChrFlags(0x15, 0x80)
    OP_22(0x7, 0x0, 0x64)
    OP_44(0x11, 0x1)
    OP_44(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)

    def lambda_8C75():
        OP_6D(90, 0, 117790, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8C75)
    Sleep(800)

    def lambda_8C92():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C92)
    Sleep(100)

    def lambda_8CA5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CA5)
    Sleep(200)

    def lambda_8CB8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8CB8)

    def lambda_8CC6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8CC6)
    WaitChrThread(0x101, 0x1)

    def lambda_8CD9():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CD9)
    Sleep(160)
    WaitChrThread(0x102, 0x1)

    def lambda_8CF9():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CF9)
    Sleep(150)
    WaitChrThread(0xF8, 0x1)

    def lambda_8D19():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8D19)
    Sleep(140)
    WaitChrThread(0xF9, 0x1)

    def lambda_8D39():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8D39)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #315
        0x8,
        (
            "#740FWell, that settles that.\x02\x03",

            "You and Ridge both did great work today.\x02\x03",

            "Please, try and keep it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x102,
        "#1040F#1POf course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x8,
        (
            "#740FI've also finished calculating\x01",
            "the formal results of the mission.\x02\x03",

            "Just let me know when\x01",
            "you want the payout.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x101,
        "#1001F#1PWe will!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #319
        "Quest #2C[Rescue the Miners]#0C Completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x15, 0x40)
    OP_4B(0x8, 255)
    OP_A2(0xB)
    OP_A2(0x2085)
    OP_28(0xBF, 0x4, 0x10)
    OP_28(0xBF, 0x1, 0x200)
    OP_28(0xBF, 0x1, 0x400)
    EventEnd(0x0)
    Return()

    # Function_18_7B9C end

    def Function_19_8EDF(): pass

    label("Function_19_8EDF")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_19_8EDF end

    def Function_20_8F38(): pass

    label("Function_20_8F38")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F59")
    OP_3F(0x151, 1)
    Jump("loc_9530")

    label("loc_8F59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9530")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #320
        "\x07\x05Choose member to remove Zero Field Generator from.\x02",
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FD6")
    Call(1, 21)
    Jump("loc_8FDA")

    label("loc_8FD6")

    Call(1, 22)

    label("loc_8FDA")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9001")
    Call(1, 21)
    Jump("loc_9005")

    label("loc_9001")

    Call(1, 22)

    label("loc_9005")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_902C")
    Call(1, 21)
    Jump("loc_9030")

    label("loc_902C")

    Call(1, 22)

    label("loc_9030")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9057")
    Call(1, 21)
    Jump("loc_905B")

    label("loc_9057")

    Call(1, 22)

    label("loc_905B")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_90A2"),
        (1, "loc_90E8"),
        (2, "loc_912E"),
        (3, "loc_9174"),
        (SWITCH_DEFAULT, "loc_91BA"),
    )


    label("loc_90A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90C5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90E5")

    label("loc_90C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90E5")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_90E5")

    Jump("loc_91BA")

    label("loc_90E8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_910B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_912B")

    label("loc_910B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_912B")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_912B")

    Jump("loc_91BA")

    label("loc_912E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9151")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9171")

    label("loc_9151")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9171")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9171")

    Jump("loc_91BA")

    label("loc_9174")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9197")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91B7")

    label("loc_9197")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91B7")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_91B7")

    Jump("loc_91BA")

    label("loc_91BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9201")

    AnonymousTalk(    #321
        "\x07\x05They are not equipped with a Zero Field Generator.\x02",
    )

    Jump("loc_9521")

    label("loc_9201")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9256")

    AnonymousTalk(    #322
        (
            "\x07\x05Estelle removed her Zero Field Generator. \x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_9256")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92A9")

    AnonymousTalk(    #323
        (
            "\x07\x05Joshua removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_92A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9300")

    AnonymousTalk(    #324
        (
            "\x07\x05Scherazard removed her Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_9300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9354")

    AnonymousTalk(    #325
        (
            "\x07\x05Olivier removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_9354")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93A5")

    AnonymousTalk(    #326
        (
            "\x07\x05Kloe removed her Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_93A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93F7")

    AnonymousTalk(    #327
        (
            "\x07\x05Agate removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_93F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9482")

    AnonymousTalk(    #328
        (
            "\x07\x05Tita removed her Zero Field Generator. Arts/crafts/normal\x01",
            "attacks now unavailable. S-Craft [Cannon Impulse] available.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_9482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94D2")

    AnonymousTalk(    #329
        (
            "\x07\x05Zin removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_9521")

    label("loc_94D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9521")

    AnonymousTalk(    #330
        (
            "\x07\x05Kevin removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )


    label("loc_9521")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_8F59")

    label("loc_9530")

    Return()

    # Function_20_8F38 end

    def Function_21_9531(): pass

    label("Function_21_9531")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_955E"),
        (1, "loc_9579"),
        (2, "loc_9593"),
        (3, "loc_95B1"),
        (4, "loc_95CC"),
        (5, "loc_95E4"),
        (6, "loc_95FD"),
        (7, "loc_9615"),
        (8, "loc_962C"),
        (SWITCH_DEFAULT, "loc_9645"),
    )


    label("loc_955E")

    OP_CC(0x1, 0x0, "[Estelle - Equipped]")
    Jump("loc_9645")

    label("loc_9579")

    OP_CC(0x1, 0x0, "[Joshua - Equipped]")
    Jump("loc_9645")

    label("loc_9593")

    OP_CC(0x1, 0x0, "[Scherazard - Equipped]")
    Jump("loc_9645")

    label("loc_95B1")

    OP_CC(0x1, 0x0, "[Olivier - Equipped]")
    Jump("loc_9645")

    label("loc_95CC")

    OP_CC(0x1, 0x0, "[Kloe - Equipped]")
    Jump("loc_9645")

    label("loc_95E4")

    OP_CC(0x1, 0x0, "[Agate - Equipped]")
    Jump("loc_9645")

    label("loc_95FD")

    OP_CC(0x1, 0x0, "[Tita - Equipped]")
    Jump("loc_9645")

    label("loc_9615")

    OP_CC(0x1, 0x0, "[Zin - Equipped]")
    Jump("loc_9645")

    label("loc_962C")

    OP_CC(0x1, 0x0, "[Kevin - Equipped]")
    Jump("loc_9645")

    label("loc_9645")

    Return()

    # Function_21_9531 end

    def Function_22_9646(): pass

    label("Function_22_9646")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_END)),
        (0, "loc_9673"),
        (1, "loc_9692"),
        (2, "loc_96B0"),
        (3, "loc_96D2"),
        (4, "loc_96F1"),
        (5, "loc_970D"),
        (6, "loc_972A"),
        (7, "loc_9746"),
        (8, "loc_9761"),
        (SWITCH_DEFAULT, "loc_977E"),
    )


    label("loc_9673")

    OP_CC(0x1, 0x0, "[Estelle - Not Equipped]")
    Jump("loc_977E")

    label("loc_9692")

    OP_CC(0x1, 0x0, "[Joshua - Not Equipped]")
    Jump("loc_977E")

    label("loc_96B0")

    OP_CC(0x1, 0x0, "[Scherazard - Not Equipped]")
    Jump("loc_977E")

    label("loc_96D2")

    OP_CC(0x1, 0x0, "[Olivier - Not Equipped]")
    Jump("loc_977E")

    label("loc_96F1")

    OP_CC(0x1, 0x0, "[Kloe - Not Equipped]")
    Jump("loc_977E")

    label("loc_970D")

    OP_CC(0x1, 0x0, "[Agate - Not Equipped]")
    Jump("loc_977E")

    label("loc_972A")

    OP_CC(0x1, 0x0, "[Tita - Not Equipped]")
    Jump("loc_977E")

    label("loc_9746")

    OP_CC(0x1, 0x0, "[Zin - Not Equipped]")
    Jump("loc_977E")

    label("loc_9761")

    OP_CC(0x1, 0x0, "[Kevin - Not Equipped]")
    Jump("loc_977E")

    label("loc_977E")

    Return()

    # Function_22_9646 end

    SaveToFile()

Try(main)
