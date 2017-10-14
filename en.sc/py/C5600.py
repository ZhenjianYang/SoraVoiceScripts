from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5600   ._SN',
        MapName             = 'Other',
        Location            = 'C5600.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'Campanella',                           # 9
        'Loewe',                                # 10
        'Weissmann',                            # 11
        'Renne',                                # 12
        'Airship',                              # 13
        'Pater-Mater',                          # 14
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
        'ED6_DT29/CH12000 ._CH',             # 04
        'ED6_DT29/CH12001 ._CH',             # 05
        'ED6_DT29/CH12000 ._CH',             # 06
        'ED6_DT29/CH12001 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12001 ._CH',             # 09
        'ED6_DT27/CH03600 ._CH',             # 0A
        'ED6_DT07/CH02040 ._CH',             # 0B
        'ED6_DT27/CH03550 ._CH',             # 0C
        'ED6_DT27/CH03510 ._CH',             # 0D
        'ED6_DT26/CH20295 ._CH',             # 0E
        'ED6_DT26/CH20305 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
        'ED6_DT29/CH12000P._CP',             # 04
        'ED6_DT29/CH12001P._CP',             # 05
        'ED6_DT29/CH12000P._CP',             # 06
        'ED6_DT29/CH12001P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12001P._CP',             # 09
        'ED6_DT27/CH03600P._CP',             # 0A
        'ED6_DT07/CH02040P._CP',             # 0B
        'ED6_DT27/CH03550P._CP',             # 0C
        'ED6_DT27/CH03510P._CP',             # 0D
        'ED6_DT26/CH20295P._CP',             # 0E
        'ED6_DT26/CH20305P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 9520,
        TriggerZ            = 9000,
        TriggerY            = 6150,
        TriggerRange        = 1000,
        ActorX              = 9960,
        ActorZ              = 9000,
        ActorY              = 6600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_252",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_299",          # 03, 3
        "Function_4_4B5",          # 04, 4
        "Function_5_1B0B",         # 05, 5
        "Function_6_343B",         # 06, 6
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_244")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 5)
    Jump("loc_251")

    label("loc_244")

    Event(0, 4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_251")

    Return()

    # Function_0_22E end

    def Function_1_252(): pass

    label("Function_1_252")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFE3AE0, 0x230073)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B")
    OP_6F(0x1, 0)
    Jump("loc_282")

    label("loc_27B")

    OP_6F(0x1, 60)

    label("loc_282")

    Return()

    # Function_1_252 end

    def Function_2_283(): pass

    label("Function_2_283")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_283")

    label("loc_298")

    Return()

    # Function_2_283 end

    def Function_3_299(): pass

    label("Function_3_299")

    OP_EA(0x2, 0x9E, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_371")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E9, 1)"), scpexpr(EXPR_END)), "loc_30A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xE9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D28)
    Jump("loc_36E")

    label("loc_30A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xE9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_36E")

    Jump("loc_426")

    label("loc_371")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Inside is a single piece of paper. It's a teaser for\x01",
            "a brand new game called 'Trails in the Chest.'\x01",
            "It looks boring. You put the paper down and leave.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_426")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x43)"), scpexpr(EXPR_END)), "loc_445")
    Jump("loc_4AC")

    label("loc_445")


    AnonymousTalk(    #3
        (
            "\x07\x00Found a scrap of paper with a [ #489i ]\x01",
            "recipe written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x07\x00Learned [ #489i ] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_4AC")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_299 end

    def Function_4_4B5(): pass

    label("Function_4_4B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    OP_6D(2380, 30000, -14320, 0)
    OP_67(0, 10010, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(340000, 0)
    OP_6E(730, 0)
    OP_11(0xA0, 0xB4, 0xFF, 0x3A98, 0x30D40, 0x0)
    SetChrPos(0x101, -26000, 18450, 11200, 180)
    SetChrPos(0x8, -26000, 18450, 11200, 180)
    OP_A1(0xC, 0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 700)
    OP_70(0x0, 0x30C)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, 21380, 20000, -38500, 0)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x3E8, 0x2710, 0x1)

    def lambda_589():
        OP_6C(330000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_589)

    def lambda_599():
        OP_67(0, 12010, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_599)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5 op#A
        "\x07\x05#50AMeanwhile - Liberl Kingdom, Location Unknown\x02",
    )

    Sleep(100)
    FadeToBright(1000, 0)
    Sleep(3000)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    OP_22(0x79, 0x0, 0x64)
    Fade(1000)
    OP_44(0x8, 0xFF)
    OP_6D(-31780, 30000, -16820, 0)
    OP_67(0, 8060, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(59000, 0)
    OP_6E(697, 0)
    OP_0D()

    def lambda_66D():
        OP_6D(-31780, 25000, 5000, 5000)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_66D)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x57E4, 0x3E80, 0x1)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x57E4, 0x3A98, 0x1)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x57E4, 0x36B0, 0x1)
    OP_97(0xC, 0x4B6E, 0x4A6, 0x4E20, 0x32C8, 0x1)
    OP_8C(0xC, 0, 400)
    SetChrFlags(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    OP_51(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x1ADB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_72(0x0, 0x20)
    OP_6F(0x0, 780)
    OP_70(0x0, 0x320)
    OP_73(0x0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 800)
    OP_70(0x0, 0x384)

    def lambda_740():
        OP_8F(0xFE, 0xFFFF9B38, 0x3B2E, 0x2E90, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_740)
    Sleep(1500)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xC, 0x1)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_82(0x1, 0x2)
    OP_6F(0x0, 1000)
    OP_70(0x0, 0x41A)
    OP_73(0x0)
    Sleep(200)
    OP_6F(0x0, 1050)
    OP_70(0x0, 0x456)
    OP_73(0x0)
    OP_23(0x79)
    OP_23(0xCC)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Fade(1000)
    OP_6D(-13700, 30000, 8590, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(296000, 0)
    OP_6E(409, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 1110)
    OP_70(0x0, 0x474)
    OP_73(0x0)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 1140)
    OP_70(0x0, 0x4B0)
    Sleep(200)
    OP_22(0xFD, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    SetChrBattleFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x80)
    StopSound(0xEA60, 0x30D40, 0x1770)

    def lambda_886():
        OP_6D(-25090, 15200, -1540, 6000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_886)

    def lambda_89E():
        OP_67(0, 11430, -18000, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89E)

    def lambda_8B6():
        OP_6B(2090, 6000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8B6)

    def lambda_8C6():
        OP_6C(0, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_8C6)

    def lambda_8D6():
        OP_6E(230, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8D6)
    OP_8E(0x8, 0xFFFF9CE6, 0x3A98, 0xFFFFFA38, 0x7D0, 0x0)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    Sleep(500)

    NpcTalk(    #6
        0x8,
        "Strange Kid",
        (
            "#6P#850FOh, what a lovely little hideaway.\x02\x03",

            "#6PThe professor's taste remains excellent\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -16600, 15000, 4170, 237)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #7
        0x9,
        "Man's Voice",
        "#3PYou're late, Campanella.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A06():
        OP_6D(-21040, 15200, 1680, 2000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A06)

    def lambda_A1E():
        OP_6B(2300, 2000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A1E)
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)

    def lambda_A3F():
        OP_92(0x9, 0x8, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_A3F)
    Sleep(500)

    def lambda_A59():
        OP_69(0x8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_A59)

    def lambda_A67():
        OP_6C(270000, 4000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A67)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x9, 0x0)
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(    #8
        0x8,
        (
            "#851FWhy, Mr. Bladelord, hello!\x01",
            "It's been SO very long.\x02\x03",

            "The last six months were so\x01",
            "dreadfully dreary without you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#124F#4PHmph. I doubt you mean that.\x02\x03",

            "#123FI understand you handled the attacks\x01",
            "on those Bracer Guilds in Erebonia?\x02\x03",

            "You must have enjoyed playing\x01",
            "with Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#850FAwww, you heard about that already?\x01",
            "There goes half my fun.\x02\x03",

            "#851FBut oh, yes, the man was incredible.\x02\x03",

            "There's no way he could have known about\x01",
            "me, and yet he always managed to put\x01",
            "together a proper counter to everything I did.\x02\x03",

            "As a result, I...broke one of our jaeger\x01",
            "corps, I'm afraid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        (
            "#124F#4PYou 'broke' Jester, huh?\x02\x03",

            "#120FI did train them to some degree,\x01",
            "but normal men do have their limits.\x02\x03",

            "I suppose throwing them up against\x01",
            "the Divine Blade was too much to ask\x01",
            "of such men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#853FBut, hey. I managed to keep him tied up\x01",
            "until your little sabotage mission was\x01",
            "completed, so all's well that ends well.\x02\x03",

            "#850FOooh, wait. I'm sorry, you were looking\x01",
            "forward to having fun with him yourself,\x01",
            "weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x9,
        (
            "#123F#4PHm... A little.\x02\x03",

            "#124FBut the blade has been bound\x01",
            "by the chains of duty.\x02\x03",

            "There's no longer any hope of\x01",
            "stopping us through official means.\x01",
            "He is no longer a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#850FHeheh. Looks like the professor's\x01",
            "plan succeeded brilliantly.\x02\x03",

            "The other members are already in\x01",
            "Liberl, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#120F#4PYes, we all conferred for the\x01",
            "first time yesterday.\x02\x03",

            "#124FBleublanc has apparently been\x01",
            "here for a while, however.\x02\x03",

            "'The Phantom Thief,' 'The Direwolf,'\x01",
            "'The Bewitching Bell,' and 'The Angel\x01",
            "of Slaughter'...\x02\x03",

            "#123FAll of them powerful...and not a\x01",
            "normal one in the lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#851FHaha... Mind you, you're not exactly\x01",
            "one to be talking on that score, hmm?\x02\x03",

            "#854FOooh, speaking of the hopelessly\x01",
            "crazy, what about HIM? Is he still\x01",
            "playing hard to get?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "#120F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#854FHaha! This is going to be SO much fun.\x02\x03",

            "Out of all the Enforcers, he's the finest\x01",
            "undercover operative we have...well, had.\x02\x03",

            "I wonder how long he can evade the sight\x01",
            "of the Bladelord and the Faceless?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x9,
        (
            "#121F#4PMm.\x02\x03",

            "#124FIn his heart, he abandoned the\x01",
            "society years ago...with all that\x01",
            "entails.\x02\x03",

            "I doubt he'll be able to pose any\x01",
            "real threat.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xA, -17000, 15200, 8000, 226)
    ClearChrFlags(0xA, 0x80)

    NpcTalk(    #20
        0xA,
        "Man's Voice",
        "#1PNow, I'm not sure I'd say that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x9, 0xA, 500)
    Sleep(500)
    Fade(1000)
    OP_6D(-20220, 15200, 2810, 0)
    OP_67(0, 11430, -18000, 0)
    OP_6B(2390, 0)
    OP_6C(0, 0)
    OP_6E(230, 0)
    SetChrPos(0xA, -18440, 15000, 4740, 229)
    SetChrPos(0x9, -24430, 15000, 240, 41)
    SetChrPos(0x8, -24930, 15000, -1890, 24)

    def lambda_13FB():

        label("loc_13FB")

        TurnDirection(0x9, 0xA, 500)
        OP_48()
        Jump("loc_13FB")

    QueueWorkItem2(0x9, 1, lambda_13FB)
    TurnDirection(0x8, 0xA, 500)

    def lambda_1413():
        OP_6D(-23900, 15000, -700, 3000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1413)
    OP_8E(0xA, 0xFFFFA4FC, 0x3A98, 0xFFFFFE48, 0x7D0, 0x0)
    OP_0D()
    WaitChrThread(0xA, 0x1)
    Sleep(500)

    ChrTalk(    #21
        0xA,
        (
            "#4P#1150FHello, Campanella.\x01",
            "Good of you to come all this way.\x02\x03",

            "You have my sincere thanks for\x01",
            "your excellent work in delaying\x01",
            "Cassius Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#851F#6PHaha... It was no trouble.\x01",
            "It was a fun bit of work, in fact.\x02\x03",

            "#850FSpeaking of fun, though, I must say,\x01",
            "I've taken a look at your plan...\x02\x03",

            "It seems like you're preparing to\x01",
            "have quite a LOT of 'fun.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xA,
        (
            "#4P#1151FWell, well! Such praise from the Fool!\x01",
            "I'm flattered.\x02\x03",

            "I think you'll find it to be even more\x01",
            "enjoyable in practice.\x02\x03",

            "Compounding your delight will be the\x01",
            "fact that everyone participating is pursuing\x01",
            "their own individual goals as well.\x02\x03",

            "Myself included, of course. Even our\x01",
            "fine silver-haired friend here has his own\x01",
            "plans in mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        (
            "#124F#6P...I won't deny it.\x02\x03",

            "#121FI'll kindly ask you not to imply anything\x01",
            "about my loyalty, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xA,
        (
            "#4P#1154FNow, now, it was simply\x01",
            "a jest. Nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#851F#6POoh, I seeee. There's more than\x01",
            "meets the eye, here. I do so love\x01",
            "such games.\x02\x03",

            "#854FWell, either way, your bad taste\x01",
            "has a special kind of artistry to it,\x01",
            "Professor.\x02\x03",

            "As for me...I'm going to make sure\x01",
            "I enjoy myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xA,
        (
            "#4P#1151FCome now, bad taste? You wound\x01",
            "me.\x02\x03",

            "Regardless, you're free to watch the\x01",
            "plan unfold to your heart's content.\x02\x03",

            "You are, after all, a representative\x01",
            "of the Grandmaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "#851F#6POh, I intend to.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_44(0x9, 0xFF)
    OP_8C(0x9, 187, 0)
    OP_8C(0xA, 235, 0)
    OP_6D(-25190, 15200, -2240, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(3640, 0)
    OP_6C(215000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_99(0x8, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #29
        0x8,
        (
            "#853F#5PAnd so Enforcer No. 0, Campanella the Fool,\x01",
            "enters the audience.\x02\x03",

            "#854FWell, Weissmann. I shall enjoy\x01",
            "watching the Anguis' 'Gospel Plan'\x01",
            "unfold...to the very end.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    Sleep(300)
    OP_24(0x1C5, 0x5A)
    Sleep(300)
    OP_24(0x1C5, 0x50)
    Sleep(300)
    OP_24(0x1C5, 0x46)
    Sleep(300)
    OP_24(0x1C5, 0x3C)
    Sleep(300)
    OP_24(0x1C5, 0x32)
    Sleep(300)
    OP_24(0x1C5, 0x28)
    Sleep(300)
    OP_24(0x1C5, 0x1E)
    Sleep(300)
    OP_24(0x1C5, 0x14)
    Sleep(300)
    OP_24(0x1C5, 0xA)
    Sleep(300)
    OP_24(0x1C5, 0x0)
    OP_21()
    Sleep(1000)
    NewScene("ED6_DT21/T5200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_4B5 end

    def Function_5_1B0B(): pass

    label("Function_5_1B0B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B1E")
    Call(0, 6)

    label("loc_1B1E")

    OP_71(0x0, 0x4)
    OP_6D(-13460, 15200, -850, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(6010, 0)
    OP_6C(0, 0)
    OP_6E(598, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x8, -26000, 18450, 11200, 180)
    OP_A1(0xD, 0x2)
    OP_71(0x2, 0x20)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 501)
    OP_70(0x2, 0x208)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    OP_CF(0xB, 0x2, "Frame85__ren")
    OP_8C(0xB, 180, 0)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, 21380, 20000, -38500, 0)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x3E8, 0x2710, 0x1)

    def lambda_1BFE():
        OP_6D(-23730, 15200, 7580, 10000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BFE)

    def lambda_1C16():
        OP_67(0, 7830, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C16)

    def lambda_1C2E():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C2E)

    def lambda_1C3E():
        OP_6B(4200, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C3E)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0x79, 0x0, 0x64)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x57E4, 0x3E80, 0x1)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x57E4, 0x3A98, 0x1)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x57E4, 0x36B0, 0x1)
    OP_97(0xD, 0x4B6E, 0x4A6, 0x4E20, 0x32C8, 0x1)
    OP_8C(0xD, 0, 400)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x1E1)

    def lambda_1CD4():
        OP_8F(0xFE, 0xFFFF9B38, 0x4E20, 0x2E90, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CD4)
    Sleep(1500)
    WaitChrThread(0xD, 0x1)
    OP_8C(0xD, 90, 50)
    Fade(1000)
    OP_6D(-27510, 15200, 10990, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x1)
    SetChrPos(0xD, -24960, 18450, 7270, 90)

    def lambda_1D5D():
        OP_8F(0xFE, 0xFFFF9F20, 0x3BC4, 0x1C34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1D5D)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 421)
    OP_70(0x2, 0x1CC)
    OP_0D()
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0xD, 0x1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xFA0, 0x1F4)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 421)
    OP_23(0x79)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xB, 0x1)
    Sleep(500)

    ChrTalk(    #30
        0xB,
        (
            "#260FHooray! Those silly little flying machines\x01",
            "were no match for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xB,
        (
            "#260FThanks, Pater-Mater! You go sleep for a\x01",
            "bit, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xD,
        "#4P...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -12840, 14800, 9830, 270)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #33
        0x9,
        "Man's Voice",
        "#1PWelcome back, Renne.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1EB4():
        OP_6D(-20330, 15200, 9930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EB4)
    Sleep(500)

    def lambda_1ED1():
        OP_8E(0xFE, 0xFFFFC252, 0x3B60, 0x23D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_1ED1)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x2)
    OP_8C(0xB, 180, 400)
    WaitChrThread(0x9, 0x0)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #34
        0xB,
        "#260FLoewe!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x2)
    OP_CF(0xB, 0x2, "Frame86__ren")
    OP_8C(0xB, 90, 0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0xB, 0xFFFFAFC4, 0x3B60, 0x240E, 0x258, 0x5DC)
    SetChrFlags(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_1F67():
        OP_8E(0xFE, 0xFFFFBCB2, 0x3B60, 0x2350, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1F67)

    def lambda_1F82():
        OP_6D(-16620, 15200, 9110, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F82)

    def lambda_1F9A():
        OP_67(0, 5290, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F9A)

    def lambda_1FB2():
        OP_6B(3420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FB2)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #35
        0xB,
        (
            "#260FI'm back, I'm back!\x02\x03",

            "I went and did that experiment,\x01",
            "just like you asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#120FI know. You did a very good job.\x02\x03",

            "You got a little creative with it, too.\x01",
            "A 'tea party'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xB,
        (
            "#260FIt's 'cause you told me not to kill\x01",
            "anyone this time.\x02\x03",

            "I had to do SOMETHING to make it\x01",
            "a little less boring, and I thought a\x01",
            "tea party would be lots of fun.\x02\x03",

            "And it was! We had tea and crumpets\x01",
            "and explosions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#120FHow...ladylike, Renne.\x02\x03",

            "So, how did the experiment itself go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xB,
        (
            "#260FI think it went okay.\x02\x03",

            "That mean guy from the church kinda\x01",
            "spoiled it with a nasty trick...\x02\x03",

            "But it was fine, otherwise! We can use\x01",
            "them in real combat if we want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "#120FVery good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xB,
        (
            "#260FI thought we couldn't make lots of\x01",
            "Gospels, though.\x02\x03",

            "How are we gonna use them as\x01",
            "weapons if we can't?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        (
            "#120FMass production of them isn't necessary.\x02\x03",

            "These tests are simply to determine the\x01",
            "full capabilities of the Gospels.\x02\x03",

            "We aren't trying to make a weapon out\x01",
            "of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "#260FReally?\x02\x03",

            "Well, whatever. Doesn't matter to me\x01",
            "either way.\x02\x03",

            "Have you found Joshua yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "#120FI think we have.\x02\x03",

            "A number of the dolls we sent out to\x01",
            "act as a diversion were destroyed.\x02\x03",

            "It's very likely he's responsible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xB,
        (
            "#260FSo he's still hiding? Aww.\x02\x03",

            "I'm good at playing hide and seek, but\x01",
            "even I'm not as good as Joshua...\x02\x03",

            "Mmmmmm, I hate this!\x02\x03",

            "Why's he being so stubborn? Why can't\x01",
            "he just come back home to the society?\x01",
            "To us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        "#120FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xB,
        (
            "#260FIt's weird, too. The professor said it's\x01",
            "all Estelle's fault Joshua won't come\x01",
            "back.\x02\x03",

            "But she told me she's been looking for\x01",
            "Joshua, too!\x02\x03",

            "Why would she say that if she's keeping\x01",
            "Joshua from coming back to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#120F...Renne.\x02\x03",

            "I wouldn't be so quick to accept everything\x01",
            "the professor says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        "#260FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "#120FTruth can change depending on one's\x01",
            "perspective.\x02\x03",

            "Just as how people can see different\x01",
            "shapes on the same moon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xB,
        (
            "#260FYou mean like how some people see\x01",
            "a face and others see a crab?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "#120FThat's right.\x02\x03",

            "The professor's truth may be different\x01",
            "from your truth.\x02\x03",

            "You need to reach for your own truth\x01",
            "based on what you yourself see and\x01",
            "feel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xB,
        (
            "#260FUm... Sounds confusing, but I think I get it.\x02\x03",

            "I really like Estelle! I liked everyone, actually.\x01",
            "They're nice, and they gave me snacks.\x01",
            "Tita was fun to play with, too.\x02\x03",

            "I don't even feel like murdering them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#120FVery good.\x02\x03",

            "You're a good girl, Renne.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x9, 0xFFFFBF28, 0x3B60, 0x2364, 0x7D0, 0x0)
    Fade(250)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 14)
    SetChrSubChip(0x9, 0)
    OP_0D()
    OP_99(0x9, 0x0, 0x2, 0x3E8)
    OP_99(0x9, 0x3, 0x6, 0x3E8)
    OP_99(0x9, 0x3, 0x6, 0x3E8)
    Fade(250)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 11)
    SetChrSubChip(0x9, 0)
    OP_0D()
    OP_8F(0x9, 0xFFFFC252, 0x3B60, 0x23D2, 0x7D0, 0x0)

    ChrTalk(    #55
        0xB,
        "#260FHeeheehee.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, -7420, 15000, 13980, 270)
    SetChrPos(0x8, -7990, 15000, 14810, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #56
        0xA,
        "Man's Voice",
        (
            "#1PIndeed, you're a very good girl, Renne.\x01",
            "And a very good worker!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A4B():
        OP_8E(0xFE, 0xFFFFBC9E, 0x3B60, 0x1EDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2A4B)

    def lambda_2A66():
        OP_8E(0xFE, 0xFFFFC3C4, 0x3B60, 0x215C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2A66)
    Sleep(500)

    def lambda_2A86():
        OP_8E(0xFE, 0xFFFFC43C, 0x3B60, 0x2684, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2A86)

    def lambda_2AA1():
        OP_6D(-16030, 15200, 9710, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2AA1)

    def lambda_2AB9():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AB9)

    def lambda_2AC9():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AC9)
    WaitChrThread(0x9, 0x1)
    OP_8C(0x9, 90, 400)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #57
        0xB,
        (
            "#260FOh, hi, Professor...and Campanella!\x02\x03",

            "You're here, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#850FHello there, Renne! For now, yes.\x02\x03",

            "Looks like you had a good time in\x01",
            "Grancel, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        (
            "#260FYeah, kinda.\x02\x03",

            "Awww, if I knew you were coming,\x01",
            "I would've invited you!\x02\x03",

            "It was a lot of fun, you know!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2CB0")

    ChrTalk(    #60
        0x8,
        (
            "#850FHaha. Now I feel bad that I missed it.\x02\x03",

            "I had to put on a nice little puppet show\x01",
            "for some lady bracers...\x02\x03",

            "It wasn't nearly as enjoyable as what\x01",
            "you did, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D5F")

    label("loc_2CB0")


    ChrTalk(    #61
        0x8,
        (
            "#850FHaha. Now I feel bad that I missed it.\x02\x03",

            "I had to put on a nice little puppet show\x01",
            "for a big burly bracer...\x02\x03",

            "It wasn't nearly as enjoyable as what\x01",
            "you did, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5F")


    ChrTalk(    #62
        0xA,
        (
            "#1150FHaha... Perhaps you should have reserved\x01",
            "the better seat ahead of time, Campenella.\x02\x03",

            "By the way, Renne...\x02\x03",

            "I couldn't help but overhear. You said\x01",
            "you're rather fond of Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "#260FHaha, sure am.\x02\x03",

            "She wasn't nearly as nasty a person\x01",
            "as you said, Professor! She's nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "#1150FAh-ah, Renne! It's not nice to put words\x01",
            "in peoples' mouths. I never said she was\x01",
            "a bad person.\x02\x03",

            "If anything, I agree with you. She is both\x01",
            "a charming and fascinating young lady.\x02\x03",

            "I simply said that she's part of the reason\x01",
            "Joshua has yet to return to us.\x02\x03",

            "Wouldn't you agree, Loewe?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "#120FI won't deny that she's part of the reason,\x01",
            "yes.\x02\x03",

            "But--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#1150FWell, then, that should clear things up.\x01",
            "What do you think, Renne?\x02\x03",

            "Given the circumstances, shouldn't we\x01",
            "make Estelle one of our friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        "#120FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xB,
        (
            "#260FMake Estelle one of our friends...?\x02\x03",

            "Yeah... Yeah! That sounds like a lot of fun!\x02\x03",

            "She's kind of on the weak side right now,\x01",
            "but if we teach her how to kill right, I bet\x01",
            "she'd be really powerful!\x02\x03",

            "And if Estelle joins us, Joshua will come\x01",
            "back, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        "#1150FI think it's safe to assume as much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        (
            "#850FHahaha! Oh, Professor, I always knew\x01",
            "you had great taste. Delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#120FThat's going a little too far with your\x01",
            "'jokes,' Professor.\x02\x03",

            "Remember, 'All who serve the society\x01",
            "must do so of their own free will.'\x02\x03",

            "That is one of the core laws of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xA,
        (
            "#1150FYou need not remind me of the\x01",
            "Grandmaster's edicts, Loewe.\x02\x03",

            "Do you really think that I, an Anguis,\x01",
            "would break such a law?\x02\x03",

            "Neither you nor Joshua were forced\x01",
            "into anything, were you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "#120F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#1150FIn any case, breaking her will would be\x01",
            "so dissatisfying.\x02\x03",

            "When she joins us...it will be entirely of\x01",
            "her own volition.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1B0B end

    def Function_6_343B(): pass

    label("Function_6_343B")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_34B4"),
        (1, "loc_34BA"),
        (SWITCH_DEFAULT, "loc_34C0"),
    )


    label("loc_34B4")

    OP_A2(0x1200)
    Jump("loc_34C0")

    label("loc_34BA")

    OP_A2(0x1201)
    Jump("loc_34C0")

    label("loc_34C0")

    Return()

    # Function_6_343B end

    SaveToFile()

Try(main)
