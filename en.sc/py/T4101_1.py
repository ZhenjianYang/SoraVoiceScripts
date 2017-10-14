from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T4101   ._SN',
            'ED6_DT21/T4101_1 ._SN',
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
        "Function_1_AB",           # 01, 1
        "Function_2_352",          # 02, 2
        "Function_3_4C6",          # 03, 3
        "Function_4_7D5",          # 04, 4
        "Function_5_14B4",         # 05, 5
        "Function_6_220D",         # 06, 6
        "Function_7_253D",         # 07, 7
        "Function_8_29BD",         # 08, 8
        "Function_9_2DED",         # 09, 9
        "Function_10_2FE8",        # 0A, 10
        "Function_11_323B",        # 0B, 11
        "Function_12_3666",        # 0C, 12
        "Function_13_38E2",        # 0D, 13
        "Function_14_3F85",        # 0E, 14
        "Function_15_40DC",        # 0F, 15
        "Function_16_4370",        # 10, 16
        "Function_17_47DE",        # 11, 17
        "Function_18_4BAF",        # 12, 18
        "Function_19_4F18",        # 13, 19
        "Function_20_52D8",        # 14, 20
        "Function_21_53D0",        # 15, 21
        "Function_22_554B",        # 16, 22
        "Function_23_567F",        # 17, 23
        "Function_24_582B",        # 18, 24
        "Function_25_59DB",        # 19, 25
        "Function_26_5C1D",        # 1A, 26
        "Function_27_5E20",        # 1B, 27
        "Function_28_5FCF",        # 1C, 28
        "Function_29_6229",        # 1D, 29
        "Function_30_88A4",        # 1E, 30
        "Function_31_88DD",        # 1F, 31
        "Function_32_8916",        # 20, 32
        "Function_33_89D3",        # 21, 33
        "Function_34_8A91",        # 22, 34
        "Function_35_8B20",        # 23, 35
        "Function_36_8BD7",        # 24, 36
        "Function_37_8C9C",        # 25, 37
        "Function_38_8D5A",        # 26, 38
        "Function_39_8DD8",        # 27, 39
        "Function_40_8E7E",        # 28, 40
        "Function_41_8F9C",        # 29, 41
        "Function_42_90BA",        # 2A, 42
        "Function_43_91D8",        # 2B, 43
        "Function_44_9206",        # 2C, 44
        "Function_45_9234",        # 2D, 45
        "Function_46_9276",        # 2E, 46
        "Function_47_92B8",        # 2F, 47
        "Function_48_92FA",        # 30, 48
        "Function_49_933C",        # 31, 49
        "Function_50_937E",        # 32, 50
        "Function_51_93CA",        # 33, 51
        "Function_52_9407",        # 34, 52
        "Function_53_958C",        # 35, 53
        "Function_54_9664",        # 36, 54
        "Function_55_9735",        # 37, 55
        "Function_56_97C2",        # 38, 56
        "Function_57_984F",        # 39, 57
        "Function_58_997E",        # 3A, 58
        "Function_59_9B99",        # 3B, 59
        "Function_60_9C22",        # 3C, 60
        "Function_61_9D0A",        # 3D, 61
        "Function_62_A084",        # 3E, 62
        "Function_63_A2D1",        # 3F, 63
        "Function_64_A4F1",        # 40, 64
        "Function_65_A718",        # 41, 65
        "Function_66_A93F",        # 42, 66
        "Function_67_AA0D",        # 43, 67
        "Function_68_AA84",        # 44, 68
        "Function_69_AAFB",        # 45, 69
        "Function_70_AB89",        # 46, 70
        "Function_71_AC17",        # 47, 71
        "Function_72_AC3B",        # 48, 72
        "Function_73_AC61",        # 49, 73
        "Function_74_ADFA",        # 4A, 74
        "Function_75_AF95",        # 4B, 75
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D1, 2)), scpexpr(EXPR_END)), "loc_119")

    ChrTalk(    #0
        0xFE,
        (
            "#063FI wonder why Agate won't eat ice\x01",
            "cream with me...\x02\x03",

            "Will he eat with me when I grow up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E")

    label("loc_119")


    ChrTalk(    #1
        0xFE,
        (
            "#563FThe ice cream here is so yummy, too...\x02\x03",

            "#063FWhy won't Agate eat any with me?\x02\x03",

            "#064FMaybe he doesn't like ice cream?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1016FI don't think that's quite it.\x02\x03",

            "#1007FThis is Agate we're talking about.\x01",
            "He's probably just embarrassed,\x01",
            "so he's turning you down.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 300)

    ChrTalk(    #3
        0xFE,
        (
            "#065FS-So he doesn't want to be with\x01",
            "a kid like me, you mean?\x02\x03",

            "Do you think I could get him to\x01",
            "eat some with me when I'm older?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1016FI dunno...\x01",
            "Why don't you ask him yourself?\x02\x03",

            "#1015FBut, a grown-up Tita and Agate...\x02\x03",

            "#1016FWhat a waste on someone like Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#065FHuh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x168A)

    label("loc_34E")

    TalkEnd(0xFE)
    Return()

    # Function_1_AB end

    def Function_2_352(): pass

    label("Function_2_352")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D1, 1)), scpexpr(EXPR_END)), "loc_3A4")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #6
        0xFE,
        (
            "#261FEstelle, hurry and finish work so we\x01",
            "can head back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C2")

    label("loc_3A4")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #7
        0xFE,
        "#260FOh, Estelle. Not finished yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000FI'll be done soon, so would you wait\x01",
            "just a little bit longer?\x02\x03",

            "Once we're done questioning, we'll head\x01",
            "back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "#264FReally?\x02\x03",

            "#265FOkay. I'll go back and wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1001FYeah, let's all get dinner together.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1689)

    label("loc_4C2")

    TalkEnd(0xFE)
    Return()

    # Function_2_352 end

    def Function_3_4C6(): pass

    label("Function_3_4C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_52F")

    ChrTalk(    #11
        0xFE,
        "Do you have some business in the sewers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "You're welcome to go in, but be careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_597")

    ChrTalk(    #13
        0xFE,
        "Do you have some business in the sewers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Since you're a bracer, we'll let you pass.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_625")

    ChrTalk(    #15
        0xFE,
        "Oh, you're bracers, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I've heard about the wanted monsters.\x01",
            "Feel free to go in. Just watch yourselves\x01",
            "in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_625")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69E")

    ChrTalk(    #17
        0xFE,
        "Unfortunately, we can't allow you inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "If your goal is training, please do it\x01",
            "somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_69E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_70D")

    ChrTalk(    #19
        0xFE,
        "Do you have some business in the sewers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I'm sorry, but we can't allow you inside for now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D1")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_7D1")

    ChrTalk(    #21
        0xFE,
        "The sewer's currently off-limits.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Lately we've had a lot more foreign\x01",
            "visitors in the capital, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "We're upping security to make sure\x01",
            "they don't get lost and wander in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D1")

    TalkEnd(0xFE)
    Return()

    # Function_3_4C6 end

    def Function_4_7D5(): pass

    label("Function_4_7D5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_961")

    ChrTalk(    #24
        0xFE,
        "Oh, Zin! Please, go on through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x108,
        (
            "#070FMany thanks.\x02\x03",

            "Given the situation, I bet it's rough\x01",
            "over at the embassy, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Yeah. Ambassador Cochrane's been running around\x01",
            "all over the place trying to get a grasp on the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I was told she'd like to hear the story direct\x01",
            "from you bracers, so I'm to let you through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1000FHuh, all right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AAD")

    label("loc_961")


    ChrTalk(    #29
        0xFE,
        "Please, pass on through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1004FUh, are you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I've been instructed by Ambassador Cochrane\x01",
            "to let you in if you came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1015FHmmm, what's this about?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "It seems she wants to hear from all kinds\x01",
            "of people so she can get a better idea\x01",
            "of the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1000FAh, got'cha. Well, then, if you'll pardon me.\x02",
    )

    CloseMessageWindow()

    label("loc_AAD")

    OP_A2(0x20D9)
    Jump("loc_ACE")

    label("loc_AB3")


    ChrTalk(    #35
        0xFE,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()

    label("loc_ACE")

    Jump("loc_14B0")

    label("loc_AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_DDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B0B")

    ChrTalk(    #36
        0x8,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D28")

    label("loc_B0B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x108, 70570, 0, -7070, 180)
    SetChrPos(0x101, 70550, 0, -5430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B55")
    SetChrPos(0x106, 69580, 0, -4260, 180)
    Jump("loc_B66")

    label("loc_B55")

    SetChrPos(0x103, 69580, 0, -4260, 180)

    label("loc_B66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B87")
    SetChrPos(0xF9, 70970, 0, -4310, 180)
    Jump("loc_B98")

    label("loc_B87")

    SetChrPos(0xF8, 70970, 0, -4310, 180)

    label("loc_B98")

    OP_6D(71710, 0, -7860, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 0, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #37
        0x8,
        "#2PZin, would you like to go into the embassy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x108,
        "#070FYeah, I would.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1000)
    OP_8E(0x8, 0x10CA2, 0xFA, 0xFFFFDCD8, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #39
        0x8,
        "#2PPlease pass through.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71150, 0, -6670, 180)
    SetChrPos(0x1, 71150, 0, -6670, 180)
    SetChrPos(0x2, 71150, 0, -6670, 180)
    SetChrPos(0x3, 71150, 0, -6670, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x3)
    EventEnd(0x0)

    label("loc_D28")

    Jump("loc_DD7")

    label("loc_D2B")


    ChrTalk(    #40
        0xFE,
        (
            "Apparently they caught the remnants of the\x01",
            "Special Ops guys hiding out at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "It's a relief to have one worry out of the way\x01",
            "before the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD7")

    Jump("loc_14B0")

    label("loc_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1099")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E14")

    ChrTalk(    #42
        0x8,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1032")

    label("loc_E14")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x108, 70570, 0, -7070, 180)
    SetChrPos(0x101, 70550, 0, -5430, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E")
    SetChrPos(0x106, 69580, 0, -4260, 180)
    Jump("loc_E6F")

    label("loc_E5E")

    SetChrPos(0x103, 69580, 0, -4260, 180)

    label("loc_E6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E90")
    SetChrPos(0xF9, 70970, 0, -4310, 180)
    Jump("loc_EA1")

    label("loc_E90")

    SetChrPos(0xF8, 70970, 0, -4310, 180)

    label("loc_EA1")

    OP_6D(71710, 0, -7860, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_8C(0x8, 0, 0)
    SetChrSubChip(0x8, 0)
    OP_0D()

    ChrTalk(    #43
        0x8,
        "#2PZin, would you like to go into the embassy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x108,
        "#070FYeah, I would.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x3C)
    Sleep(1000)
    OP_8E(0x8, 0x10CA2, 0xFA, 0xFFFFDCD8, 0xBB8, 0x0)
    OP_8C(0x8, 0, 400)
    Sleep(500)

    ChrTalk(    #45
        0x8,
        "#2PPlease, pass through.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(71150, 0, -6670, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 71150, 0, -6670, 180)
    SetChrPos(0x1, 71150, 0, -6670, 180)
    SetChrPos(0x2, 71150, 0, -6670, 180)
    SetChrPos(0x3, 71150, 0, -6670, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x3)
    EventEnd(0x0)

    label("loc_1032")

    Jump("loc_1096")

    label("loc_1035")


    ChrTalk(    #46
        0xFE,
        "A girl wearing a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I don't remember seeing her,\x01",
            "but I hope she's all right.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1096")

    Jump("loc_14B0")

    label("loc_1099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1138")

    ChrTalk(    #48
        0xFE,
        (
            "A bit ago, Ambassador Cochrane ran into\x01",
            "Ambassador Crainagh of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Those two have chemistry, all right.\x01",
            "EXPLOSIVE chemistry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14B0")

    label("loc_1138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_12B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_120D")

    ChrTalk(    #50
        0xFE,
        "Everyone, did you meet with Ambassador Cochrane?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Ambassador Cochrane's always been kind of\x01",
            "a scary and weird person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Sometimes she refuses to see visitors\x01",
            "and just sends them away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 3)), scpexpr(EXPR_END)), "loc_12B1")

    ChrTalk(    #53
        0xFE,
        "Please, come in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Ah, the embassy grounds are extraterritorial,\x01",
            "just so you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "You should probably refrain\x01",
            "from any suspicious activity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12B5")

    label("loc_12B1")

    Call(0, 11)

    label("loc_12B5")

    Jump("loc_14B0")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_14B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_142D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 4)), scpexpr(EXPR_END)), "loc_1318")

    ChrTalk(    #56
        0x8,
        (
            "I'm sure Ambassador Cochrane will be happy\x01",
            "to see you, Zin.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142A")

    label("loc_1318")


    ChrTalk(    #57
        0x108,
        "#071FHey, buddy, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        "Ohhh? It's Zin!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        "Did you come to visit Liberl again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x108,
        (
            "#070FHaha, more or less.\x02\x03",

            "No doubt there'll be a lot of trouble again,\x01",
            "but it's good to be here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "Haha. I'm sure Ambassador Cochrane will\x01",
            "be happy to see you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x166C)

    label("loc_142A")

    Jump("loc_14B0")

    label("loc_142D")


    ChrTalk(    #62
        0xFE,
        "Oh, hey, this is the Calvardian embassy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Sorry, but unless you have some business\x01",
            "here I'm afraid I can't let you enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B0")

    TalkEnd(0x8)
    Return()

    # Function_4_7D5 end

    def Function_5_14B4(): pass

    label("Function_5_14B4")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_16E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162C")

    ChrTalk(    #64
        0xFE,
        (
            "You guys are...\x01",
            "Ah, please, pass through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1015FOh, Olivier's not with us,\x01",
            "but can we pass anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "Yes, there's no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Given the situation, the ambassador would like\x01",
            "as much information as he can get, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I've been informed that if you bracers came by,\x01",
            "you were to be let through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1000FOh, okay. Well, then...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20D8)
    Jump("loc_16DE")

    label("loc_162C")


    ChrTalk(    #70
        0xFE,
        (
            "Given the situation, the ambassador would like\x01",
            "as much information as he can get, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "I've been informed that if you bracers came by,\x01",
            "you were to be let through.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    Jump("loc_2209")

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B48")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_171B")

    ChrTalk(    #72
        0x9,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1928")

    label("loc_171B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 75550, 0, 69160, 0)
    SetChrPos(0x101, 75460, 0, 67600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1765")
    SetChrPos(0x106, 76600, 0, 66230, 0)
    Jump("loc_1776")

    label("loc_1765")

    SetChrPos(0x103, 76600, 0, 66230, 0)

    label("loc_1776")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1797")
    SetChrPos(0xF9, 75320, 0, 66060, 0)
    Jump("loc_17A8")

    label("loc_1797")

    SetChrPos(0xF8, 75320, 0, 66060, 0)

    label("loc_17A8")

    OP_6D(74500, 0, 71450, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #73
        0x9,
        "#2POlivier, would you like to enter the embassy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x104,
        "#030FWould you mind?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x3C)
    Sleep(1000)
    OP_8C(0x9, 180, 400)
    Sleep(500)

    ChrTalk(    #75
        0x9,
        "#2PPlease, pass through.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(75200, 0, 68360, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 75200, 0, 68360, 0)
    SetChrPos(0x1, 75200, 0, 68360, 0)
    SetChrPos(0x2, 75200, 0, 68360, 0)
    SetChrPos(0x3, 75200, 0, 68360, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x5)
    EventEnd(0x0)

    label("loc_1928")

    Jump("loc_1B45")

    label("loc_192B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_19CC")

    ChrTalk(    #76
        0xFE,
        (
            "Mueller will be on a trip to the Bose\x01",
            "region for a while, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "I guess that means we're letting Olivier\x01",
            "out into the wild again, huh...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B45")

    label("loc_19CC")


    ChrTalk(    #78
        0xFE,
        (
            "Mueller will be on a trip to the Bose\x01",
            "region for a while, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "Apparently he's going to some Royal\x01",
            "Army facility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "I guess this means we'll be letting\x01",
            "Olivier loose upon the world again...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B42")

    ChrTalk(    #81
        0x104,
        (
            "#033FSoldier, you wound me.\x02\x03",

            "#034FYou know not how it pains me to be parted\x01",
            "from my stalwart, bosom companion...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 400)

    ChrTalk(    #82
        0xFE,
        "...Please stop lying.\x02",
    )

    CloseMessageWindow()

    label("loc_1B42")

    OP_A2(0x4)

    label("loc_1B45")

    Jump("loc_2209")

    label("loc_1B48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1C2F")

    ChrTalk(    #83
        0xFE,
        (
            "Oh, hello...\x01",
            "Do you have some business with Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "If you're looking for Olivier, he left with\x01",
            "Mueller a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "You wouldn't know it from the way they act,\x01",
            "but those two actually get along pretty well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2209")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CB2")

    ChrTalk(    #86
        0xFE,
        (
            "Ah, how did your meeting with the\x01",
            "ambassador go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "I hope that you were able to get done what\x01",
            "you needed to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2209")

    label("loc_1CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1DBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 7)), scpexpr(EXPR_END)), "loc_1D2F")

    ChrTalk(    #88
        0xFE,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Remember that the embassy grounds are\x01",
            "extraterritorial, so mind yourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1D3D")
    Call(0, 13)
    Jump("loc_1DBB")

    label("loc_1D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 6)), scpexpr(EXPR_END)), "loc_1DB7")

    ChrTalk(    #90
        0xFE,
        (
            "Ambassador Crainagh and Major Vander\x01",
            "haven't returned yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "I don't think they'll be that late, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1DBB")

    label("loc_1DB7")

    Call(0, 12)

    label("loc_1DBB")

    Jump("loc_2209")

    label("loc_1DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2209")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2107")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 5)), scpexpr(EXPR_END)), "loc_1E7B")
    TurnDirection(0x9, 0x104, 0)

    ChrTalk(    #92
        0x9,
        (
            "Olivier, please stop leaving without\x01",
            "a word all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "Your latest disappearing act has really gotten\x01",
            "Ambassador Crainagh all worked up. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2104")

    label("loc_1E7B")

    TurnDirection(0x9, 0x104, 0)

    ChrTalk(    #94
        0x104,
        "#031F#6PHello, good soldier. Have you been well?\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #95
        0x9,
        "#5PO-Olivier?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        "#5PWhere the heck have you been?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x104,
        "#033F#6POh, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        "#5PEr, nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "#5PYou've been hiding from us ever since you\x01",
            "went to Elmo for a 'little break,' haven't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        "#5PMueller was livid.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x104,
        "#035F#6PHeh... As always, a very cute man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1007F#6PWait, Olivier...\x02\x03",

            "#1019FYou haven't been keeping quiet to the embassy\x01",
            "about working with us, have you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x104,
        (
            "#031F#6PHa. Ha. Ha.\x02\x03",

            "Roads wandered in search of love are roads\x01",
            "to travel in secret, but of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1007F#6PThe heck is that supposed to mean...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x166D)

    label("loc_2104")

    Jump("loc_2209")

    label("loc_2107")


    ChrTalk(    #105
        0xFE,
        (
            "Beyond this point is the Erebonian embassy.\x01",
            "No one may enter except those with official\x01",
            "business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I've been told to keep security very tight now,\x01",
            "especially with the signing ceremony approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "I'm sorry, but we hope for your understanding.\x02",
    )

    CloseMessageWindow()

    label("loc_2209")

    TalkEnd(0x9)
    Return()

    # Function_5_14B4 end

    def Function_6_220D(): pass

    label("Function_6_220D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22E5")

    ChrTalk(    #108
        0xFE,
        (
            "With orbments unusable, even our gorgeous\x01",
            "capital is pitch black at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Seems like the queen is looking into the\x01",
            "situation, but I wonder if she'll really\x01",
            "find a way to make them work again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2539")

    label("loc_22E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_23B0")

    ChrTalk(    #110
        0xFE,
        "That stuff at the harbor was terrible, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "The culprit, Kanone... She's that woman who\x01",
            "was always stuck to Colonel Richard, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "She always did have a sneaky face, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2539")

    label("loc_23B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2414")

    ChrTalk(    #113
        0xFE,
        "What, you looking for someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "A girl in a white dress... Nope.\x01",
            "Didn't see her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2539")

    label("loc_2414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2467")

    ChrTalk(    #115
        0xFE,
        (
            "The crows are crying, so that means it's\x01",
            "time to goooo home. ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2539")

    label("loc_2467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_24C5")

    ChrTalk(    #116
        0xFE,
        (
            "I'm kinda bored, so maybe I'll go to the\x01",
            "Edel Department Store on my way back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2539")

    label("loc_24C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2539")

    ChrTalk(    #117
        0xFE,
        "Heya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Apparently the Grand Arena's closed\x01",
            "since they don't have any shows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "A little sad, huh.\x02",
    )

    CloseMessageWindow()

    label("loc_2539")

    TalkEnd(0xFE)
    Return()

    # Function_6_220D end

    def Function_7_253D(): pass

    label("Function_7_253D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2611")

    ChrTalk(    #120
        0xFE,
        (
            "I thought the orbal shutdown problem was just\x01",
            "in the capital, but it seems like it's affecting\x01",
            "other regions too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "If orbments remain unusable forever,\x01",
            "what's gonna happen to this country?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_2611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_26F0")

    ChrTalk(    #122
        0xFE,
        (
            "It's true that lately there's not been much\x01",
            "to talk about, and that was sad, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "I wish they'd spare us stuff like last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I want some, really, really BIG topic\x01",
            "that'll get everyone talking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_26F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(    #125
        0xFE,
        "Lately there hasn't been much to talk about.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Isn't there, like, something that'd\x01",
            "be a real shock to everyone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_2772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2809")

    ChrTalk(    #127
        0xFE,
        (
            "The evenings are lovely, but don't\x01",
            "they make you a little lonely?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I found myself shedding some tears\x01",
            "as I watched the sun set.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_2809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2890")

    ChrTalk(    #129
        0xFE,
        (
            "Oh, are you the bracers who won\x01",
            "the Martial Arts Competition?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Ahhh, I'm so lucky to meet you in a place\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29B9")

    label("loc_2890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_29B9")

    ChrTalk(    #131
        0xFE,
        (
            "When I visited Grancel to see the Martial Arts\x01",
            "Competition, I really came to like the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I even moved here because I liked it so much!\x01",
            "It really is an interesting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Next year I'll totally be able to catch the\x01",
            "Martial Arts Competition and the Birthday\x01",
            "Celebration.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B9")

    TalkEnd(0xFE)
    Return()

    # Function_7_253D end

    def Function_8_29BD(): pass

    label("Function_8_29BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A82")

    ChrTalk(    #134
        0xFE,
        (
            "Liberl is a country that developed as much as\x01",
            "it has thanks to orbments, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "If orbments remain unusable like this, things\x01",
            "will surely become more than just 'inconvenient.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE9")

    label("loc_2A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2B2A")

    ChrTalk(    #136
        0xFE,
        (
            "It seems like the Intelligence Division did\x01",
            "something crazy again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I'm just extremely relieved that there were\x01",
            "no fatalities amongst the citizenry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE9")

    label("loc_2B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2BEC")

    ChrTalk(    #138
        0xFE,
        (
            "It's such lovely weather I thought\x01",
            "I'd head to the villa, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "It seems the Royal Army is using it as\x01",
            "security headquarters at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "Well, guess it makes sense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DE9")

    label("loc_2BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C7F")

    ChrTalk(    #141
        0xFE,
        (
            "With that signing ceremony or whatever\x01",
            "close they seem pretty busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Seems like it's hard being a\x01",
            "government official, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE9")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2D83")

    ChrTalk(    #143
        0xFE,
        (
            "With disasters and incidents one after the other,\x01",
            "it seems like the capital's only just now calmed\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "...Is what I thought, but next up is the\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Well, if this'll make things peaceful,\x01",
            "it's more than welcome, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE9")

    label("loc_2D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2DE9")

    ChrTalk(    #146
        0xFE,
        "Ahh, so sleepy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Maybe I should go get a pick-me-up\x01",
            "at the West Block coffee house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE9")

    TalkEnd(0xFE)
    Return()

    # Function_8_29BD end

    def Function_9_2DED(): pass

    label("Function_9_2DED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2E56")

    ChrTalk(    #148
        0xFE,
        "More like, seriously, gimme a break.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "Don't you think this lifestyle is SO tragic?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FE4")

    label("loc_2E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2EA3")

    ChrTalk(    #150
        0xFE,
        (
            "Seems like that suuuper lame duke's\x01",
            "come back to the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE4")

    label("loc_2EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2F18")

    ChrTalk(    #151
        0xFE,
        "More like, what IS a ghost?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "...What, seriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "Come ON, no way something like that exists!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FE4")

    label("loc_2F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F53")

    ChrTalk(    #154
        0xFE,
        "More like, what are we gonna eat today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FE4")

    label("loc_2F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2F89")

    ChrTalk(    #155
        0xFE,
        "More like, what are we gonna do today?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FE4")

    label("loc_2F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2FE4")

    ChrTalk(    #156
        0xFE,
        "More like, what's a signing ceremony?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "Does it got anything to do with us?\x02",
    )

    CloseMessageWindow()

    label("loc_2FE4")

    TalkEnd(0xFE)
    Return()

    # Function_9_2DED end

    def Function_10_2FE8(): pass

    label("Function_10_2FE8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3062")

    ChrTalk(    #158
        0xFE,
        (
            "That thing that appeared at the lake\x01",
            "is SUPER suspicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "I mean, doesn't it just LOOK suspicious?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3237")

    label("loc_3062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_30C6")

    ChrTalk(    #160
        0xFE,
        "What, seriously? But, you know that duke...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "Don't you think he's a little cute?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3237")

    label("loc_30C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3134")

    ChrTalk(    #162
        0xFE,
        "Like, it really happened at Ruan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "Why don't you believe me?\x01",
            "Seriously, that ticks me off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3237")

    label("loc_3134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31A7")

    ChrTalk(    #164
        0xFE,
        "Wanna go to the cafe in the West Block?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "The curry there is so good it's suuuper\x01",
            "dangerous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3237")

    label("loc_31A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_31DF")

    ChrTalk(    #166
        0xFE,
        "Anyway, why don't we get some ice cream?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3237")

    label("loc_31DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3237")

    ChrTalk(    #167
        0xFE,
        (
            "Basically, you know, it's like that.\x01",
            "Like, 'let's all get along,' you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3237")

    TalkEnd(0xFE)
    Return()

    # Function_10_2FE8 end

    def Function_11_323B(): pass

    label("Function_11_323B")

    OP_EA(0x1, 0xC, 0x0, 0x0)
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_32B2")

    ChrTalk(    #168
        0xFE,
        (
            "A broken heart bathed in the golden\x01",
            "glow of dusk... The remnants of the\x01",
            "dreams of the strong...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_32B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3398")

    ChrTalk(    #169
        0xFE,
        (
            "I feel a lot better after baring my soul in\x01",
            "a fevered chase of the sunset.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "All right, no point just lying around here.\x01",
            "Heh. That won't get anything done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "Yeah, it's time to set off on a journey\x01",
            "somewhere!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3477")

    ChrTalk(    #172
        0xFE,
        (
            "The evening sun, dyeing the white\x01",
            "clouds such a brilliant scarlet color...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "And, me. Such a small piece in the\x01",
            "grand scheme of things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Hey, Ricky...\x01",
            "I, who am so insignificant, what should I do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3506")

    ChrTalk(    #175
        0xFE,
        (
            "You sure seem to be yawning an awful lot\x01",
            "while I'm trying to pour my heart out to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "If you're a friend, suffer with me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3662")

    label("loc_3506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3662")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FA")

    ChrTalk(    #177
        0xFE,
        "*sigh* In the end, everything is as it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "Today, too, I'm pondering.\x01",
            "Soooo much pondering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "I'm sure I will spend tomorrow pondering as well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "No job, no girlfriend...\x01",
            "I wonder if my life has a purpose.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3662")

    label("loc_35FA")


    ChrTalk(    #181
        0xFE,
        "*sigh* Today, too, I'm pondering.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "No job, no girlfriend...\x01",
            "I wonder if my life has a purpose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3662")

    TalkEnd(0xFE)
    Return()

    # Function_11_323B end

    def Function_12_3666(): pass

    label("Function_12_3666")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_36F6")

    ChrTalk(    #183
        0xFE,
        (
            "Apparently Anton's heart was 'shattered' once\x01",
            "again in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Seems like he intends to be a dramatist\x01",
            "or something now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DE")

    label("loc_36F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_379B")

    ChrTalk(    #185
        0xFE,
        "I'd say 'dramatic' fits Anton perfectly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "Go with what you know, as they say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "Well, that's not quite it, but I think it\x01",
            "suits him just fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DE")

    label("loc_379B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3854")

    ChrTalk(    #188
        0xFE,
        (
            "...Why don't you try running\x01",
            "after the evening sun?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "Not sure how much it'll accomplish, but you\x01",
            "might find yourself feeling better just from\x01",
            "the flow of things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38DE")

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3886")

    ChrTalk(    #190
        0xFE,
        "*yaaawn* Good weather today again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38DE")

    label("loc_3886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_38DE")

    ChrTalk(    #191
        0xFE,
        "Haha, look, Anton.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "That cloud...\x01",
            "It looks like Duke Dunan's hairstyle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DE")

    TalkEnd(0xFE)
    Return()

    # Function_12_3666 end

    def Function_13_38E2(): pass

    label("Function_13_38E2")

    TalkBegin(0x11)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38FF")
    OP_A9(0xCE)
    TalkEnd(0x11)
    Return()

    label("loc_38FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3910")
    TalkEnd(0x11)
    Return()

    label("loc_3910")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_39D5")

    ChrTalk(    #193
        0xFE,
        (
            "The Grancel Castle kitchen is making our\x01",
            "ice cream!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "The queen said she wanted to make\x01",
            "sure everyone could try it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "I was shocked to hear the queen\x01",
            "had eaten my ice cream.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F81")

    label("loc_39D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3AA5")

    ChrTalk(    #196
        0xFE,
        (
            "Last night it seems something really\x01",
            "crazy happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "All my customers have been talking\x01",
            "about the harbor incident non-stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "Thanks to that, I've become pretty\x01",
            "familiar with the case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F81")

    label("loc_3AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3C22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 4)), scpexpr(EXPR_END)), "loc_3B83")

    ChrTalk(    #199
        0xFE,
        (
            "If you're looking for the girl in the white dress,\x01",
            "isn't she gonna be at the landing port?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "She said, 'I'm going to meet up with my\x01",
            "friends at the landing port,' at least, and\x01",
            "really happily too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C1F")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 3)), scpexpr(EXPR_END)), "loc_3B91")
    Call(0, 24)
    Jump("loc_3C1F")

    label("loc_3B91")


    ChrTalk(    #201
        0xFE,
        (
            "It's nice to have a mag like the\x01",
            "Liberl News talk about us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "What makes me happiest is to see\x01",
            "kids happy eating my ice cream.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C1F")

    Jump("loc_3F81")

    label("loc_3C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C76")

    ChrTalk(    #203
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "How about some ice cream as\x01",
            "a treat after dinner? \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F81")

    label("loc_3C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3CBD")

    ChrTalk(    #205
        0xFE,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "How about some cold, delicious ice cream?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F81")

    label("loc_3CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3F81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB7")

    ChrTalk(    #207
        0xFE,
        (
            "I know people say I'm 'the purveyor of ice\x01",
            "cream to the royal family,' but that's just\x01",
            "a dumb rumor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "Though, if Lady Klaudia ate my ice cream,\x01",
            "I'd be happy to hear that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3EB1")
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #209
        0x101,
        "#1000F(...Kloe, have you had the ice cream here?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x105,
        (
            "#040F(...Ahem!)\x02\x03",

            "(Actually, it was Grandmother's suggestion.)\x02\x03",

            "(I was really happy to get to try it.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x11, 400)

    ChrTalk(    #211
        0x101,
        (
            "#1001FMiss, you're good to go. You can, in fact, proudly\x01",
            "say you're purveyor to the royal family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "Huh?\x02",
    )

    CloseMessageWindow()

    label("loc_3EB1")

    OP_A2(0x1)
    Jump("loc_3F81")

    label("loc_3EB7")


    ChrTalk(    #213
        0xFE,
        (
            "I know people say I'm 'the purveyor of ice\x01",
            "cream to the royal family,' but that's just\x01",
            "a dumb rumor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "Of course, if Lady Klaudia really DID eat my\x01",
            "ice cream, I'd be happy to hear that, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F81")

    TalkEnd(0x11)
    Return()

    # Function_13_38E2 end

    def Function_14_3F85(): pass

    label("Function_14_3F85")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4003")

    ChrTalk(    #215
        0xFE,
        "The Linde is still stuck in Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "I was so worried about my child,\x01",
            "that I came back to the capital. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_4003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4055")

    ChrTalk(    #217
        0xFE,
        "I'm sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "Want to go get some ice cream over\x01",
            "there together?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40D8")

    label("loc_4055")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_40D8")

    ChrTalk(    #219
        0xFE,
        (
            "I try to meet up with my son whenever\x01",
            "I can between flights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "I know that I'm making this kid\x01",
            "put up with a lot...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40D8")

    TalkEnd(0xFE)
    Return()

    # Function_14_3F85 end

    def Function_15_40DC(): pass

    label("Function_15_40DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_41AD")

    ChrTalk(    #221
        0xFE,
        "The rooms are so dark and cold...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "It's really scary, but I'm doin' my best\x01",
            "to be brave just like Mama said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "Don't tell anyone, but I was so relieved\x01",
            "when I saw Mama's face I cried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_41AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_421E")

    ChrTalk(    #224
        0xFE,
        (
            "Ehe, I did good and watched over the\x01",
            "house while you were gone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "I wasn't lonely or anything!\x02",
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_421E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4284")

    ChrTalk(    #226
        0xFE,
        (
            "Yup, yup. I know Mama's tryin' real hard\x01",
            "with her job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "I'm Mama's son, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_4284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42D5")

    ChrTalk(    #228
        0xFE,
        "Mama... *sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "I wanna play with you again soon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_42D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4318")

    ChrTalk(    #230
        0xFE,
        "Yaaay, Mama's back from her job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "Jealous, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_436C")

    label("loc_4318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_436C")

    ChrTalk(    #232
        0xFE,
        "Isn't Mama gonna come home soon...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "I'll do my best to wait, so...\x02",
    )

    CloseMessageWindow()

    label("loc_436C")

    TalkEnd(0xFE)
    Return()

    # Function_15_40DC end

    def Function_16_4370(): pass

    label("Function_16_4370")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_444D")

    ChrTalk(    #234
        0xFE,
        (
            "In international society, Liberl's superiority\x01",
            "is maintained by our orbal technology.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "The non-aggression pact is a sign of that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "If this situation continues, even the\x01",
            "queen won't be able to...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47DA")

    label("loc_444D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_452A")

    ChrTalk(    #237
        0xFE,
        (
            "So the Intelligence Division caused\x01",
            "an incident like that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "I suppose it could be considered more fruits\x01",
            "of Colonel Richard's treason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "One way or another, a military\x01",
            "solution isn't a good one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47DA")

    label("loc_452A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_45D5")

    ChrTalk(    #240
        0xFE,
        (
            "Mayors from each region will be coming for\x01",
            "the day of the signing ceremony, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "I suppose Ruan's new mayor will be\x01",
            "attending...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "I wonder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_47DA")

    label("loc_45D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46B3")

    ChrTalk(    #243
        0xFE,
        (
            "It will surely take time for the Royal Army to\x01",
            "recover from the damage the coup d'etat\x01",
            "caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "However, we have Captain Schwarz, Colonel Cid,\x01",
            "and General Cassius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "I'm sure Liberl will be fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_47DA")

    label("loc_46B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4738")

    ChrTalk(    #246
        0xFE,
        (
            "I'm amazed the Empire agreed to sign\x01",
            "the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "Ho ho, I wonder what kind of magic\x01",
            "our queen used.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47DA")

    label("loc_4738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_47DA")

    ChrTalk(    #248
        0xFE,
        (
            "Miss Schwarz of the Royal Guard was recently\x01",
            "promoted to captain, I understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Ho ho. Considering her ability and successes,\x01",
            "it's only natural.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47DA")

    TalkEnd(0xFE)
    Return()

    # Function_16_4370 end

    def Function_17_47DE(): pass

    label("Function_17_47DE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4875")

    ChrTalk(    #250
        0xFE,
        (
            "*sigh* Nights sure are long when you can't\x01",
            "use orbments. I'm so anxious I can't sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "It's so depressing to see the sun set...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BAB")

    label("loc_4875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_494F")

    ChrTalk(    #252
        0xFE,
        (
            "I've thought long and hard about it,\x01",
            "and you know what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "I need to cultivate my inner beauty\x01",
            "to meet a wonderful man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "Wouldn't it be wonderful if we could\x01",
            "both bring out the best of each other?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BAB")

    label("loc_494F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4A1E")

    ChrTalk(    #255
        0xFE,
        (
            "Life can change a lot depending on who\x01",
            "you tie yourself to for it, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "I think it's important to have a good eye\x01",
            "for men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "First, it's important to check their shoes\x01",
            "and watch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BAB")

    label("loc_4A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9C")

    ChrTalk(    #258
        0xFE,
        (
            "This lady I'd never met asked\x01",
            "me if I'd marry her son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "I can't really marry someone I've never met...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BAB")

    label("loc_4A9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4B1A")

    ChrTalk(    #260
        0xFE,
        (
            "This weird old lady's been\x01",
            "eyeing me for a while now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "I wonder why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "Is there something on my face?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4BAB")

    label("loc_4B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4BAB")

    ChrTalk(    #263
        0xFE,
        (
            "A while back, I was being followed around by\x01",
            "a man on the stairs in front of the department\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "That was creepy and scary...\x02",
    )

    CloseMessageWindow()

    label("loc_4BAB")

    TalkEnd(0xFE)
    Return()

    # Function_17_47DE end

    def Function_18_4BAF(): pass

    label("Function_18_4BAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4C7F")

    ChrTalk(    #265
        0xFE,
        (
            "To youths nowadays, orbments not working is\x01",
            "a source of terrible anxiety, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "Of course, it sure does make it hard\x01",
            "to boil water.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "Guess I've gotten complacent too.\x01",
            "Ho ho ho.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F14")

    label("loc_4C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4D18")

    ChrTalk(    #268
        0xFE,
        (
            "It seems like the Royal Guard and some\x01",
            "bracers solved last night's case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "If the army and guild cooperate,\x01",
            "we've got nothing to fear.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F14")

    label("loc_4D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_4D90")

    ChrTalk(    #270
        0xFE,
        (
            "I know it's their job, but I'm sure it must\x01",
            "be hard on the soldiers providing security\x01",
            "for these events.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F14")

    label("loc_4D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DD8")

    ChrTalk(    #271
        0xFE,
        (
            "Oh, my, the sun's setting a bit earlier,\x01",
            "isn't it...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F14")

    label("loc_4DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_4E77")

    ChrTalk(    #272
        0xFE,
        "I haven't seen Kurt of the Bracer Guild lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "I wonder if he's off in some other region...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "Kurt is very popular for his politeness.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F14")

    label("loc_4E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_4F14")
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #275
        0xFE,
        "Oh, that symbol on your chest...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "Miss... You're a bracer, aren't you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "Good work with your job. And\x01",
            "very impressive at your age.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F14")

    TalkEnd(0xFE)
    Return()

    # Function_18_4BAF end

    def Function_19_4F18(): pass

    label("Function_19_4F18")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_525F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5178")

    ChrTalk(    #278
        0xFE,
        "The History Museum... Yeah, this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        "#1011FOh, Jimmy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "Whoa? Hey, you're the bracers\x01",
            "who saved me at Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x101,
        (
            "#1000FWhat are you doing here?\x02\x03",

            "#1004FAh, right... Delivering that artifact, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Yeah, it may have lost its power, but\x01",
            "who knows what it might do, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "I'll entrust it to these guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x101,
        (
            "#1001FGood call.\x02\x03",

            "If you'd also give up on treasure hunting and\x01",
            "get a real job, that'd be even better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "Ouch... But, I'm afraid I can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "I suppose it'd be different if I could find\x01",
            "something even more romantic than being\x01",
            "a treasure hunter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5259")

    label("loc_5178")


    ChrTalk(    #287
        0xFE,
        (
            "The History Museum...\x01",
            "Whoa, yeah, this is it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "I'm sure I can leave an artifact here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "Actually, I found a defunct artifact while\x01",
            "I was in Zeiss...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "I figured I'd get the History Museum to take\x01",
            "a look at it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5259")

    OP_A2(0x1649)
    Jump("loc_52D4")

    label("loc_525F")


    ChrTalk(    #291
        0xFE,
        (
            "I plan on getting them to have a look at\x01",
            "my little discovery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "First I need to find the person in charge...\x02",
    )

    CloseMessageWindow()

    label("loc_52D4")

    TalkEnd(0xFE)
    Return()

    # Function_19_4F18 end

    def Function_20_52D8(): pass

    label("Function_20_52D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_531D")

    ChrTalk(    #293
        0xFE,
        (
            "Professor Russell in Zeiss might know\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53CC")

    label("loc_531D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_53A2")

    ChrTalk(    #294
        0xFE,
        (
            "There's no way we can deal with\x01",
            "a giant archaism like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "If it attacked next time,\x01",
            "we wouldn't last a moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53CC")

    label("loc_53A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_53CC")

    ChrTalk(    #296
        0xFE,
        "Oh, looking for a lost child?\x02",
    )

    CloseMessageWindow()

    label("loc_53CC")

    TalkEnd(0xFE)
    Return()

    # Function_20_52D8 end

    def Function_21_53D0(): pass

    label("Function_21_53D0")

    TalkBegin(0xFE)
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5453")

    ChrTalk(    #297
        0xFE,
        (
            "The Royal Army is still maintaining\x01",
            "heightened security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "I'll do my best too in case the worst happens.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5543")

    label("loc_5453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_54D5")

    ChrTalk(    #299
        0xFE,
        (
            "I heard a rumor that the one behind all that\x01",
            "mess was a tiny kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "There's no way that could be true, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5543")

    label("loc_54D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5543")

    ChrTalk(    #301
        0xFE,
        (
            "There are a lot of critical facilities in the East\x01",
            "Block, so we need to keep security tight here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5543")

    OP_4B(0xFE, 255)
    TalkEnd(0xFE)
    Return()

    # Function_21_53D0 end

    def Function_22_554B(): pass

    label("Function_22_554B")

    TalkBegin(0xFE)
    OP_4A(0xFE, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_55BA")

    ChrTalk(    #302
        0xFE,
        (
            "General Cassius and Colonel Cid\x01",
            "are in the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        "Just thinking that calms me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5677")

    label("loc_55BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_564A")

    ChrTalk(    #304
        0xFE,
        (
            "I was shocked at yesterday's incident,\x01",
            "but Julia returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        (
            "Seems like Colonel Cid called her back,\x01",
            "but what perfect timing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5677")

    label("loc_564A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5677")

    ChrTalk(    #306
        0xFE,
        "For now, everything's all clear.\x02",
    )

    CloseMessageWindow()

    label("loc_5677")

    OP_4B(0xFE, 255)
    TalkEnd(0xFE)
    Return()

    # Function_22_554B end

    def Function_23_567F(): pass

    label("Function_23_567F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_568C")
    Jump("loc_5827")

    label("loc_568C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_56DF")

    ChrTalk(    #307
        0xFE,
        (
            "Please, just yesterday wasn't enough\x01",
            "time to get a real look at it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_56DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5760")

    ChrTalk(    #308
        0xFE,
        (
            "I've come all this way! I'd like\x01",
            "to see the academic facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "Cultural education is important for people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_5760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57AE")

    ChrTalk(    #310
        0xFE,
        (
            "...All these unexpected expenses are giving\x01",
            "me a headache.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_57AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_57F9")

    ChrTalk(    #311
        0xFE,
        (
            "I didn't think it was the off season\x01",
            "for the Grand Arena...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5827")

    label("loc_57F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5827")

    ChrTalk(    #312
        0xFE,
        "Oh, so this is the Grand Arena...\x02",
    )

    CloseMessageWindow()

    label("loc_5827")

    TalkEnd(0xFE)
    Return()

    # Function_23_567F end

    def Function_24_582B(): pass

    label("Function_24_582B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5838")
    Jump("loc_59D7")

    label("loc_5838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_58C6")

    ChrTalk(    #313
        0xFE,
        (
            "Apparently this guy is determined to visit\x01",
            "the History Museum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "Since we're on vacation I want to go\x01",
            "somewhere else today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59D7")

    label("loc_58C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_593B")

    ChrTalk(    #315
        0xFE,
        "The History Museum... Huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "It doesn't sound that fun, to be honest.\x01",
            "I want to do something else.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59D7")

    label("loc_593B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5970")

    ChrTalk(    #317
        0xFE,
        "Haha, that was some fun shopping.\x02",
    )

    CloseMessageWindow()
    Jump("loc_59D7")

    label("loc_5970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_59AC")

    ChrTalk(    #318
        0xFE,
        "*sigh* Really, this guy doesn't plan enough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_59D7")

    label("loc_59AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_59D7")

    ChrTalk(    #319
        0xFE,
        "Er.... Are these doors closed?\x02",
    )

    CloseMessageWindow()

    label("loc_59D7")

    TalkEnd(0xFE)
    Return()

    # Function_24_582B end

    def Function_25_59DB(): pass

    label("Function_25_59DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_59E8")
    Jump("loc_5C19")

    label("loc_59E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5A5D")

    ChrTalk(    #320
        0xFE,
        (
            "The Empire's got a sense of danger around it,\x01",
            "but that's charming too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        "I'd love to go someday.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C19")

    label("loc_5A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5AA1")

    ChrTalk(    #322
        0xFE,
        (
            "...A girl in a white dress?\x01",
            "Sorry, haven't seen her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C19")

    label("loc_5AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B21")

    ChrTalk(    #323
        0xFE,
        (
            "You were talking to that black-haired\x01",
            "Imperial soldier, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "Mmmm, yes... I'm a big fan of his.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C19")

    label("loc_5B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5BA9")

    ChrTalk(    #325
        0xFE,
        (
            "A black-haired soldier came out\x01",
            "of the embassy just a bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "His expression was impassive,\x01",
            "but he was so cool. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C19")

    label("loc_5BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5C19")

    ChrTalk(    #327
        0xFE,
        (
            "The Imperial crest's got some real\x01",
            "power behind it now that I've had the\x01",
            "chance to see it up close.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C19")

    TalkEnd(0xFE)
    Return()

    # Function_25_59DB end

    def Function_26_5C1D(): pass

    label("Function_26_5C1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5C2A")
    Jump("loc_5E1C")

    label("loc_5C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5C5D")

    ChrTalk(    #328
        0xFE,
        "Now, which way is the landing port?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E1C")

    label("loc_5C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5C8F")

    ChrTalk(    #329
        0xFE,
        "What should I see today, I wonder.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5E1C")

    label("loc_5C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D1B")

    ChrTalk(    #330
        0xFE,
        (
            "Mmm, what a nice sightseeing trip\x01",
            "I've had here in the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "Perhaps it's about time I head back\x01",
            "to the hotel.  \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1C")

    label("loc_5D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5DD3")

    ChrTalk(    #332
        0xFE,
        (
            "Err, this is the East Block in front\x01",
            "of the Calvardian embassy, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        (
            "This city is so big that it's easy to get lost,\x01",
            "so I picked up a map at the department store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E1C")

    label("loc_5DD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5E1C")

    ChrTalk(    #334
        0xFE,
        (
            "This is my first time in the capital,\x01",
            "but what a large city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E1C")

    TalkEnd(0xFE)
    Return()

    # Function_26_5C1D end

    def Function_27_5E20(): pass

    label("Function_27_5E20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5E2D")
    Jump("loc_5FCB")

    label("loc_5E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5E81")

    ChrTalk(    #335
        0xFE,
        (
            "Seems like some kind of incident happened.\x01",
            "I wonder what, exactly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCB")

    label("loc_5E81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5ED9")

    ChrTalk(    #336
        0xFE,
        "Have I seen a girl?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "Yeah, actually. I did.\x01",
            "She passed through here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCB")

    label("loc_5ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F0A")

    ChrTalk(    #338
        0xFE,
        "Ahh, what a lovely evening...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FCB")

    label("loc_5F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5F98")

    ChrTalk(    #339
        0xFE,
        (
            "Just visiting the tourist spots doesn't\x01",
            "make a trip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        (
            "Spending time without any plan like\x01",
            "this is also a wonderful memory.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FCB")

    label("loc_5F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5FCB")

    ChrTalk(    #341
        0xFE,
        "Haha, this is quite the secret spot...\x02",
    )

    CloseMessageWindow()

    label("loc_5FCB")

    TalkEnd(0xFE)
    Return()

    # Function_27_5E20 end

    def Function_28_5FCF(): pass

    label("Function_28_5FCF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5FDC")
    Jump("loc_6225")

    label("loc_5FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_6058")

    ChrTalk(    #342
        0xFE,
        "Today's finally the last day of this fun trip.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        (
            "From tomorrow on it's back to work as a\x01",
            "housewife again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6225")

    label("loc_6058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_60C0")

    ChrTalk(    #344
        0xFE,
        (
            "A girl in a white dress?\x01",
            "I think I saw her a bit ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        "It was right around here...\x02",
    )

    CloseMessageWindow()
    Jump("loc_6225")

    label("loc_60C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6163")

    ChrTalk(    #346
        0xFE,
        (
            "When you're out shopping while traveling,\x01",
            "your purse strings get so loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        (
            "I've already used up what I'd planned\x01",
            "on spending on souvenirs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6225")

    label("loc_6163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_61DF")

    ChrTalk(    #348
        0xFE,
        "That ice cream was delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        (
            "Now, then, perhaps it's time to do some\x01",
            "shopping at the department store.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6225")

    label("loc_61DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_6225")

    ChrTalk(    #350
        0xFE,
        (
            "I'd heard there was a good ice\x01",
            "cream stand around here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6225")

    TalkEnd(0xFE)
    Return()

    # Function_28_5FCF end

    def Function_29_6229(): pass

    label("Function_29_6229")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_D2(0x700E1, 0x700E5, 0x0)
    OP_D2(0x7030A, 0x70311, 0x1)
    OP_D2(0x7030B, 0x70312, 0x2)
    OP_D2(0x7030C, 0x70313, 0x3)
    OP_D2(0x7013B, 0x7013F, 0x4)
    OP_D2(0x70530, 0x70538, 0x5)
    OP_D2(0x70531, 0x70539, 0x6)
    OP_D2(0x70532, 0x7053A, 0x7)
    OP_D2(0x2700C0, 0x2700C4, 0x8)
    OP_D2(0x7014A, 0x7014E, 0x9)
    OP_D2(0x6007B, 0x60080, 0xA)
    OP_D2(0x6007C, 0x60081, 0xB)
    OP_D2(0x290142, 0x290146, 0xC)
    OP_D2(0x29014C, 0x290150, 0xD)
    OP_D2(0x26000E, 0x260013, 0xE)
    OP_D2(0x270312, 0x27031C, 0xF)
    OP_D2(0x270315, 0x27031F, 0x10)
    OP_D2(0x270316, 0x270320, 0x11)
    OP_D2(0x70310, 0x70317, 0x12)
    OP_D3(0x13)
    OP_D2(0x60053, 0x60058, 0x13)
    OP_D3(0x14)
    OP_D2(0x290143, 0x290147, 0x14)
    OP_D2(0x290144, 0x290148, 0x15)
    OP_D2(0x29014A, 0x29014B, 0x16)
    OP_D2(0x70540, 0x70541, 0x17)
    OP_D2(0x29014D, 0x290151, 0x18)
    OP_D2(0x29014F, 0x290153, 0x19)
    OP_D2(0x29014E, 0x290152, 0x1A)
    OP_D2(0x7030F, 0x70316, 0x1B)
    OP_D2(0x70310, 0x70317, 0x1C)
    OP_D2(0x270313, 0x27031D, 0x1D)
    OP_D2(0x270314, 0x27031E, 0x1E)
    OP_D2(0x270318, 0x270322, 0x1F)
    OP_D2(0x26000D, 0x260012, 0x20)
    OP_D2(0x270326, 0x270330, 0x21)
    OP_D2(0x27032A, 0x270334, 0x22)
    OP_D2(0x270327, 0x270331, 0x23)
    OP_D2(0x270328, 0x270332, 0x24)
    OP_D2(0x27032C, 0x270336, 0x25)
    SetChrChipByIndex(0x28, 8)
    SetChrChipByIndex(0x29, 2)
    SetChrChipByIndex(0x2A, 2)
    SetChrChipByIndex(0x2B, 2)
    SetChrChipByIndex(0x2C, 2)
    SetChrChipByIndex(0x2D, 2)
    SetChrChipByIndex(0x2E, 2)
    SetChrChipByIndex(0x2F, 2)
    SetChrChipByIndex(0x30, 2)
    SetChrChipByIndex(0x31, 6)
    SetChrChipByIndex(0x32, 6)
    SetChrChipByIndex(0x33, 6)
    SetChrChipByIndex(0x34, 6)
    SetChrChipByIndex(0x35, 6)
    SetChrChipByIndex(0x36, 6)
    SetChrChipByIndex(0x37, 6)
    SetChrChipByIndex(0x38, 6)
    SetChrChipByIndex(0x49, 19)
    SetChrChipByIndex(0x4A, 19)
    SetChrChipByIndex(0x4B, 19)
    SetChrChipByIndex(0x4C, 19)
    SetChrSubChip(0x28, 0)
    SetChrSubChip(0x29, 0)
    SetChrSubChip(0x2A, 0)
    SetChrSubChip(0x2B, 0)
    SetChrSubChip(0x2C, 0)
    SetChrSubChip(0x2D, 0)
    SetChrSubChip(0x2E, 0)
    SetChrSubChip(0x2F, 0)
    SetChrSubChip(0x30, 0)
    SetChrSubChip(0x31, 0)
    SetChrSubChip(0x32, 0)
    SetChrSubChip(0x33, 0)
    SetChrSubChip(0x34, 0)
    SetChrSubChip(0x35, 0)
    SetChrSubChip(0x36, 0)
    SetChrSubChip(0x37, 0)
    SetChrSubChip(0x38, 0)
    SetChrSubChip(0x49, 0)
    SetChrSubChip(0x4A, 0)
    SetChrSubChip(0x4B, 0)
    SetChrSubChip(0x4C, 0)
    SetChrPos(0x28, 35820, 0, -960, 90)
    SetChrPos(0x29, 34250, 0, 720, 90)
    SetChrPos(0x2A, 34250, 0, -320, 90)
    SetChrPos(0x2B, 34250, 0, -1560, 90)
    SetChrPos(0x2C, 34250, 0, -2570, 90)
    SetChrPos(0x2D, 33000, 0, 720, 90)
    SetChrPos(0x2E, 33000, 0, -320, 90)
    SetChrPos(0x2F, 33000, 0, -1560, 90)
    SetChrPos(0x30, 33000, 0, -2570, 90)
    SetChrPos(0x31, 31750, 0, 720, 90)
    SetChrPos(0x32, 31750, 0, -320, 90)
    SetChrPos(0x33, 31750, 0, -1560, 90)
    SetChrPos(0x34, 31750, 0, -2570, 90)
    SetChrPos(0x35, 30500, 0, 720, 90)
    SetChrPos(0x36, 30500, 0, -320, 90)
    SetChrPos(0x37, 30500, 0, -1560, 90)
    SetChrPos(0x38, 30500, 0, -2570, 90)
    SetChrPos(0x49, 42120, 250, -7020, 90)
    SetChrPos(0x4A, 99670, 250, 40980, 180)
    SetChrPos(0x4B, 94910, 250, 44180, 90)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    OP_6D(41080, 0, -1410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(235000, 0)
    OP_6E(262, 0)
    LoadEffect(0x0, "map\\\\mp009_00.eff")
    LoadEffect(0x1, "monster\\\\msc0100.eff")
    LoadEffect(0x2, "Craft\\\\cr161_00.eff")
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    LoadEffect(0x4, "map\\\\mpsmk0.eff")
    LoadEffect(0x5, "map\\\\mpfire2.eff")
    LoadEffect(0x6, "map\\\\mpkaji0.eff")
    LoadEffect(0x7, "monster\\ms00300.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x6, 0xFF, 0xFF, 50440, 0, 64220, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_C8(0x200, 0x46, "C_PLAC24._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)
    Sleep(300)

    def lambda_6791():
        OP_6D(43810, 0, -2060, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6791)

    def lambda_67A9():
        OP_67(0, 6770, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67A9)

    def lambda_67C1():
        OP_6B(2200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67C1)

    def lambda_67D1():
        OP_6E(368, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_67D1)

    def lambda_67E1():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_67E1)
    Sleep(80)

    def lambda_67FC():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_67FC)

    def lambda_6812():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_6812)

    def lambda_6828():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_6828)

    def lambda_683E():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_683E)
    Sleep(80)

    def lambda_6859():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_6859)

    def lambda_686F():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_686F)

    def lambda_6885():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_6885)

    def lambda_689B():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_689B)
    Sleep(80)

    def lambda_68B6():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_68B6)

    def lambda_68CC():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_68CC)

    def lambda_68E2():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_68E2)

    def lambda_68F8():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_68F8)
    Sleep(80)

    def lambda_6913():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_6913)

    def lambda_6929():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_6929)

    def lambda_693F():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_693F)

    def lambda_6955():
        OP_94(0x0, 0xFE, 0x0, 0x2BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_6955)
    WaitChrThread(0x28, 0x1)
    OP_8C(0x28, 270, 400)
    WaitChrThread(0x35, 0x1)
    SetChrChipByIndex(0x29, 1)
    SetChrChipByIndex(0x2D, 1)
    SetChrChipByIndex(0x31, 4)
    SetChrChipByIndex(0x35, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x36, 0x1)
    SetChrChipByIndex(0x2A, 1)
    SetChrChipByIndex(0x2E, 1)
    SetChrChipByIndex(0x32, 4)
    SetChrChipByIndex(0x36, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x37, 0x1)
    SetChrChipByIndex(0x2B, 1)
    SetChrChipByIndex(0x2F, 1)
    SetChrChipByIndex(0x33, 4)
    SetChrChipByIndex(0x37, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x38, 0x1)
    SetChrChipByIndex(0x2C, 1)
    SetChrChipByIndex(0x30, 1)
    SetChrChipByIndex(0x34, 4)
    SetChrChipByIndex(0x38, 4)
    OP_22(0xD5, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #351
        0x28,
        (
            "#1186F#5PCommence Operation Clean Sweep!\x01",
            "Remember, our first priority is the\x01",
            "safety of the citizenry!\x02\x03",

            "Assist the army where possible!\x01",
            "Engage jaeger corps and archaisms\x01",
            "at your discretion!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName("Special Ops Troops")

    AnonymousTalk(    #352
        "\x07\x00#5SYES, MA'AM!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    SetChrChipByIndex(0x29, 2)
    SetChrChipByIndex(0x2A, 2)
    SetChrChipByIndex(0x2B, 2)
    SetChrChipByIndex(0x2C, 2)
    OP_43(0x29, 0x0, 0x1, 0x2F)
    OP_43(0x2A, 0x0, 0x1, 0x30)
    OP_43(0x2B, 0x0, 0x1, 0x31)
    OP_43(0x2C, 0x0, 0x1, 0x32)
    Sleep(100)
    SetChrChipByIndex(0x2D, 2)
    SetChrChipByIndex(0x2E, 2)
    SetChrChipByIndex(0x2F, 2)
    SetChrChipByIndex(0x30, 2)
    OP_43(0x2D, 0x0, 0x1, 0x2F)
    OP_43(0x2E, 0x0, 0x1, 0x30)
    OP_43(0x2F, 0x0, 0x1, 0x31)
    OP_43(0x30, 0x0, 0x1, 0x32)
    Sleep(100)
    SetChrChipByIndex(0x31, 6)
    SetChrChipByIndex(0x32, 6)
    SetChrChipByIndex(0x33, 6)
    SetChrChipByIndex(0x34, 6)
    OP_43(0x31, 0x0, 0x1, 0x2F)
    OP_43(0x32, 0x0, 0x1, 0x30)
    OP_43(0x33, 0x0, 0x1, 0x31)
    OP_43(0x34, 0x0, 0x1, 0x32)
    Sleep(100)
    SetChrChipByIndex(0x35, 6)
    SetChrChipByIndex(0x36, 6)
    SetChrChipByIndex(0x37, 6)
    SetChrChipByIndex(0x38, 6)
    OP_43(0x35, 0x0, 0x1, 0x2F)
    OP_43(0x36, 0x0, 0x1, 0x30)
    OP_43(0x37, 0x0, 0x1, 0x31)
    OP_43(0x38, 0x0, 0x1, 0x32)
    Sleep(100)

    def lambda_6BE2():
        OP_6D(47810, 0, -2060, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6BE2)
    OP_8C(0x28, 90, 400)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x0)
    OP_44(0x29, 0x0)
    OP_44(0x2A, 0x0)
    OP_44(0x2B, 0x0)
    OP_44(0x2C, 0x0)
    OP_44(0x2D, 0x0)
    OP_44(0x2E, 0x0)
    OP_44(0x2F, 0x0)
    OP_44(0x30, 0x0)
    OP_44(0x31, 0x0)
    OP_44(0x32, 0x0)
    OP_44(0x33, 0x0)
    OP_44(0x34, 0x0)
    OP_44(0x35, 0x0)
    OP_44(0x36, 0x0)
    OP_44(0x37, 0x0)
    OP_44(0x38, 0x0)
    OP_6D(97060, 250, 34890, 0)
    OP_67(0, 8290, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(40000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x43, 0x80)
    ClearChrFlags(0x44, 0x80)
    ClearChrFlags(0x45, 0x80)
    ClearChrFlags(0x46, 0x80)
    SetChrFlags(0x43, 0x4)
    SetChrFlags(0x44, 0x4)
    SetChrFlags(0x45, 0x4)
    SetChrFlags(0x46, 0x4)
    SetChrChipByIndex(0x43, 20)
    SetChrChipByIndex(0x44, 20)
    SetChrChipByIndex(0x45, 13)
    SetChrChipByIndex(0x46, 13)
    SetChrSubChip(0x43, 0)
    SetChrSubChip(0x44, 0)
    SetChrSubChip(0x45, 0)
    SetChrSubChip(0x46, 0)
    SetChrPos(0x43, 100320, 1000, 33430, 270)
    SetChrPos(0x44, 103220, 1000, 36090, 270)
    SetChrPos(0x45, 96780, 550, 70110, 180)
    SetChrPos(0x46, 94780, 550, 70110, 180)
    SetChrPos(0x29, 95630, 250, 61420, 180)
    SetChrPos(0x31, 95850, 0, 24930, 0)
    SetChrPos(0x32, 88010, 0, 35790, 90)
    SetChrPos(0x33, 89710, 0, 40080, 90)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    SetChrFlags(0x29, 0x20)
    SetChrFlags(0x2A, 0x20)
    SetChrFlags(0x2B, 0x20)
    SetChrFlags(0x2C, 0x20)
    SetChrFlags(0x31, 0x20)
    SetChrFlags(0x32, 0x20)
    SetChrFlags(0x33, 0x20)
    SetChrFlags(0x34, 0x20)
    SetChrFlags(0x43, 0x20)

    def lambda_6DA6():

        label("loc_6DA6")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6DA6")

    QueueWorkItem2(0x43, 2, lambda_6DA6)
    OP_43(0x28, 0x3, 0x1, 0x47)

    def lambda_6DC0():
        OP_8F(0xFE, 0x16314, 0x3E8, 0x8296, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_6DC0)
    OP_43(0x43, 0x0, 0x1, 0x33)
    Sleep(400)
    SetChrFlags(0x44, 0x20)

    def lambda_6DEC():

        label("loc_6DEC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6DEC")

    QueueWorkItem2(0x44, 2, lambda_6DEC)

    def lambda_6DFF():
        OP_8F(0xFE, 0x16CD8, 0x3E8, 0x8CFA, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_6DFF)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_6E29():
        OP_6D(96790, 250, 33400, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E29)

    def lambda_6E41():
        OP_67(0, 5810, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E41)

    def lambda_6E59():
        OP_6B(2860, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E59)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)
    OP_7D(0x0, 0x31, 0x32, 0xC8)
    ClearChrFlags(0x31, 0x20)

    def lambda_6E80():
        OP_8E(0xFE, 0x1766A, 0x0, 0x706C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_6E80)
    WaitChrThread(0x31, 0x1)
    OP_7D(0x1, 0x31, 0x0, 0x0)
    SetChrFlags(0x31, 0x20)
    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 1)

    def lambda_6EB7():
        OP_96(0xFE, 0x1766A, 0x0, 0x7E68, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_6EB7)
    Sleep(300)

    def lambda_6EDA():
        OP_99(0xFE, 0x1, 0x4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_6EDA)
    Sleep(100)

    def lambda_6EEF():
        OP_6D(96820, 250, 35080, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6EEF)
    OP_44(0x28, 0x3)
    OP_23(0x13A)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x43, 0, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_44(0x43, 0x1)
    OP_44(0x44, 0x1)
    OP_44(0x43, 0x2)
    SetChrChipByIndex(0x44, 12)
    SetChrSubChip(0x44, 0)
    SetChrChipByIndex(0x43, 12)
    SetChrSubChip(0x43, 0)

    def lambda_6F79():
        OP_8C(0xFE, 220, 200)
        ExitThread()

    QueueWorkItem(0x44, 3, lambda_6F79)

    def lambda_6F87():
        OP_8F(0xFE, 0x17368, 0x2EE, 0x8E94, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_6F87)

    def lambda_6FA2():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_6FA2)

    def lambda_6FBC():
        OP_8C(0xFE, 175, 400)
        ExitThread()

    QueueWorkItem(0x43, 3, lambda_6FBC)
    WaitChrThread(0x43, 0x1)

    def lambda_6FCF():

        label("loc_6FCF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6FCF")

    QueueWorkItem2(0x43, 2, lambda_6FCF)
    OP_44(0x44, 0x2)
    SetChrChipByIndex(0x44, 21)
    SetChrSubChip(0x44, 0)

    def lambda_6FF0():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_6FF0)
    Sleep(400)

    def lambda_7005():
        OP_99(0xFE, 0x2, 0x5, 0x9C4)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_7005)

    def lambda_7015():
        OP_8F(0xFE, 0x17A52, 0x3E8, 0x837C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_7015)
    Sleep(100)
    OP_7D(0x0, 0x31, 0x14, 0x64)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)

    def lambda_7047():
        OP_8C(0xFE, 310, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_7047)

    def lambda_7055():
        OP_96(0xFE, 0x1836C, 0xFA, 0x78A0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7055)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x31, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x31, 0x0, 0x0)

    def lambda_708F():
        OP_6C(55000, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_708F)

    def lambda_709F():
        OP_6B(3000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_709F)
    SetChrChipByIndex(0x32, 7)
    SetChrSubChip(0x32, 1)

    def lambda_70B9():
        OP_96(0xFE, 0x16D78, 0x0, 0x8E94, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_70B9)
    Sleep(300)

    def lambda_70DC():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_70DC)
    Sleep(200)

    def lambda_70F1():
        OP_6D(98560, 250, 36300, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70F1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x43, -1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)

    def lambda_7154():
        OP_8F(0xFE, 0x181B4, 0x3E8, 0x90F6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_7154)

    def lambda_716F():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_716F)

    def lambda_7189():
        OP_8C(0xFE, 280, 400)
        ExitThread()

    QueueWorkItem(0x43, 3, lambda_7189)
    SetChrFlags(0x33, 0x4)
    SetChrChipByIndex(0x33, 6)
    SetChrSubChip(0x33, 2)
    OP_7D(0x0, 0x33, 0x32, 0xC8)

    def lambda_71AE():
        OP_96(0xFE, 0x17AAC, 0xFA, 0x9C90, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_71AE)
    WaitChrThread(0x33, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x33, 0x0, 0x0)
    OP_8C(0x33, 160, 0)

    def lambda_71E5():
        OP_6D(99800, 250, 37640, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_71E5)

    def lambda_71FD():
        OP_67(0, 4650, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71FD)

    def lambda_7215():
        OP_6B(3190, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7215)

    def lambda_7225():
        OP_96(0xFE, 0x18312, 0x7D0, 0x91E6, 0x9C4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_7225)
    WaitChrThread(0x33, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_43(0x31, 0x0, 0x1, 0x34)
    OP_8C(0x33, 225, 0)
    SetChrFlags(0x33, 0x800)
    SetChrChipByIndex(0x33, 23)
    SetChrSubChip(0x33, 1)

    def lambda_726A():
        OP_96(0xFE, 0x17D0E, 0xFA, 0x89B2, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_726A)
    Sleep(200)

    def lambda_728D():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_728D)
    Sleep(200)

    def lambda_72A2():
        OP_6D(98770, 250, 35640, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_72A2)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x44, 900, 500, 1200, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x44, 22)
    SetChrSubChip(0x44, 0)

    def lambda_730F():
        OP_8F(0xFE, 0x1739A, 0x2EE, 0x7D31, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_730F)

    def lambda_732A():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_732A)
    WaitChrThread(0x44, 0x1)
    SetChrFlags(0x32, 0x800)
    SetChrChipByIndex(0x32, 7)
    SetChrSubChip(0x32, 0)

    def lambda_7358():
        OP_96(0xFE, 0x1712E, 0x0, 0x843A, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_7358)
    OP_8C(0x32, 190, 1000)
    OP_8C(0x32, 270, 1000)
    OP_8C(0x32, 0, 1000)
    OP_8C(0x32, 90, 1000)
    Sleep(50)
    OP_8C(0x32, 190, 0)

    def lambda_739E():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_739E)
    Sleep(100)

    def lambda_73B3():
        OP_6D(97710, 250, 35190, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_73B3)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x44, -500, 500, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)

    def lambda_7416():
        OP_8F(0xFE, 0x1717E, 0x2EE, 0x75BC, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_7416)

    def lambda_7431():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_7431)

    def lambda_744B():
        OP_8C(0xFE, 190, 400)
        ExitThread()

    QueueWorkItem(0x44, 3, lambda_744B)
    WaitChrThread(0x44, 0x1)

    def lambda_745E():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x44, 2, lambda_745E)
    Sleep(1000)
    PlayEffect(0x1, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x1, 0x2)
    OP_44(0x44, 0x2)
    SetChrFlags(0x44, 0x80)
    OP_83(0x1, 0x0)
    WaitChrThread(0x31, 0x0)
    Sleep(600)
    OP_22(0x193, 0x0, 0x64)
    Sleep(600)
    SetChrChipByIndex(0x32, 5)
    SetChrSubChip(0x32, 0)

    def lambda_74DF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x32, 3, lambda_74DF)
    Sleep(50)
    SetChrChipByIndex(0x33, 5)
    SetChrSubChip(0x33, 0)

    def lambda_74FC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x33, 3, lambda_74FC)
    Sleep(50)
    SetChrChipByIndex(0x31, 5)
    SetChrSubChip(0x31, 0)

    def lambda_7519():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_7519)

    def lambda_7527():
        OP_6D(96430, 250, 59720, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7527)

    def lambda_753F():
        OP_67(0, 7420, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_753F)

    def lambda_7557():
        OP_6C(42000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7557)

    def lambda_7567():
        OP_6B(2630, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7567)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 2)
    SetChrChipByIndex(0x32, 23)
    SetChrSubChip(0x32, 2)
    SetChrFlags(0x32, 0x4)
    SetChrPos(0x31, 88410, 250, 51790, 75)
    SetChrPos(0x32, 102920, 1250, 51790, 255)
    SetChrChipByIndex(0x46, 24)
    SetChrSubChip(0x46, 0)
    OP_43(0x28, 0x3, 0x1, 0x48)

    def lambda_75C8():
        OP_8E(0xFE, 0x1723C, 0x226, 0xB086, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_75C8)
    Sleep(200)
    SetChrChipByIndex(0x45, 24)
    SetChrSubChip(0x45, 0)

    def lambda_75F2():
        OP_8E(0xFE, 0x17A0C, 0x226, 0xB086, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_75F2)
    Sleep(600)

    def lambda_7612():
        OP_6D(96430, 250, 52470, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7612)
    Sleep(450)
    OP_43(0x46, 0x0, 0x1, 0x35)
    Sleep(50)
    OP_43(0x45, 0x0, 0x1, 0x36)
    WaitChrThread(0x46, 0x0)
    WaitChrThread(0x45, 0x0)
    Sleep(400)

    def lambda_7651():
        OP_6D(96010, 250, 52510, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7651)

    def lambda_7669():
        OP_6C(23000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7669)

    def lambda_7679():
        OP_6B(2530, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7679)
    SetChrChipByIndex(0x31, 5)
    SetChrSubChip(0x31, 0)

    def lambda_7693():
        OP_8C(0xFE, 355, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_7693)

    def lambda_76A1():
        OP_96(0xFE, 0x1723C, 0xFA, 0xBD4C, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_76A1)
    Sleep(200)
    SetChrChipByIndex(0x32, 5)
    SetChrSubChip(0x32, 0)

    def lambda_76CE():
        OP_8C(0xFE, 355, 400)
        ExitThread()

    QueueWorkItem(0x32, 3, lambda_76CE)

    def lambda_76DC():
        OP_96(0xFE, 0x17A0C, 0xFA, 0xBF40, 0x1F4, 0x9C4)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_76DC)
    WaitChrThread(0x31, 0x1)
    ClearChrFlags(0x31, 0x800)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0x32, 0x1)
    ClearChrFlags(0x32, 0x800)
    ClearChrFlags(0x32, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x46, 26)
    SetChrSubChip(0x46, 0)

    def lambda_7727():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_7727)
    Sleep(200)
    SetChrChipByIndex(0x45, 26)
    SetChrSubChip(0x45, 0)

    def lambda_7746():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_7746)
    WaitChrThread(0x45, 0x2)
    OP_22(0x193, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x29, 0x80)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 0)

    def lambda_7774():
        OP_6D(96010, 250, 58040, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7774)
    WaitChrThread(0x101, 0x0)
    Sleep(400)

    def lambda_7796():
        OP_6D(96010, 250, 57370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7796)

    def lambda_77AE():
        OP_67(0, 5360, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77AE)

    def lambda_77C6():
        OP_6C(40000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77C6)

    def lambda_77D6():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_77D6)
    Sleep(100)
    OP_82(0x1, 0x0)
    PlayEffect(0x7, 0x1, 0x29, -200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x45, 0, 0, -200, 0)
    Sleep(40)
    PlayEffect(0x7, 0x2, 0x29, 200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x46, 0, 0, -200, 0)
    Sleep(40)
    PlayEffect(0x7, 0x3, 0x29, -200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x45, 200, 0, 0, 0)
    Sleep(40)
    PlayEffect(0x7, 0x4, 0x29, 200, 400, -800, 0, 0, 0, 1000, 1000, 1000, 0x46, -200, 0, 0, 0)
    Sleep(1300)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_43(0x46, 0x0, 0x1, 0x37)
    Sleep(50)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_43(0x45, 0x0, 0x1, 0x38)
    WaitChrThread(0x46, 0x0)
    WaitChrThread(0x45, 0x0)
    SetChrChipByIndex(0x29, 1)
    SetChrSubChip(0x29, 0)
    OP_8C(0x29, 0, 800)

    def lambda_7926():
        OP_6B(3530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7926)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 0)
    ClearChrFlags(0x29, 0x20)

    def lambda_7945():
        OP_8E(0xFE, 0x1758E, 0xFA, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_7945)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)
    ClearChrFlags(0x31, 0x20)
    SetChrChipByIndex(0x32, 6)
    SetChrSubChip(0x32, 0)
    ClearChrFlags(0x32, 0x20)

    def lambda_797E():
        OP_8E(0xFE, 0x17A0C, 0xFA, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_797E)
    Sleep(100)

    def lambda_799E():
        OP_8E(0xFE, 0x1723C, 0xFA, 0x11170, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_799E)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadEffect(0x1, "monster\\\\msc0568.eff")
    LoadEffect(0x2, "monster\\\\msc0555.eff")
    LoadEffect(0x7, "map\\\\mp003_00.eff")
    OP_44(0x101, 0x0)
    OP_44(0x29, 0x1)
    OP_44(0x31, 0x1)
    OP_44(0x32, 0x1)
    SetChrPos(0x49, 40700, 1250, 46910, 270)
    SetChrPos(0x4A, 99670, 250, 40980, 180)
    SetChrPos(0x4B, 94910, 250, 44180, 90)
    OP_6D(70190, 1250, 52590, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(156000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x39, 29)
    SetChrChipByIndex(0x3A, 29)
    SetChrChipByIndex(0x3B, 35)
    SetChrChipByIndex(0x3C, 35)
    SetChrChipByIndex(0x3D, 35)
    SetChrChipByIndex(0x29, 0)
    SetChrChipByIndex(0x2A, 0)
    SetChrChipByIndex(0x2B, 2)
    SetChrChipByIndex(0x2C, 2)
    SetChrChipByIndex(0x2D, 2)
    SetChrChipByIndex(0x31, 4)
    SetChrSubChip(0x39, 0)
    SetChrSubChip(0x3A, 0)
    SetChrSubChip(0x3B, 0)
    SetChrSubChip(0x3C, 0)
    SetChrSubChip(0x3D, 0)
    SetChrSubChip(0x29, 0)
    SetChrSubChip(0x2A, 0)
    SetChrSubChip(0x2B, 0)
    SetChrSubChip(0x2C, 0)
    SetChrSubChip(0x2D, 0)
    SetChrSubChip(0x31, 0)
    SetChrPos(0x39, 81020, 1250, 53150, 0)
    SetChrPos(0x3A, 59440, 1250, 53150, 0)
    SetChrPos(0x3B, 70350, 1250, 33350, 0)
    SetChrPos(0x3C, 68900, 1250, 31550, 0)
    SetChrPos(0x3D, 71360, 1250, 31750, 0)
    SetChrPos(0x29, 59440, 1250, 53150, 90)
    SetChrPos(0x2A, 81020, 1250, 53150, 270)
    SetChrPos(0x2B, 70130, 1250, 35150, 0)
    SetChrPos(0x2C, 71250, 1250, 33950, 0)
    SetChrPos(0x2D, 69040, 1250, 33380, 0)
    SetChrPos(0x31, 69960, 250, 66900, 180)
    ClearChrFlags(0x39, 0x80)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x39, 0x40)
    SetChrFlags(0x3A, 0x40)
    SetChrFlags(0x3B, 0x40)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3D, 0x40)
    SetChrFlags(0x29, 0x40)
    SetChrFlags(0x2A, 0x40)
    SetChrFlags(0x2B, 0x40)
    SetChrFlags(0x2C, 0x40)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x31, 0x40)

    def lambda_7C13():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7C13)
    FadeToBright(1000, 0)

    def lambda_7C2C():
        OP_8E(0xFE, 0x1156C, 0x4E2, 0xCF9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_7C2C)
    Sleep(400)

    def lambda_7C4C():
        OP_8E(0xFE, 0x10F40, 0x4E2, 0xCF9E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_7C4C)
    OP_0D()
    WaitChrThread(0x39, 0x1)
    SetChrChipByIndex(0x39, 14)
    SetChrSubChip(0x39, 0)
    WaitChrThread(0x3A, 0x1)
    SetChrChipByIndex(0x3A, 14)
    SetChrSubChip(0x3A, 0)
    WaitChrThread(0x101, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_43(0x29, 0x0, 0x1, 0x39)
    Sleep(400)

    def lambda_7CA6():
        OP_6D(70280, 1250, 52460, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7CA6)

    def lambda_7CBE():
        OP_6B(2150, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CBE)
    Sleep(200)
    OP_43(0x2A, 0x0, 0x1, 0x3C)
    WaitChrThread(0x29, 0x0)

    def lambda_7CDF():
        OP_6D(70160, 1250, 52920, 3400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7CDF)

    def lambda_7CF7():
        OP_67(0, 11000, -10000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CF7)

    def lambda_7D0F():
        OP_6B(2340, 3400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D0F)

    def lambda_7D1F():
        OP_6C(90000, 3400)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7D1F)
    OP_43(0x3A, 0x0, 0x1, 0x3B)
    WaitChrThread(0x2A, 0x0)
    OP_43(0x2A, 0x0, 0x1, 0x3D)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x3A, 15)
    SetChrSubChip(0x3A, 0)
    SetChrPos(0x3A, 69170, 1250, 53160, 250)
    SetChrChipByIndex(0x2A, 1)
    SetChrSubChip(0x2A, 0)

    def lambda_7D6C():
        OP_6D(69190, 2150, 55290, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7D6C)

    def lambda_7D84():
        OP_67(0, 7040, -10000, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D84)

    def lambda_7D9C():
        OP_6C(46000, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7D9C)
    SetChrFlags(0x31, 0x800)
    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 2)

    def lambda_7DBB():
        OP_96(0xFE, 0x11148, 0x4E2, 0xD58E, 0x7D0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_7DBB)
    Sleep(650)

    def lambda_7DDE():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_7DDE)
    Sleep(150)
    PlayEffect(0x1, 0x1, 0xFF, 69960, 1250, 53070, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x258, 0xBB8, 0xC8)

    def lambda_7E39():
        OP_6D(69320, 2150, 48410, 600)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7E39)

    def lambda_7E51():
        OP_6B(2560, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E51)

    def lambda_7E61():
        OP_6C(32000, 600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E61)
    SetChrChipByIndex(0x39, 16)
    SetChrSubChip(0x39, 0)
    OP_8C(0x39, 0, 0)

    def lambda_7E82():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_7E82)

    def lambda_7E9C():
        OP_96(0xFE, 0x116CA, 0xFA, 0xB284, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_7E9C)
    SetChrChipByIndex(0x3A, 16)
    SetChrSubChip(0x3A, 0)
    OP_8C(0x3A, 0, 0)

    def lambda_7ECB():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_7ECB)

    def lambda_7EE5():
        OP_96(0xFE, 0x10E96, 0xFA, 0xB158, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_7EE5)
    WaitChrThread(0x3A, 0x1)
    SetChrChipByIndex(0x3A, 17)
    SetChrSubChip(0x3A, 2)
    OP_43(0x3A, 0x0, 0x1, 0x1E)
    WaitChrThread(0x39, 0x1)
    SetChrChipByIndex(0x39, 17)
    SetChrSubChip(0x39, 3)
    OP_43(0x39, 0x0, 0x1, 0x1F)
    WaitChrThread(0x101, 0x0)

    def lambda_7F34():
        OP_6D(71130, 250, 45090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7F34)

    def lambda_7F4C():
        OP_67(0, 9520, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F4C)

    def lambda_7F64():
        OP_6B(1750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F64)

    def lambda_7F74():
        OP_6C(44000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7F74)

    def lambda_7F84():
        OP_6E(354, 2000)
        ExitThread()

    QueueWorkItem(0x28, 0, lambda_7F84)

    def lambda_7F94():
        OP_8F(0xFE, 0x112CE, 0xFA, 0xAC4E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_7F94)

    def lambda_7FAF():
        OP_8F(0xFE, 0x10D24, 0xFA, 0xA97E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_7FAF)

    def lambda_7FCA():
        OP_8F(0xFE, 0x116C0, 0xFA, 0xA7DA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_7FCA)
    WaitChrThread(0x3B, 0x1)
    SetChrChipByIndex(0x3B, 33)
    SetChrSubChip(0x3B, 0)
    WaitChrThread(0x3C, 0x1)
    SetChrChipByIndex(0x3C, 33)
    SetChrSubChip(0x3C, 0)
    WaitChrThread(0x3D, 0x1)
    SetChrChipByIndex(0x3D, 33)
    SetChrSubChip(0x3D, 0)
    WaitChrThread(0x101, 0x0)

    def lambda_8017():
        OP_6D(70780, 250, 47510, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8017)

    def lambda_802F():
        OP_67(0, 8460, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_802F)

    def lambda_8047():
        OP_6B(2270, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8047)

    def lambda_8057():
        OP_6C(32000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8057)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 0)
    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 0)
    SetChrChipByIndex(0x2A, 2)
    SetChrSubChip(0x2A, 0)
    SetChrPos(0x29, 68800, 1250, 55030, 180)
    SetChrPos(0x31, 70040, 1250, 53370, 180)
    SetChrPos(0x2A, 71540, 1250, 55010, 180)
    ClearChrFlags(0x29, 0x20)
    ClearChrFlags(0x31, 0x20)
    ClearChrFlags(0x2A, 0x20)

    def lambda_80C7():
        OP_8F(0xFE, 0x10CC0, 0x4E2, 0xC756, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_80C7)

    def lambda_80E2():
        OP_8F(0xFE, 0x11198, 0x4E2, 0xC4C2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_80E2)

    def lambda_80FD():
        OP_8F(0xFE, 0x11774, 0x4E2, 0xC742, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_80FD)
    WaitChrThread(0x29, 0x1)
    SetChrChipByIndex(0x29, 1)
    SetChrSubChip(0x29, 0)
    WaitChrThread(0x31, 0x1)
    SetChrChipByIndex(0x31, 5)
    SetChrSubChip(0x31, 0)
    WaitChrThread(0x2A, 0x1)
    SetChrChipByIndex(0x2A, 1)
    SetChrSubChip(0x2A, 0)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    OP_62(0x3D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(400)

    def lambda_8170():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3D, 3, lambda_8170)
    Sleep(400)

    def lambda_8183():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3C, 3, lambda_8183)
    Sleep(200)

    def lambda_8196():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x3B, 3, lambda_8196)
    Sleep(400)
    Fade(500)
    OP_6D(70570, 250, 40500, 0)
    OP_67(0, 8460, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(144000, 0)
    OP_6E(354, 0)
    SetChrPos(0x39, 71170, 250, 45200, 0)
    SetChrPos(0x3B, 70190, 250, 44050, 180)
    SetChrPos(0x3D, 71660, 250, 42970, 180)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2B, 0x20)
    ClearChrFlags(0x2C, 0x20)
    ClearChrFlags(0x2D, 0x20)

    def lambda_823C():
        OP_8F(0xFE, 0x111F2, 0x4E2, 0x98EE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_823C)

    def lambda_8257():
        OP_8F(0xFE, 0x11652, 0x4E2, 0x9632, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_8257)

    def lambda_8272():
        OP_8F(0xFE, 0x10DB0, 0x4E2, 0x95EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8272)
    WaitChrThread(0x2B, 0x1)
    SetChrChipByIndex(0x2B, 1)
    SetChrSubChip(0x2B, 0)
    WaitChrThread(0x2C, 0x1)
    SetChrChipByIndex(0x2C, 1)
    SetChrSubChip(0x2C, 0)
    WaitChrThread(0x2D, 0x1)
    SetChrChipByIndex(0x2D, 1)
    SetChrSubChip(0x2D, 0)

    def lambda_82BA():
        OP_6D(70870, 250, 43890, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_82BA)

    def lambda_82D2():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_82D2)

    def lambda_82E2():
        OP_6C(135000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_82E2)
    SetChrChipByIndex(0x3C, 35)
    SetChrSubChip(0x3C, 0)

    def lambda_82FC():
        OP_8F(0xFE, 0x10D24, 0xFA, 0xAAAA, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_82FC)
    WaitChrThread(0x3C, 0x1)
    OP_44(0x3C, 0x2)
    SetChrChipByIndex(0x3C, 33)
    SetChrSubChip(0x3C, 0)
    SetChrChipByIndex(0x3D, 35)
    SetChrSubChip(0x3D, 0)

    def lambda_8334():
        OP_8F(0xFE, 0x117EC, 0xFA, 0xAA96, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_8334)
    WaitChrThread(0x3D, 0x1)
    OP_44(0x3D, 0x2)
    SetChrChipByIndex(0x3D, 33)
    SetChrSubChip(0x3D, 0)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_43(0x29, 0x0, 0x1, 0x22)
    OP_43(0x2A, 0x0, 0x1, 0x21)
    OP_43(0x31, 0x0, 0x1, 0x20)
    OP_43(0x2B, 0x0, 0x1, 0x23)
    OP_43(0x2C, 0x0, 0x1, 0x24)
    OP_43(0x2D, 0x0, 0x1, 0x25)
    OP_43(0x39, 0x0, 0x1, 0x26)
    OP_43(0x3A, 0x0, 0x1, 0x27)
    OP_43(0x3B, 0x0, 0x1, 0x28)
    OP_43(0x3C, 0x0, 0x1, 0x29)
    OP_43(0x3D, 0x0, 0x1, 0x2A)
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x5A)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x5A)
    Sleep(100)
    OP_22(0x84, 0x0, 0x5A)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x5A)
    Sleep(200)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x5A)
    Sleep(200)
    OP_22(0x84, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(100)
    OP_22(0xA4, 0x0, 0x50)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x50)
    Sleep(200)
    OP_22(0xD6, 0x0, 0x46)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x46)
    Sleep(2000)
    OP_6D(42310, 1250, 51050, 0)
    OP_67(0, 5870, -10000, 0)
    OP_6B(2400, 0)
    OP_6C(304000, 0)
    OP_6E(332, 0)
    SetChrChipByIndex(0x47, 9)
    SetChrChipByIndex(0x48, 10)
    SetChrPos(0x47, 43000, 1250, 50000, 90)
    SetChrPos(0x48, 43000, 1250, 51100, 90)
    ClearChrFlags(0x47, 0x80)
    ClearChrFlags(0x48, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_DC()

    ChrTalk(    #353
        0x47,
        (
            "#143F#6PHoly... Just when I thought this\x01",
            "couldn't get ANY crazier!\x02\x03",

            "When did the Special Ops\x01",
            "guys show up?!\x02\x03",

            "And they're going after the\x01",
            "society's goons, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x48,
        (
            "#151F#6PMaybe this is, you know,\x01",
            "heavy penance for awwwwful\x01",
            "deeds! And stuff!\x02\x03",

            "Or maybe they're trying to remind\x01",
            "everyone how awesome they are?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x47, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #355
        0x47,
        (
            "#145F#6PWho the hell would...? They're trying\x01",
            "to clear their name, Dorothy.\x02\x03",

            "#144FAh, the hell with it!\x02\x03",

            "Dorothy! Make with the camera!\x02\x03",

            "Shoot and shoot until we can't\x01",
            "stuff film in there anymore!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x48,
        "#150F#6PAye, aye, sir!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x48, 11)
    OP_0D()
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x48, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x48, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x48, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_6229 end

    def Function_30_88A4(): pass

    label("Function_30_88A4")


    def lambda_88AA():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_88AA)
    Sleep(1200)
    OP_44(0x3A, 0x2)

    def lambda_88CD():
        OP_99(0xFE, 0x2, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_88CD)
    WaitChrThread(0x3A, 0x2)
    Return()

    # Function_30_88A4 end

    def Function_31_88DD(): pass

    label("Function_31_88DD")


    def lambda_88E3():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_88E3)
    Sleep(2000)
    OP_44(0x39, 0x2)

    def lambda_8906():
        OP_99(0xFE, 0x3, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_8906)
    WaitChrThread(0x39, 0x2)
    Return()

    # Function_31_88DD end

    def Function_32_8916(): pass

    label("Function_32_8916")

    SetChrChipByIndex(0x31, 23)
    SetChrSubChip(0x31, 2)

    def lambda_8926():
        OP_96(0xFE, 0x11198, 0xFA, 0xB4D2, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_8926)
    Sleep(400)

    def lambda_8949():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_8949)
    WaitChrThread(0x31, 0x1)
    OP_22(0x84, 0x0, 0x64)
    Sleep(400)

    def lambda_8968():
        OP_99(0xFE, 0x5, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_8968)

    def lambda_8978():
        OP_96(0xFE, 0x11198, 0xFA, 0xBEB4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_8978)
    WaitChrThread(0x31, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_89A0():
        OP_96(0xFE, 0x11198, 0xFA, 0xAD02, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_89A0)
    Sleep(300)

    def lambda_89C3():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_89C3)
    WaitChrThread(0x31, 0x1)
    Return()

    # Function_32_8916 end

    def Function_33_89D3(): pass

    label("Function_33_89D3")

    Sleep(200)
    SetChrFlags(0x2A, 0x20)
    SetChrChipByIndex(0x2A, 2)
    SetChrSubChip(0x2A, 2)

    def lambda_89ED():
        OP_96(0xFE, 0x117B0, 0xFA, 0xB98C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_89ED)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8A15():
        OP_96(0xFE, 0x11E04, 0xFA, 0xB216, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8A15)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8A3D():
        OP_96(0xFE, 0x11E86, 0xFA, 0xBA40, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8A3D)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)
    OP_8C(0x2A, 220, 0)

    def lambda_8A76():
        OP_8F(0xFE, 0x11864, 0xFA, 0xB31A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8A76)
    WaitChrThread(0x2A, 0x1)
    Return()

    # Function_33_89D3 end

    def Function_34_8A91(): pass

    label("Function_34_8A91")

    Sleep(600)
    SetChrFlags(0x29, 0x20)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 2)

    def lambda_8AAB():
        OP_96(0xFE, 0x10DEC, 0xFA, 0xBA2C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8AAB)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8AD3():
        OP_96(0xFE, 0x10E64, 0xFA, 0xBF68, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8AD3)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 5)

    def lambda_8B05():
        OP_8F(0xFE, 0x10E28, 0xFA, 0xB40A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_8B05)
    WaitChrThread(0x29, 0x1)
    Return()

    # Function_34_8A91 end

    def Function_35_8B20(): pass

    label("Function_35_8B20")

    Sleep(400)
    SetChrFlags(0x2B, 0x20)
    SetChrChipByIndex(0x2B, 2)
    SetChrSubChip(0x2B, 2)

    def lambda_8B3A():
        OP_96(0xFE, 0x10CD4, 0xFA, 0xA0E6, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8B3A)
    WaitChrThread(0x2B, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8B62():
        OP_96(0xFE, 0x11774, 0xFA, 0xA3DE, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8B62)
    WaitChrThread(0x2B, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8B8A():
        OP_96(0xFE, 0x111D4, 0x2EE, 0x9D58, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8B8A)
    WaitChrThread(0x2B, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2B, 3)
    SetChrSubChip(0x2B, 5)

    def lambda_8BBC():
        OP_8F(0xFE, 0x111DE, 0xFA, 0xA8A2, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8BBC)
    WaitChrThread(0x2B, 0x1)
    Return()

    # Function_35_8B20 end

    def Function_36_8BD7(): pass

    label("Function_36_8BD7")

    Sleep(100)
    SetChrFlags(0x2C, 0x20)
    SetChrChipByIndex(0x2C, 2)
    SetChrSubChip(0x2C, 2)

    def lambda_8BF1():
        OP_96(0xFE, 0x11774, 0xFA, 0xA258, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_8BF1)
    WaitChrThread(0x2C, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x2C, 315, 0)

    def lambda_8C20():
        OP_96(0xFE, 0x11D00, 0xFA, 0xA60E, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_8C20)
    WaitChrThread(0x2C, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x2C, 225, 0)

    def lambda_8C4F():
        OP_96(0xFE, 0x11D8C, 0xFA, 0xAED8, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_8C4F)
    WaitChrThread(0x2C, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2C, 3)
    SetChrSubChip(0x2C, 5)

    def lambda_8C81():
        OP_8F(0xFE, 0x11A44, 0xFA, 0xABAE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_8C81)
    WaitChrThread(0x2C, 0x1)
    Return()

    # Function_36_8BD7 end

    def Function_37_8C9C(): pass

    label("Function_37_8C9C")

    Sleep(600)
    SetChrFlags(0x2D, 0x20)
    SetChrChipByIndex(0x2D, 2)
    SetChrSubChip(0x2D, 2)

    def lambda_8CB6():
        OP_96(0xFE, 0x11594, 0x4E2, 0x9B78, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8CB6)
    WaitChrThread(0x2D, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8CDE():
        OP_96(0xFE, 0x10D6A, 0x1F4, 0x9E2A, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8CDE)
    WaitChrThread(0x2D, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x2D, 45, 0)

    def lambda_8D0D():
        OP_96(0xFE, 0x10734, 0xFA, 0xA58C, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8D0D)
    WaitChrThread(0x2D, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2D, 3)
    SetChrSubChip(0x2D, 5)

    def lambda_8D3F():
        OP_8F(0xFE, 0x10AC2, 0xFA, 0xA910, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_8D3F)
    WaitChrThread(0x2D, 0x1)
    Return()

    # Function_37_8C9C end

    def Function_38_8D5A(): pass

    label("Function_38_8D5A")

    Sleep(300)
    SetChrFlags(0x39, 0x20)
    SetChrChipByIndex(0x39, 29)
    SetChrSubChip(0x39, 2)
    OP_8C(0x39, 270, 0)

    def lambda_8D7B():
        OP_96(0xFE, 0x11CF6, 0xFA, 0xAF8C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_8D7B)
    WaitChrThread(0x39, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x39, 30)
    SetChrSubChip(0x39, 0)

    def lambda_8DAD():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_8DAD)

    def lambda_8DBD():
        OP_8F(0xFE, 0x115E4, 0xFA, 0xB130, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_8DBD)
    WaitChrThread(0x39, 0x1)
    Return()

    # Function_38_8D5A end

    def Function_39_8DD8(): pass

    label("Function_39_8DD8")

    Sleep(300)
    SetChrFlags(0x3A, 0x20)
    SetChrChipByIndex(0x3A, 29)
    SetChrSubChip(0x3A, 2)
    OP_8C(0x3A, 90, 0)

    def lambda_8DF9():
        OP_96(0xFE, 0x1091E, 0xFA, 0xB18A, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_8DF9)
    WaitChrThread(0x3A, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_8E21():
        OP_96(0xFE, 0x107C0, 0xFA, 0xAADC, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_8E21)
    WaitChrThread(0x3A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x3A, 30)
    SetChrSubChip(0x3A, 0)

    def lambda_8E53():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_8E53)

    def lambda_8E63():
        OP_8F(0xFE, 0x10E1E, 0xFA, 0xB22A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_8E63)
    WaitChrThread(0x3A, 0x1)
    Return()

    # Function_39_8DD8 end

    def Function_40_8E7E(): pass

    label("Function_40_8E7E")

    Sleep(200)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)
    SetChrSubChip(0xFE, 0)

    def lambda_8E98():

        label("loc_8E98")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_8E98")

    QueueWorkItem2(0xFE, 2, lambda_8E98)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(1000)
    OP_44(0xFE, 0x2)
    Return()

    # Function_40_8E7E end

    def Function_41_8F9C(): pass

    label("Function_41_8F9C")

    Sleep(400)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)
    SetChrSubChip(0xFE, 0)

    def lambda_8FB6():

        label("loc_8FB6")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_8FB6")

    QueueWorkItem2(0xFE, 2, lambda_8FB6)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(1000)
    OP_44(0xFE, 0x2)
    Return()

    # Function_41_8F9C end

    def Function_42_90BA(): pass

    label("Function_42_90BA")

    Sleep(600)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)
    SetChrSubChip(0xFE, 0)

    def lambda_90D4():

        label("loc_90D4")

        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        OP_48()
        Jump("loc_90D4")

    QueueWorkItem2(0xFE, 2, lambda_90D4)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    PlayEffect(0x2, 0xFF, 0xFE, 0, 750, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFE, 0, 500, -4000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(1000)
    OP_44(0xFE, 0x2)
    Return()

    # Function_42_90BA end

    def Function_43_91D8(): pass

    label("Function_43_91D8")

    OP_8E(0xFE, 0xB75C, 0x0, 0x532, 0x1388, 0x0)
    OP_8E(0xFE, 0xCA94, 0x0, 0x532, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_43_91D8 end

    def Function_44_9206(): pass

    label("Function_44_9206")

    OP_8E(0xFE, 0xB75C, 0x0, 0x82, 0x1388, 0x0)
    OP_8E(0xFE, 0xCA62, 0x0, 0x82, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_44_9206 end

    def Function_45_9234(): pass

    label("Function_45_9234")

    OP_8E(0xFE, 0xB70C, 0x0, 0xFFFFF786, 0x1388, 0x0)
    OP_8E(0xFE, 0xBC0C, 0x0, 0xFFFFF966, 0x1388, 0x0)
    OP_8E(0xFE, 0xD4E4, 0x0, 0xFFFFF966, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_45_9234 end

    def Function_46_9276(): pass

    label("Function_46_9276")

    OP_8E(0xFE, 0xB70C, 0x0, 0xFFFFF312, 0x1388, 0x0)
    OP_8E(0xFE, 0xBC0C, 0x0, 0xFFFFF4DE, 0x1388, 0x0)
    OP_8E(0xFE, 0xD4E4, 0x0, 0xFFFFF4DE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_46_9276 end

    def Function_47_92B8(): pass

    label("Function_47_92B8")

    OP_8E(0xFE, 0xBF2C, 0x0, 0x65E, 0x1388, 0x0)
    OP_8E(0xFE, 0xC7BA, 0x0, 0xC8A, 0x1388, 0x0)
    OP_8E(0xFE, 0xCC74, 0x0, 0x15C2, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_47_92B8 end

    def Function_48_92FA(): pass

    label("Function_48_92FA")

    OP_8E(0xFE, 0xBBC6, 0x0, 0xC8, 0x1388, 0x0)
    OP_8E(0xFE, 0xCB16, 0x0, 0x35C, 0x1388, 0x0)
    OP_8E(0xFE, 0xE448, 0x0, 0x35C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_48_92FA end

    def Function_49_933C(): pass

    label("Function_49_933C")

    OP_8E(0xFE, 0xBB62, 0x0, 0xFFFFF79A, 0x1388, 0x0)
    OP_8E(0xFE, 0xCA94, 0x0, 0xFFFFF4FC, 0x1388, 0x0)
    OP_8E(0xFE, 0xE3F8, 0x0, 0xFFFFF4FC, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_49_933C end

    def Function_50_937E(): pass

    label("Function_50_937E")

    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xB676, 0x0, 0xFFFFF164, 0x1388, 0x0)
    OP_8E(0xFE, 0xCF08, 0xFA, 0xFFFFE8FE, 0x1388, 0x0)
    OP_8E(0xFE, 0xDEF8, 0xFA, 0xFFFFE5D4, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_50_937E end

    def Function_51_93CA(): pass

    label("Function_51_93CA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x178F4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_93E0")
    Sleep(15)
    Jump("Function_51_93CA")

    label("loc_93E0")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x2EE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_93F1():
        OP_8F(0xFE, 0x16314, 0x2EE, 0x8296, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_93F1)
    Return()

    # Function_51_93CA end

    def Function_52_9407(): pass

    label("Function_52_9407")

    SetChrChipByIndex(0x31, 6)
    SetChrSubChip(0x31, 6)
    OP_7D(0x0, 0x31, 0x32, 0x64)

    def lambda_941F():
        OP_8C(0xFE, 280, 400)
        ExitThread()

    QueueWorkItem(0x31, 3, lambda_941F)

    def lambda_942D():
        OP_96(0xFE, 0x18D76, 0xFA, 0x8160, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_942D)
    WaitChrThread(0x31, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x31, 0x0, 0x0)
    SetChrChipByIndex(0x31, 7)
    SetChrSubChip(0x31, 1)

    def lambda_9467():
        OP_96(0xFE, 0x184A2, 0xFA, 0x8B92, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_9467)
    Sleep(200)

    def lambda_948A():
        OP_99(0xFE, 0x1, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_948A)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x43, 500, 500, -1200, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x43, 22)
    SetChrSubChip(0x43, 0)

    def lambda_94F4():
        OP_8F(0xFE, 0x1780E, 0x2EE, 0x9448, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_94F4)

    def lambda_950F():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_950F)
    WaitChrThread(0x43, 0x1)

    def lambda_952E():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x43, 2, lambda_952E)
    Sleep(1000)
    PlayEffect(0x1, 0x1, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x1, 0x2)
    OP_44(0x43, 0x2)
    SetChrFlags(0x43, 0x80)
    OP_83(0x1, 0x0)
    Return()

    # Function_52_9407 end

    def Function_53_958C(): pass

    label("Function_53_958C")


    def lambda_9592():
        OP_96(0xFE, 0x16D8C, 0x0, 0xCA4E, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x31, 1, lambda_9592)
    Sleep(400)

    def lambda_95B5():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_95B5)
    Sleep(200)
    OP_44(0x46, 0x1)
    OP_44(0x28, 0x3)
    OP_23(0x13F)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x31, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrFlags(0x46, 0x20)
    SetChrChipByIndex(0x46, 25)
    SetChrSubChip(0x46, 0)

    def lambda_962F():
        OP_8F(0xFE, 0x1723C, 0x226, 0xD3D6, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_962F)

    def lambda_964A():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_964A)
    WaitChrThread(0x46, 0x1)
    Return()

    # Function_53_958C end

    def Function_54_9664(): pass

    label("Function_54_9664")


    def lambda_966A():
        OP_96(0xFE, 0x17EBC, 0x0, 0xCA4E, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x32, 1, lambda_966A)
    Sleep(550)

    def lambda_968D():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_968D)
    Sleep(200)
    OP_44(0x45, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x32, -1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrFlags(0x45, 0x20)
    SetChrChipByIndex(0x45, 25)
    SetChrSubChip(0x45, 0)

    def lambda_9700():
        OP_8F(0xFE, 0x17A0C, 0x226, 0xCFEE, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_9700)

    def lambda_971B():
        OP_9E(0xFE, 0x3C, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_971B)
    WaitChrThread(0x45, 0x1)
    Return()

    # Function_54_9664 end

    def Function_55_9735(): pass

    label("Function_55_9735")

    SetChrChipByIndex(0x46, 25)
    SetChrSubChip(0x46, 0)

    def lambda_9745():
        OP_9E(0xFE, 0x3C, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_9745)
    WaitChrThread(0x46, 0x2)

    def lambda_9764():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x46, 2, lambda_9764)
    Sleep(1000)
    PlayEffect(0x1, 0x5, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x5, 0x2)
    OP_44(0x46, 0x2)
    SetChrFlags(0x46, 0x80)
    OP_83(0x5, 0x0)
    Return()

    # Function_55_9735 end

    def Function_56_97C2(): pass

    label("Function_56_97C2")

    SetChrChipByIndex(0x45, 25)
    SetChrSubChip(0x45, 0)

    def lambda_97D2():
        OP_9E(0xFE, 0x3C, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_97D2)
    WaitChrThread(0x45, 0x2)

    def lambda_97F1():
        OP_9E(0xFE, 0x14, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x45, 2, lambda_97F1)
    Sleep(1200)
    PlayEffect(0x1, 0x6, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_83(0x6, 0x2)
    OP_44(0x45, 0x2)
    SetChrFlags(0x45, 0x80)
    OP_83(0x6, 0x0)
    Return()

    # Function_56_97C2 end

    def Function_57_984F(): pass

    label("Function_57_984F")

    OP_7D(0x0, 0x29, 0x14, 0x64)

    def lambda_985D():
        OP_96(0xFE, 0xFDFB, 0x4E2, 0xC6AC, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_985D)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_9885():
        OP_8C(0xFE, 250, 300)
        ExitThread()

    QueueWorkItem(0x3A, 3, lambda_9885)
    OP_8C(0x29, 20, 0)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 0)

    def lambda_98A4():
        OP_96(0xFE, 0x10B94, 0x4E2, 0xCD32, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_98A4)
    Sleep(200)

    def lambda_98C7():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_98C7)
    WaitChrThread(0x29, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x3A, -500, 500, -500, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_7D(0x1, 0x29, 0x0, 0x0)
    SetChrChipByIndex(0x3A, 17)
    SetChrSubChip(0x3A, 1)
    OP_44(0x3A, 0x3)
    OP_8C(0x3A, 200, 0)
    SetChrFlags(0x3A, 0x20)

    def lambda_9949():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_9949)

    def lambda_9963():
        OP_8F(0xFE, 0x11008, 0x4E2, 0xD066, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9963)
    WaitChrThread(0x3A, 0x1)
    Return()

    # Function_57_984F end

    def Function_58_997E(): pass

    label("Function_58_997E")

    OP_7D(0x0, 0x29, 0x14, 0x64)
    SetChrChipByIndex(0x29, 2)
    SetChrSubChip(0x29, 6)

    def lambda_9996():
        OP_96(0xFE, 0x10806, 0x4E2, 0xC8E6, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9996)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_99BE():
        OP_8C(0xFE, 340, 400)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_99BE)

    def lambda_99CC():
        OP_96(0xFE, 0x11242, 0x4E2, 0xC8E6, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_99CC)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_99F4():
        OP_8C(0xFE, 160, 400)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_99F4)

    def lambda_9A02():
        OP_96(0xFE, 0x10996, 0x4E2, 0xD804, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9A02)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x29, 0x0, 0x0)
    SetChrChipByIndex(0x29, 3)
    SetChrSubChip(0x29, 5)

    def lambda_9A3C():
        OP_8F(0xFE, 0x10CE8, 0x4E2, 0xD188, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9A3C)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x29, 500, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x3A, 31)
    SetChrSubChip(0x3A, 0)
    OP_8C(0x3A, 340, 0)

    def lambda_9AB8():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_9AB8)

    def lambda_9AD2():
        OP_96(0xFE, 0x11238, 0x4E2, 0xC832, 0xC8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9AD2)
    WaitChrThread(0x3A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x3A, 30)
    SetChrSubChip(0x3A, 0)

    def lambda_9B04():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_9B04)
    WaitChrThread(0x3A, 0x2)
    OP_7D(0x0, 0x29, 0x14, 0x64)
    SetChrChipByIndex(0x29, 1)
    SetChrSubChip(0x29, 2)

    def lambda_9B2B():
        OP_8C(0xFE, 80, 400)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_9B2B)

    def lambda_9B39():
        OP_96(0xFE, 0x104DC, 0x4E2, 0xCFDA, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_9B39)

    def lambda_9B57():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_9B57)

    def lambda_9B67():
        OP_8F(0xFE, 0x10F04, 0x4E2, 0xCEF4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9B67)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    WaitChrThread(0x29, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_7D(0x1, 0x29, 0x0, 0x0)
    Return()

    # Function_58_997E end

    def Function_59_9B99(): pass

    label("Function_59_9B99")

    Sleep(400)
    SetChrFlags(0x3A, 0x20)
    SetChrChipByIndex(0x3A, 30)
    SetChrSubChip(0x3A, 0)

    def lambda_9BB3():
        OP_96(0xFE, 0x113A0, 0x4E2, 0xD570, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9BB3)

    def lambda_9BD1():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_9BD1)
    WaitChrThread(0x3A, 0x1)
    OP_43(0x29, 0x0, 0x1, 0x3A)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_9BF2():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x3A, 2, lambda_9BF2)

    def lambda_9C02():
        OP_8F(0xFE, 0x10E32, 0x4E2, 0xD110, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_9C02)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_59_9B99 end

    def Function_60_9C22(): pass

    label("Function_60_9C22")

    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)
    OP_7D(0x0, 0x2A, 0x14, 0xC8)

    def lambda_9C3A():
        OP_8F(0xFE, 0x11A4E, 0x4E2, 0xCF9E, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9C3A)
    Sleep(100)

    def lambda_9C5A():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_9C5A)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_7D(0x1, 0x2A, 0x0, 0x0)
    SetChrChipByIndex(0x39, 15)
    SetChrSubChip(0x39, 0)
    OP_44(0x39, 0x3)
    OP_8C(0x39, 100, 0)

    def lambda_9CD5():
        OP_9E(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_9CD5)

    def lambda_9CEF():
        OP_8F(0xFE, 0x114A4, 0x4E2, 0xCF9E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9CEF)
    WaitChrThread(0x39, 0x1)
    Return()

    # Function_60_9C22 end

    def Function_61_9D0A(): pass

    label("Function_61_9D0A")


    def lambda_9D10():
        OP_8F(0xFE, 0x11634, 0x4E2, 0xCF9E, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9D10)

    def lambda_9D2B():
        OP_8F(0xFE, 0x11BDE, 0x4E2, 0xCF9E, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9D2B)

    def lambda_9D46():
        OP_9E(0xFE, 0x3C, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_9D46)

    def lambda_9D60():
        OP_9E(0xFE, 0x3C, 0x0, 0x0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9D60)
    WaitChrThread(0x39, 0x1)
    OP_44(0x39, 0x2)
    WaitChrThread(0x2A, 0x1)
    OP_44(0x2A, 0x2)
    OP_22(0xD6, 0x0, 0x64)
    SetChrChipByIndex(0x39, 30)
    SetChrSubChip(0x39, 7)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x2A, 2)
    WaitChrThread(0x2A, 0x2)

    def lambda_9DDA():
        OP_96(0xFE, 0x12386, 0x4E2, 0xCF8A, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9DDA)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)
    OP_7D(0x0, 0x2A, 0x14, 0xC8)

    def lambda_9E14():
        OP_8F(0xFE, 0x11BDE, 0x4E2, 0xCF9E, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9E14)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    OP_7D(0x1, 0x2A, 0x0, 0x0)
    SetChrChipByIndex(0x39, 15)
    WaitChrThread(0x39, 0x0)

    def lambda_9E91():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_9E91)

    def lambda_9EAB():
        OP_8F(0xFE, 0x11314, 0x4E2, 0xCF9E, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9EAB)
    WaitChrThread(0x39, 0x1)
    Sleep(200)

    def lambda_9ED0():
        OP_8C(0xFE, 160, 400)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_9ED0)

    def lambda_9EDE():
        OP_96(0xFE, 0x116E8, 0x4E2, 0xD6EC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9EDE)
    WaitChrThread(0x39, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x39, 30)
    SetChrSubChip(0x39, 3)

    def lambda_9F10():
        OP_99(0xFE, 0x3, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_9F10)

    def lambda_9F20():
        OP_96(0xFE, 0x119AE, 0x4E2, 0xD1A6, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9F20)
    Sleep(100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x39, 1000, 500, -1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    SetChrChipByIndex(0x2A, 27)
    SetChrSubChip(0x2A, 0)
    OP_8C(0x2A, 340, 0)

    def lambda_9F9F():
        OP_9E(0xFE, 0x3C, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_9F9F)

    def lambda_9FB9():
        OP_8F(0xFE, 0x11FEE, 0x4E2, 0xC7A6, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9FB9)
    WaitChrThread(0x2A, 0x1)
    Sleep(200)
    OP_7D(0x0, 0x2A, 0x14, 0xC8)

    def lambda_9FE6():
        OP_8C(0xFE, 250, 400)
        ExitThread()

    QueueWorkItem(0x2A, 3, lambda_9FE6)

    def lambda_9FF4():
        OP_96(0xFE, 0x1255C, 0x4E2, 0xCFDA, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9FF4)
    WaitChrThread(0x2A, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x2A, 3)
    SetChrSubChip(0x2A, 5)

    def lambda_A026():
        OP_8F(0xFE, 0x11D0A, 0x4E2, 0xCFDA, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A026)
    SetChrChipByIndex(0x39, 15)
    WaitChrThread(0x39, 0x0)

    def lambda_A04B():
        OP_8C(0xFE, 70, 400)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_A04B)

    def lambda_A059():
        OP_96(0xFE, 0x112A6, 0x4E2, 0xCFA8, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_A059)
    WaitChrThread(0x2A, 0x1)
    OP_7D(0x1, 0x2A, 0x0, 0x0)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_61_9D0A end

    def Function_62_A084(): pass

    label("Function_62_A084")


    def lambda_A08A():

        label("loc_A08A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A08A")

    QueueWorkItem2(0x43, 0, lambda_A08A)

    def lambda_A09D():

        label("loc_A09D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_A09D")

    QueueWorkItem2(0x44, 0, lambda_A09D)

    def lambda_A0B0():
        OP_8E(0xFE, 0x188E4, 0xFA, 0x7800, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A0B0)
    Sleep(100)

    def lambda_A0D0():
        OP_8E(0xFE, 0x183E4, 0xFA, 0x7D5A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_A0D0)
    Sleep(200)
    OP_8C(0x43, 225, 400)
    WaitChrThread(0x2B, 0x1)
    OP_8C(0x2B, 0, 400)
    SetChrChipByIndex(0x2B, 7)
    WaitChrThread(0x2C, 0x1)
    OP_8C(0x2C, 90, 400)
    SetChrChipByIndex(0x2C, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2B, 0x0, 0x7, 0xBB8)

    def lambda_A15C():
        OP_9E(0x43, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x43, 1, lambda_A15C)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2C, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2B, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2C, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x0, 0x43, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_A279():
        OP_96(0xFE, 0x188F8, 0xFA, 0x7364, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A279)
    Sleep(100)

    def lambda_A29C():
        OP_96(0xFE, 0x17FCA, 0xFA, 0x7D00, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_A29C)
    WaitChrThread(0x2B, 0x1)
    SetChrChipByIndex(0x2B, 5)
    WaitChrThread(0x2C, 0x1)
    SetChrChipByIndex(0x2C, 5)
    OP_83(0x0, 0x2)
    SetChrFlags(0x43, 0x80)
    Return()

    # Function_62_A084 end

    def Function_63_A2D1(): pass

    label("Function_63_A2D1")


    def lambda_A2D7():
        OP_8E(0xFE, 0x1848E, 0xFA, 0x899E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_A2D7)
    Sleep(100)

    def lambda_A2F7():
        OP_8E(0xFE, 0x184C0, 0xFA, 0x8548, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_A2F7)
    Sleep(200)
    WaitChrThread(0x2F, 0x1)
    OP_8C(0x2F, 90, 400)
    SetChrChipByIndex(0x2F, 7)
    WaitChrThread(0x30, 0x1)
    OP_8C(0x30, 90, 400)
    SetChrChipByIndex(0x30, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2F, 0x0, 0x7, 0xBB8)

    def lambda_A37C():
        OP_9E(0x44, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x44, 1, lambda_A37C)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x30, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x2F, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x30, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x2, 0x44, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_A499():
        OP_96(0xFE, 0x180EC, 0xFA, 0x894E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_A499)
    Sleep(100)

    def lambda_A4BC():
        OP_96(0xFE, 0x18146, 0xFA, 0x8552, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_A4BC)
    WaitChrThread(0x2F, 0x1)
    SetChrChipByIndex(0x2F, 5)
    WaitChrThread(0x30, 0x1)
    SetChrChipByIndex(0x30, 5)
    OP_83(0x2, 0x2)
    SetChrFlags(0x44, 0x80)
    Return()

    # Function_63_A2D1 end

    def Function_64_A4F1(): pass

    label("Function_64_A4F1")


    def lambda_A4F7():
        OP_8E(0xFE, 0x17BC4, 0xFA, 0x9178, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A4F7)
    Sleep(100)

    def lambda_A517():
        OP_8E(0xFE, 0x17CB4, 0xFA, 0x8C50, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_A517)
    Sleep(200)
    OP_8C(0x45, 270, 400)
    WaitChrThread(0x33, 0x1)
    OP_8C(0x33, 90, 400)
    SetChrChipByIndex(0x33, 7)
    WaitChrThread(0x34, 0x1)
    OP_8C(0x34, 45, 400)
    SetChrChipByIndex(0x34, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x33, 0x0, 0x7, 0xBB8)

    def lambda_A5A3():
        OP_9E(0x45, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x45, 1, lambda_A5A3)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x34, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x33, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x5, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x34, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x4, 0x45, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_A6C0():
        OP_96(0xFE, 0x178A4, 0x0, 0x91E6, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A6C0)
    Sleep(100)

    def lambda_A6E3():
        OP_96(0xFE, 0x17A48, 0xFA, 0x89B2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x34, 1, lambda_A6E3)
    WaitChrThread(0x33, 0x1)
    SetChrChipByIndex(0x33, 5)
    WaitChrThread(0x34, 0x1)
    SetChrChipByIndex(0x34, 5)
    OP_83(0x4, 0x2)
    SetChrFlags(0x45, 0x80)
    Return()

    # Function_64_A4F1 end

    def Function_65_A718(): pass

    label("Function_65_A718")


    def lambda_A71E():
        OP_8E(0xFE, 0x173E0, 0x0, 0x8110, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_A71E)
    Sleep(100)

    def lambda_A73E():
        OP_8E(0xFE, 0x16E7C, 0x0, 0x85A2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_A73E)
    Sleep(200)
    OP_8C(0x46, 180, 400)
    WaitChrThread(0x38, 0x1)
    OP_8C(0x38, 0, 400)
    SetChrChipByIndex(0x38, 7)
    WaitChrThread(0x37, 0x1)
    OP_8C(0x37, 90, 400)
    SetChrChipByIndex(0x37, 7)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x38, 0x0, 0x7, 0xBB8)

    def lambda_A7CA():
        OP_9E(0x46, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x46, 1, lambda_A7CA)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x7, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x37, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x38, 0x0, 0x7, 0xBB8)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x7, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x37, 0x0, 0x7, 0xBB8)
    PlayEffect(0x1, 0x6, 0x46, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)

    def lambda_A8E7():
        OP_96(0xFE, 0x17426, 0x0, 0x7DD2, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_A8E7)
    Sleep(100)

    def lambda_A90A():
        OP_96(0xFE, 0x16AB2, 0x0, 0x858E, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_A90A)
    WaitChrThread(0x38, 0x1)
    SetChrChipByIndex(0x38, 5)
    WaitChrThread(0x37, 0x1)
    SetChrChipByIndex(0x37, 5)
    OP_83(0x6, 0x2)
    SetChrFlags(0x46, 0x80)
    Return()

    # Function_65_A718 end

    def Function_66_A93F(): pass

    label("Function_66_A93F")

    OP_8E(0x2E, 0x11116, 0xFA, 0xAAE6, 0x1388, 0x0)
    SetChrChipByIndex(0x2E, 3)
    OP_8C(0x2E, 90, 400)
    OP_99(0x2E, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x0, 0x3D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x3D, 17)

    def lambda_A9A8():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_A9A8)
    OP_8C(0x2E, 270, 400)
    OP_99(0x2E, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x1, 0x3E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x3E, 17)

    def lambda_AA02():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_AA02)
    Return()

    # Function_66_A93F end

    def Function_67_AA0D(): pass

    label("Function_67_AA0D")

    OP_8E(0x31, 0x1147C, 0xFA, 0xA79E, 0x1388, 0x0)
    SetChrChipByIndex(0x31, 3)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0x3D, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x31, 0x0, 0x7, 0xBB8)

    def lambda_AA6F():
        OP_9E(0x3D, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3D, 1, lambda_AA6F)
    Return()

    # Function_67_AA0D end

    def Function_68_AA84(): pass

    label("Function_68_AA84")

    OP_8E(0x32, 0x10DCE, 0xFA, 0xA79E, 0x1388, 0x0)
    SetChrChipByIndex(0x32, 3)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x3, 0x3E, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_99(0x32, 0x0, 0x7, 0xBB8)

    def lambda_AAE6():
        OP_9E(0x3E, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3E, 1, lambda_AAE6)
    Return()

    # Function_68_AA84 end

    def Function_69_AAFB(): pass

    label("Function_69_AAFB")

    OP_8E(0x35, 0x117BA, 0xFA, 0xAFDC, 0x1388, 0x0)
    SetChrChipByIndex(0x35, 3)
    OP_8C(0x35, 315, 400)
    OP_99(0x35, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x4, 0x3B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AB5F():
        OP_9E(0x3B, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_AB5F)
    SetChrChipByIndex(0x3B, 17)

    def lambda_AB7E():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_AB7E)
    Return()

    # Function_69_AAFB end

    def Function_70_AB89(): pass

    label("Function_70_AB89")

    OP_8E(0x36, 0x10AF4, 0xFA, 0xB004, 0x1388, 0x0)
    SetChrChipByIndex(0x36, 3)
    OP_8C(0x36, 45, 400)
    OP_99(0x36, 0x0, 0x7, 0xBB8)
    PlayEffect(0x2, 0x5, 0x3C, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_ABED():
        OP_9E(0x3C, 0x1E, 0x0, 0x7D0, 0xFA0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_ABED)
    SetChrChipByIndex(0x3C, 17)

    def lambda_AC0C():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_AC0C)
    Return()

    # Function_70_AB89 end

    def Function_71_AC17(): pass

    label("Function_71_AC17")

    Sleep(200)

    label("loc_AC1C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC3A")
    OP_22(0x13A, 0x0, 0x64)
    Sleep(200)
    OP_23(0x13A)
    Sleep(200)
    Jump("loc_AC1C")

    label("loc_AC3A")

    Return()

    # Function_71_AC17 end

    def Function_72_AC3B(): pass

    label("Function_72_AC3B")

    Sleep(150)

    label("loc_AC40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC60")
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x5A)
    Sleep(300)
    Jump("loc_AC40")

    label("loc_AC60")

    Return()

    # Function_72_AC3B end

    def Function_73_AC61(): pass

    label("Function_73_AC61")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_AC6D")
    Return()

    label("loc_AC6D")

    EventBegin(0x0)
    Fade(500)
    OP_6D(109680, 1500, 33080, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 108790, 1250, 32950, 90)
    SetChrPos(0x105, 107810, 1250, 33760, 90)
    SetChrPos(0x104, 107340, 1250, 32390, 90)
    SetChrPos(0x108, 106280, 1250, 33000, 90)
    OP_0D()

    ChrTalk(    #357
        0x101,
        "#1004FHuh, it's unlocked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x105,
        (
            "#044FThe entrance here should be kept locked as\x01",
            "long as there's no show like the martial\x01",
            "arts tournament.\x02\x03",

            "#042FIn which case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x104,
        "#035FHeh, it seems this is our goal then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x108,
        "#070FAll right, let's get inside.\x02",
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_73_AC61 end

    def Function_74_ADFA(): pass

    label("Function_74_ADFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_AE06")
    Return()

    label("loc_AE06")

    EventBegin(0x0)
    Fade(500)
    OP_6D(109680, 1500, 35580, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 108790, 1250, 35450, 90)
    SetChrPos(0x105, 107810, 1250, 36260, 90)
    SetChrPos(0x104, 107340, 1250, 34890, 90)
    SetChrPos(0x108, 106280, 1250, 35500, 90)
    OP_0D()

    ChrTalk(    #361
        0x101,
        "#1004FHuh, it's unlocked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x105,
        (
            "#044FThe entrance here should be kept locked as\x01",
            "long as there's no show like the Martial\x01",
            "Arts Competition.\x02\x03",

            "#042FIn which case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x104,
        "#035FHeh, it seems this is our goal, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x108,
        "#070FAll right, let's get inside.\x02",
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_74_ADFA end

    def Function_75_AF95(): pass

    label("Function_75_AF95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_AFA1")
    Return()

    label("loc_AFA1")

    EventBegin(0x0)
    Fade(500)
    OP_6D(109680, 1500, 30580, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 108790, 1250, 30450, 90)
    SetChrPos(0x105, 107810, 1250, 31260, 90)
    SetChrPos(0x104, 107340, 1250, 29890, 90)
    SetChrPos(0x108, 106280, 1250, 30500, 90)
    OP_0D()

    ChrTalk(    #365
        0x101,
        "#1004FHuh, it's unlocked?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x105,
        (
            "#044FThe entrance here should be kept locked as\x01",
            "long as there's no show like the Martial\x01",
            "Arts Competition.\x02\x03",

            "#042FIn which case...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x104,
        "#035FHeh, it seems this is our goal, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x108,
        "#070FAll right, let's get inside.\x02",
    )

    CloseMessageWindow()
    OP_28(0xC4, 0x1, 0x100)
    EventEnd(0x0)
    Return()

    # Function_75_AF95 end

    SaveToFile()

Try(main)
