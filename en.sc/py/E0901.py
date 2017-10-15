from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0901   ._SN',
        MapName             = 'Event',
        Location            = 'E0901.x',
        MapIndex            = 1,
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
        'Boat',                                 # 9
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
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT07/CH00023 ._CH',             # 01
        'ED6_DT07/CH00053 ._CH',             # 02
        'ED6_DT07/CH00033 ._CH',             # 03
        'ED6_DT07/CH00043 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
        'ED6_DT07/CH00073 ._CH',             # 06
        'ED6_DT27/CH03083 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT07/CH00023P._CP',             # 01
        'ED6_DT07/CH00053P._CP',             # 02
        'ED6_DT07/CH00033P._CP',             # 03
        'ED6_DT07/CH00043P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
        'ED6_DT07/CH00073P._CP',             # 06
        'ED6_DT27/CH03083P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_119",          # 01, 1
        "Function_2_11A",          # 02, 2
        "Function_3_1AF1",         # 03, 3
        "Function_4_1B27",         # 04, 4
        "Function_5_1B7D",         # 05, 5
        "Function_6_1C06",         # 06, 6
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_118")
    OP_A3(0x10F0)
    Event(0, 2)

    label("loc_118")

    Return()

    # Function_0_10A end

    def Function_1_119(): pass

    label("Function_1_119")

    Return()

    # Function_1_119 end

    def Function_2_11A(): pass

    label("Function_2_11A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131")
    Call(0, 5)
    Call(0, 6)

    label("loc_131")

    FadeToDark(0, 0, -1)
    OP_76(0xFF, 0x0, 0x1, 0x2, 0x1, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0x0, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_6D(1210, -2990, -360, 0)
    OP_67(0, 7400, -10000, 0)
    OP_6B(4550, 0)
    OP_6C(271000, 0)
    OP_6E(370, 0)
    OP_A1(0x8, 0x0)
    SetChrPos(0x8, -28690, -2850, 20660, 305)
    OP_48()
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x109, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_89(0x101, -27480, -2750, 20350, 125)
    OP_89(0x109, -27880, -2750, 19880, 125)
    OP_89(0xF8, -28750, -2750, 21200, 125)
    OP_89(0xF9, -29110, -2750, 20650, 125)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x109, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x109, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_280")
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 1)

    label("loc_280")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_298")
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 2)

    label("loc_298")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 3)

    label("loc_2B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C8")
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 4)

    label("loc_2C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E0")
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 5)

    label("loc_2E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F8")
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 6)

    label("loc_2F8")

    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)
    LoadEffect(0x1, "map\\\\mp013_00.eff")
    LoadEffect(0x2, "map\\\\mp013_01.eff")
    PlayEffect(0x1, 0x1, 0x8, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x8, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x1CC, 0x0, 0x64)
    OP_22(0xDA, 0x1, 0x4B)
    Sleep(2000)

    def lambda_3B6():
        OP_8F(0xFE, 0x0, 0xFFFFF4DE, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_3B6)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_3DB():
        OP_6B(3200, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DB)
    WaitChrThread(0x8, 0x0)
    OP_44(0x101, 0x0)
    Fade(1000)
    OP_6D(330, -2830, -510, 0)
    OP_67(0, 8550, -10000, 0)
    OP_6B(3340, 0)
    OP_6C(180000, 0)
    OP_6E(229, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    OP_89(0x101, 1050, -2750, -300, 125)
    OP_89(0x109, 620, -2750, -850, 125)
    OP_89(0xF8, -50, -2750, 450, 125)
    OP_89(0xF9, -500, -2750, 0, 125)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#1003F#6PHmmm. Sure is quiet...\x02\x03",

            "#1002FYou'd think we'd be able to see\x01",
            "the beach soon or something.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FD():
        OP_67(0, 6500, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FD)

    def lambda_515():
        OP_6B(3050, 13000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_515)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AE")

    ChrTalk(    #1
        0x108,
        (
            "#074F#4PMm. We should be moving in the right\x01",
            "direction, I think.\x02\x03",

            "#070FThere is little need to worry.\x01",
            "We will get there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE")

    label("loc_5AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_628")

    ChrTalk(    #2
        0x106,
        (
            "#053F#4PWe should be goin' in the right direction.\x02\x03",

            "#050FBest thing to do now is just plow forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE")

    label("loc_628")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B0")

    ChrTalk(    #3
        0x103,
        (
            "#026F#4PUnless I'm off, we should be going in\x01",
            "the right direction.\x02\x03",

            "#020FWe'll get there eventually.\x01",
            "Don't worry.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE")

    label("loc_6B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(    #4
        0x104,
        (
            "#035F#4PUnless my skill at reading maps has fled me,\x01",
            "this is the right direction.\x02\x03",

            "#030FOur best course of action is to proceed\x01",
            "forward.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CE")

    label("loc_74F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CE")

    ChrTalk(    #5
        0x105,
        (
            "#542F#4PThis should be the right direction,\x01",
            "I think.\x02\x03",

            "We should reach land if we keep going\x01",
            "on this course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CE")

    Sleep(100)
    SetChrSubChip(0x109, 2)
    Sleep(400)

    ChrTalk(    #6
        0x109,
        (
            "#1062F#6PAhhhh, besides, check out that moon!\x02\x03",

            "#1061FThis is the sort of night you'd want to\x01",
            "take a girlfriend out on a date, really.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 2)
    Sleep(400)

    ChrTalk(    #7
        0x101,
        (
            "#1007F#6PAnd SOMEONE'S as mellowed out as ever...\x02\x03",

            "#1008FBut, do you actually have a girlfriend,\x01",
            "Kevin?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x109, 1)
    Sleep(400)

    ChrTalk(    #8
        0x109,
        (
            "#1071F#4PHeh! Despite what you might think, I have\x01",
            "at least one candidate in each town on\x01",
            "the continent, and--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1028F#6PCandidate.\x01",
            "Meaning you don't actually have one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x109,
        "#1068F#4PC'mon...at least let me FINISH braggin'!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A01")

    ChrTalk(    #11
        0x105,
        "#045F#4PHahaha...\x02",
    )

    CloseMessageWindow()

    label("loc_A01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A26")

    ChrTalk(    #12
        0x107,
        "#061F#4PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_A26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A49")

    ChrTalk(    #13
        0x103,
        "#027F#4POh, my.\x02",
    )

    CloseMessageWindow()

    label("loc_A49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A93")

    ChrTalk(    #14
        0x104,
        (
            "#035F#4PHeh, you are but a squire in love,\x01",
            "sir knight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A93")


    ChrTalk(    #15
        0x101,
        (
            "#1015F#6PThough... Kevin, why ARE you out here on\x01",
            "your own still?\x02\x03",

            "This is becoming kind of a big deal and\x01",
            "you have no backup, aside from us. Are\x01",
            "the Gralsritter kind of understaffed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1067F#4PWell, the situation's kinda...complicated.\x02\x03",

            "#1065FI got dispatched out here on my own at first,\x01",
            "yeah.\x02\x03",

            "#1060FIf stuff REALLY hits the rotating thingamajigger,\x01",
            "though, some of my buddies might fly out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1004F#6POh, okay.\x02\x03",

            "#1015FEr, so, the Gralsritter's job is\x01",
            "the retrieval of artifacts, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1060F#4PMore accurately, investigation, management\x01",
            "AND retrieval.\x02\x03",

            "And 'retrieval' usually means recovering it\x01",
            "from someone.\x02\x03",

            "#1065FThe church has forbidden the average\x01",
            "citizen from owning working artifacts,\x01",
            "and most nations agree and let us work.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DF1")

    ChrTalk(    #19
        0x107,
        (
            "#064F#4PUm, I'm curious, why does the church want\x01",
            "to take them away so badly?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E52")

    label("loc_DF1")


    ChrTalk(    #20
        0x101,
        (
            "#1004F#6PBut what's with all the locking down?\x01",
            "Seems like a lot of effort for old machines.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E52")


    ChrTalk(    #21
        0x109,
        (
            "#1063F#4POkay, so, thing is, there's lots and lots\x01",
            "of different types of artifacts, right?\x02\x03",

            "And nobody really knows how or why they\x01",
            "work yet.\x02\x03",

            "#1065FDespite that, they DO work, and depending\x01",
            "on how you use 'em, they can have\x01",
            "absolutely crazy abilities.\x02\x03",

            "#1067FWhat do you think tends to happen when you\x01",
            "put infinite cosmic power in the hands\x01",
            "of your average citizen?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF8")

    ChrTalk(    #22
        0x107,
        "#063F#4PUm... What happens?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1023")

    label("loc_FF8")


    ChrTalk(    #23
        0x101,
        "#1015F#6PI, uh, can guess...but what?\x02",
    )

    CloseMessageWindow()

    label("loc_1023")


    ChrTalk(    #24
        0x109,
        (
            "#1063F#4PThe biggest thing is actually obsession.\x02\x03",

            "They can't resist the seduction of power\x01",
            "and inevitably use the artifact for...\x01",
            "nothing good.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E0")

    ChrTalk(    #25
        0x107,
        "#065F#4PN-No way...\x02",
    )

    CloseMessageWindow()

    label("loc_10E0")


    ChrTalk(    #26
        0x101,
        "#1002F#6PSeriously? Always?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1065F#4PWe've seen it happen time and time again\x01",
            "throughout history, sadly enough.\x02\x03",

            "#1063FEstelle, you remember Mayor Dalmore well\x01",
            "enough to know what I'm talkin' about, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1296")

    ChrTalk(    #28
        0x101,
        "#1020F#6PEr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#049F#4PIt's true, Mayor Dalmore did seem terribly\x01",
            "cruel when he showed his true face to us.\x02\x03",

            "He seemed like a man who had cast aside\x01",
            "anything we would consider moral restraint...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1368")

    label("loc_1296")


    ChrTalk(    #30
        0x101,
        (
            "#1020F#6PEr...\x02\x03",

            "#1007FYeah, Dalmore did seem to have this\x01",
            "awful mean streak in him.\x02\x03",

            "It wasn't like that mind-controlled Capua\x01",
            "boss guy. Dalmore seemed like he felt he\x01",
            "could fight the whole world and win.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1368")


    ChrTalk(    #31
        0x109,
        (
            "#1065F#4PHolding absolute power gives people a warped\x01",
            "sort of confidence, erases their ability\x01",
            "to control themselves...\x02\x03",

            "#1060FIt's the mission of the Gralsritter to\x01",
            "stop that before it happens.\x02\x03",

            "#1068FAin't always the prettiest job in the\x01",
            "world, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        "#1004F#6PR-Really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1674")

    ChrTalk(    #33
        0x104,
        (
            "#035F#4PIt simply means the church has its own\x01",
            "business, Estelle.\x02\x03",

            "#030FFor example, in some cases individuals are\x01",
            "allowed to possess or keep artifacts,\x01",
            "are they not?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_155C")

    ChrTalk(    #34
        0x103,
        "#027F#4P...\x02",
    )

    CloseMessageWindow()

    label("loc_155C")


    ChrTalk(    #35
        0x109,
        (
            "#1064F#6P...Man, you DO know a lot.\x02\x03",

            "#1071FWell, I'm gonna have to say 'no comment'\x01",
            "on that one, Mr. Bard.\x02\x03",

            "Got a duty to keep Church business confidential\x01",
            "and all that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x104,
        "#035F#4PHeh. Of course, my good man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1019F#6PUrge...to push Kevin off the boat...rising...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1724")

    label("loc_1674")


    ChrTalk(    #38
        0x109,
        (
            "#1062F#4PHey, even the Bracer Guild has stuff\x01",
            "they can't talk about publicly, right?\x02\x03",

            "It's not any different than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        "#1007F#6POh, uh, well... You've got me there.\x02",
    )

    CloseMessageWindow()

    label("loc_1724")


    def lambda_172A():
        OP_6E(315, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_172A)
    OP_43(0x8, 0x2, 0x0, 0x4)
    Sleep(1000)
    StopSound(0x3E8, 0xEA60, 0x1F40)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)
    OP_20(0x7D0)
    OP_82(0x80, 0x2)
    OP_82(0x81, 0x2)
    OP_82(0x82, 0x2)
    Sleep(100)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    SetChrSubChip(0x101, 0)
    Sleep(400)

    ChrTalk(    #40
        0x101,
        "#1005F#6PHey...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1845")

    ChrTalk(    #41
        0x103,
        (
            "#022F#4PI would bet this means we're\x01",
            "close to their base.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197A")

    label("loc_1845")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_189C")

    ChrTalk(    #42
        0x106,
        (
            "#057F#4PLand frickin' ho, it looks like,\x01",
            "judgin' from this soup.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197A")

    label("loc_189C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18E1")

    ChrTalk(    #43
        0x108,
        "#072F#4PI suspect we're close to their base...\x02",
    )

    CloseMessageWindow()
    Jump("loc_197A")

    label("loc_18E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192D")

    ChrTalk(    #44
        0x107,
        (
            "#065F#4PSo this is the fog near their base,\x01",
            "right...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_197A")

    label("loc_192D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197A")

    ChrTalk(    #45
        0x105,
        (
            "#042F#4PWe must be drawing close to\x01",
            "the Ouroboros base...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197A")

    Sleep(500)
    OP_21()
    OP_1D(0x7D)
    Sleep(1000)

    ChrTalk(    #46
        0x109,
        (
            "#1063F#4PNow we really got no choice\x01",
            "but to plow on ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1002F#6PYeah...\x02\x03",

            "Stay alert, everyone.\x01",
            "They might try to ambush us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_43(0x8, 0x3, 0x0, 0x3)
    StopSound(0x3E8, 0x7530, 0x7D0)

    def lambda_1A30():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A30)
    Sleep(500)

    def lambda_1A4B():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A4B)
    Sleep(400)

    def lambda_1A66():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A66)
    Sleep(300)

    def lambda_1A81():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A81)
    Sleep(200)

    def lambda_1A9C():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A9C)
    Sleep(100)

    def lambda_1AB7():
        OP_94(0x1, 0xFE, 0xB4, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1AB7)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_82(0x0, 0x2)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_11A end

    def Function_3_1AF1(): pass

    label("Function_3_1AF1")

    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x15E)
    OP_73(0x0)
    OP_72(0x0, 0x20)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 301)
    OP_70(0x0, 0x168)
    Return()

    # Function_3_1AF1 end

    def Function_4_1B27(): pass

    label("Function_4_1B27")

    OP_22(0x1C3, 0x1, 0x64)
    Sleep(3000)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x5A)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    Sleep(200)
    OP_23(0x1C3)
    Return()

    # Function_4_1B27 end

    def Function_5_1B7D(): pass

    label("Function_5_1B7D")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BF9"),
        (1, "loc_1BFF"),
        (SWITCH_DEFAULT, "loc_1C05"),
    )


    label("loc_1BF9")

    OP_A2(0x1200)
    Jump("loc_1C05")

    label("loc_1BFF")

    OP_A2(0x1201)
    Jump("loc_1C05")

    label("loc_1C05")

    Return()

    # Function_5_1B7D end

    def Function_6_1C06(): pass

    label("Function_6_1C06")

    ClearMapFlags(0x1)
    OP_6D(15460, -2990, 171130, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_6_1C06 end

    SaveToFile()

Try(main)
